"""
Script to parse Google Docs API XML documentation and generate Pydantic models
"""

import re
import sys
from pathlib import Path
from typing import Optional, Set, Tuple

from bs4 import BeautifulSoup


class Field:
    """Represents a field in a resource model"""

    def __init__(
        self,
        name: str,
        type_name: str,
        description: str,
        is_collection: bool = False,
        is_map: bool = False,
        map_key_type: str = None,
        map_value_type: str = None,
        is_enum: bool = False,
    ):
        self.name = name
        self.type_name = type_name
        self.description = description
        self.is_collection = is_collection
        self.is_map = is_map
        self.map_key_type = map_key_type
        self.map_value_type = map_value_type
        self.is_enum = is_enum


class ResourceModel:
    """Represents a resource model from the API documentation"""

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.fields: list[Field] = []
        self.url = ""


def _parse_map(schema: str) -> Optional[Tuple[str, str]]:
    pattern = re.compile(
        r"""map\s*\(\s*            # 'map (' とその前後の空白
            key:\s*(?P<key>.+?)    # key: の後に続く xxx を非貪欲で取得
            \s*,\s*               # カンマとその前後の空白
            value:\s*(?P<value>.+?)# value: の後に続く yyy を非貪欲で取得
            \s*\)$                # 終端の ')' とその前後の空白
        """,
        re.VERBOSE,
    )
    match = pattern.search(schema)
    if match:
        key_type = match.group("key").strip()
        value_type = match.group("value").strip()
        return key_type, value_type


def _parse_object(schema: str) -> Optional[str]:
    pattern_obj = re.compile(r"object\s*\(\s*(?P<inner>[^)]+)\s*\)$")
    match = pattern_obj.search(schema)
    if match:
        return match.group("inner").strip()
    return None


def _parse_enum(schema: str) -> Optional[str]:
    pattern_obj = re.compile(r"enum\s*\(\s*(?P<inner>[^)]+)\s*\)$")
    match = pattern_obj.search(schema)
    if match:
        return match.group("inner").strip()
    return None


def parse_field_type(
    type_text: str,
) -> Tuple[str, bool, bool, Optional[str], Optional[str], bool]:
    """
    Parse the field type text and determine:
    - The base type name
    - If it's a collection
    - If it's a map
    - Map key type (if applicable)
    - Map value type (if applicable)
    - If it's an enum
    """
    is_collection = False
    is_map = False
    map_key_type = None
    map_value_type = None
    is_enum = False
    type_text = re.sub(r"<[^>]+>", "", type_text).strip()
    if type_text.endswith("[]") or type_text.startswith("array of"):
        is_collection = True
        type_text = type_text.replace("[]", "").replace("array of", "").strip()
    map_match = _parse_map(type_text)
    if map_match is not None:
        is_map = True
        map_key_type, map_value_type = map_match
        object_match = _parse_object(map_value_type)
        if object_match is not None:
            map_value_type = object_match
    object_match = _parse_object(type_text)
    if object_match is not None:
        type_text = object_match
    enum_match = _parse_enum(type_text)
    if enum_match is not None:
        is_enum = True
        type_text = enum_match
    return type_text, is_collection, is_map, map_key_type, map_value_type, is_enum


def clean_description(desc: str) -> str:
    """Clean up description text"""
    desc = re.sub(r"\s+", " ", desc)
    desc = re.sub(r"<[^>]+>", "", desc)
    return desc.strip()


def parse_models_from_xml(xml_content: str) -> list[ResourceModel]:
    """Parse resource models from the XML documentation"""
    soup = BeautifulSoup(xml_content, "html.parser")
    models = []
    resource_sections = soup.find_all("section")
    empty_object_types = set()
    toc_links = soup.select("ul.toc li a")
    for link in toc_links:
        resource_name = link.text.strip()
        href = link.get("href", "")
        if "#" in href:
            resource_id = href.split("#")[-1]
            if resource_id.endswith("SuggestionState") or "Type" in resource_id:
                empty_object_types.add(resource_id)
    for section in resource_sections:
        section_id = section.get("id", "")
        if not section_id or section_id.startswith("/"):
            continue
        h2_elem = section.find("h2")
        if h2_elem is None:
            continue
        resource_name = section_id
        description = ""
        desc_section = soup.find("section", {"id": section_id + ".description"})
        if desc_section is not None and desc_section.find("p") is not None:
            description = clean_description(desc_section.find("p").text or "")
        model = ResourceModel(resource_name, description)
        h2_span = h2_elem.find("span", {"class": "devsite-heading"})
        if h2_span is not None and h2_span.text:
            resource_name = h2_span.text.replace("Resource:", "").strip()
            model.name = resource_name
        h2_id = h2_elem.get("id", "")
        if h2_id:
            model.url = f"https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#{h2_id}"
        enum_section = section.find("section", {"id": section_id + ".ENUM_VALUES"})
        if enum_section is not None:
            enum_table = enum_section.find("table")
            if enum_table is not None:
                enum_rows = enum_table.find_all("tr")
                for row in enum_rows:
                    if row.find("th"):
                        continue
                    cells = row.find_all("td")
                    if len(cells) < 2:
                        continue
                    enum_value_elem = cells[0].find("code", {"class": "apitype"})
                    if enum_value_elem is None or not enum_value_elem.text:
                        continue
                    enum_value = enum_value_elem.text.strip().replace("<wbr>", "")
                    enum_description = cells[1].text.strip()
                    field = Field(
                        name=enum_value,
                        type_name="str",
                        description=enum_description,
                        is_enum=True,
                    )
                    model.fields.append(field)
        fields_section = section.find("section", {"id": section_id + ".FIELDS"})
        if fields_section is not None and not enum_section:
            fields_table = fields_section.find(
                "table", {"id": section_id + ".FIELDS-table"}
            )
            if fields_table is not None:
                field_rows = fields_table.find_all("tr")
                for row in field_rows:
                    field_td = row.find_all("td")
                    if len(field_td) < 2:
                        continue
                    field_name = field_td[0].find("code")
                    if field_name is None or not field_name.text:
                        continue
                    raw_name = field_name.text.strip()
                    field_name_cleaned = re.sub(
                        r"(?<!^)(?=[A-Z])", "_", raw_name
                    ).lower()
                    field_name_cleaned = field_name_cleaned.replace("[]", "")
                    field_name_cleaned = field_name_cleaned.replace(".", "_")
                    field_name_cleaned = re.sub(r"[\[\]]", "", field_name_cleaned)
                    field_type_elem = field_td[1].find("p")
                    if not field_type_elem:
                        continue
                    field_type = field_type_elem.find("code", {"class": "apitype"})
                    if field_type is None or not field_type.text:
                        continue
                    type_text = field_type.text.strip()
                    (
                        type_name,
                        is_collection,
                        is_map,
                        map_key_type,
                        map_value_type,
                        is_enum,
                    ) = parse_field_type(type_text)
                    description_paras = field_td[1].find_all("p")
                    description = ""
                    for p in description_paras[1:]:
                        if p.text:
                            description += clean_description(p.text) + " "
                    field = Field(
                        field_name_cleaned,
                        type_name,
                        description.strip(),
                        is_collection,
                        is_map,
                        map_key_type,
                        map_value_type,
                        is_enum,
                    )
                    model.fields.append(field)
        models.append(model)
    for empty_type in empty_object_types:
        if not any(model.name == empty_type for model in models):
            empty_model = ResourceModel(empty_type, "This type has no fields.")
            empty_model.url = f"https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#{empty_type}"
            empty_model.fields = []
            models.append(empty_model)
    return models


def generate_pydantic_models(models: list[ResourceModel]) -> str:
    """Generate Pydantic model classes from the parsed models"""
    type_mapping = {
        "string": "str",
        "integer": "int",
        "number": "float",
        "boolean": "bool",
        "object": "dict",
        "array": "list",
    }
    enum_models = []
    regular_models = []
    for model in models:
        if model.name.endswith("Type") or (
            model.fields
            and any(field.is_enum for field in model.fields)
            and len(model.fields) == 1
        ):
            enum_models.append(model)
        else:
            regular_models.append(model)
    model_names = [m.name for m in models]
    model_dict = {m.name: m for m in models}
    dependencies: dict[str, Set[str]] = {}
    for model in regular_models:
        dependencies[model.name] = set()
        for field in model.fields:
            if field.type_name in model_names and field.type_name not in [
                m.name for m in enum_models
            ]:
                dependencies[model.name].add(field.type_name)
            if (
                field.is_map
                and field.map_value_type in model_names
                and field.map_value_type not in [m.name for m in enum_models]
            ):
                dependencies[model.name].add(field.map_value_type)
    result = [
        "from __future__ import annotations",
        "",
        "from enum import Enum",
        "from typing import Any, Optional, Union",
        "from pydantic import BaseModel, ConfigDict, Field, alias_generators",
        "",
        "",
    ]
    for model in sorted(enum_models, key=lambda m: m.name):
        model_code = generate_model_code(model, models)
        result.append(model_code)
    remaining_models = set(model.name for model in regular_models)
    added_models = set()
    added_models.update(model.name for model in enum_models)
    while remaining_models:
        progress_made = False
        for model_name in sorted(list(remaining_models)):
            deps = dependencies.get(model_name, set())
            if all(dep in added_models for dep in deps):
                model = model_dict.get(model_name)
                if model:
                    model_code = generate_model_code(model, models)
                    result.append(model_code)
                added_models.add(model_name)
                remaining_models.remove(model_name)
                progress_made = True
        if not progress_made and remaining_models:
            model_name = sorted(list(remaining_models))[0]
            model = model_dict.get(model_name)
            if model:
                model_code = generate_model_code(model, models)
                result.append(model_code)
            added_models.add(model_name)
            remaining_models.remove(model_name)
    return "\n".join(result)


def generate_model_code(model: ResourceModel, all_models: list[ResourceModel]) -> str:
    """Generate code for a specific model"""
    model_names = [m.name for m in all_models]
    lines = [
        f"class {model.name}(BaseModel):",
        f'    """',
        f"    {model.description}",
    ]
    if model.url:
        lines.append(f"    {model.url}")
    lines.extend(
        [
            f'    """',
            "    model_config = ConfigDict(",
            "        populate_by_name=True,",
            "        alias_generator=alias_generators.to_camel,",
            "    )",
            "",
        ]
    )
    if model.name.endswith("Type") or (
        any(field.is_enum for field in model.fields) and len(model.fields) == 1
    ):
        lines = [
            f"class {model.name}(str, Enum):",
            f'    """',
            f"    {model.description}",
        ]
        if model.url:
            lines.append(f"    {model.url}")
        lines.append(f'    """')
        if model.fields:
            for field in model.fields:
                enum_value = field.name.upper()
                lines.append(
                    f'    {enum_value} = "{field.name}"  # {field.description}'
                )
        else:
            lines.append(f"    # No enum values defined in the API documentation")
            lines.append(f'    UNSPECIFIED = "UNSPECIFIED"')
    else:
        if not model.fields:
            lines.append("    pass")
        else:
            for field in model.fields:
                field_type = get_python_type(field, model_names)
                description = field.description.replace('"', '\\"')
                description_lines = []
                for i in range(0, len(description), 100):
                    description_lines.append(description[i : i + 100])
                if len(description_lines) == 1:
                    field_line = f'    {field.name}: {field_type} = Field(description="{description}")'
                else:
                    field_line = f"    {field.name}: {field_type} = Field(\n        description=(\n"
                    for i, line in enumerate(description_lines):
                        if i < len(description_lines) - 1:
                            field_line += f'            "{line}"\n'
                        else:
                            field_line += f'            "{line}"\n'
                    field_line += "        )\n    )"
                lines.append(field_line)
    lines.append("")
    return "\n".join(lines)


def get_python_type(field: Field, model_names: list[str]) -> str:
    """Determine the Python type annotation for a field"""
    type_mapping = {
        "string": "str",
        "integer": "int",
        "number": "float",
        "boolean": "bool",
    }
    if field.is_enum:
        return f"Optional[{field.type_name}]"
    base_type = type_mapping.get(field.type_name.lower(), field.type_name)
    if field.type_name in model_names:
        base_type = field.type_name
    if field.is_collection:
        return f"list[{base_type}]"
    if field.is_map:
        key_type = type_mapping.get(field.map_key_type.lower(), field.map_key_type)
        value_type = field.map_value_type
        if field.map_value_type in model_names:
            value_type = field.map_value_type
        else:
            value_type = type_mapping.get(field.map_value_type.lower(), "Any")
        return f"dict[{key_type}, {value_type}]"
    return f"Optional[{base_type}]"


def main():
    xml_content = ""
    if len(sys.argv) > 1:
        xml_file = Path(sys.argv[1])
        if xml_file.exists():
            xml_content = xml_file.read_text(encoding="utf-8")
    else:
        xml_content = sys.stdin.read()
    doc_match = re.search(
        r"<document_content>(.*?)</document_content>", xml_content, re.DOTALL
    )
    if doc_match:
        xml_content = doc_match.group(1)
    models = parse_models_from_xml(xml_content)
    code = generate_pydantic_models(models)
    Path("draft.py").write_text(code, encoding="utf-8")


if __name__ == "__main__":
    main()
