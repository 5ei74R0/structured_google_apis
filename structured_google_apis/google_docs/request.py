from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, alias_generators

from .resource import (
    DocumentStyle,
    ParagraphStyle,
    Range,
    SectionStyle,
    Size,
    TableCellStyle,
    TableColumnProperties,
    TableRowStyle,
    TextStyle,
)


class HeaderFooterType(str, Enum):
    """
    The types of headers and footers that can be created.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#headerfootertype
    """

    HEADER_FOOTER_TYPE_UNSPECIFIED = (
        "HEADER_FOOTER_TYPE_UNSPECIFIED"  # The header/footer type is unspecified.
    )
    DEFAULT = "DEFAULT"  # A default header/footer.


class BulletGlyphPreset(str, Enum):
    """
    Preset patterns of bullet glyphs for lists.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#bulletglyphpreset
    """

    BULLET_GLYPH_PRESET_UNSPECIFIED = (
        "BULLET_GLYPH_PRESET_UNSPECIFIED"  # The bullet glyph preset is unspecified.
    )
    BULLET_DISC_CIRCLE_SQUARE = "BULLET_DISC_CIRCLE_SQUARE"  # A bulleted list with a DISC, CIRCLE and SQUARE bullet glyph for the first 3 list nesting levels.
    BULLET_DIAMONDX_ARROW3D_SQUARE = "BULLET_DIAMONDX_ARROW3D_SQUARE"  # A bulleted list with a DIAMONDX, ARROW3D and SQUARE bullet glyph for the first 3 list nesting levels.
    BULLET_CHECKBOX = "BULLET_CHECKBOX"  # A bulleted list with CHECKBOX bullet glyphs for all list nesting levels.
    BULLET_ARROW_DIAMOND_DISC = "BULLET_ARROW_DIAMOND_DISC"  # A bulleted list with a ARROW, DIAMOND and DISC bullet glyph for the first 3 list nesting levels.
    BULLET_STAR_CIRCLE_SQUARE = "BULLET_STAR_CIRCLE_SQUARE"  # A bulleted list with a STAR, CIRCLE and SQUARE bullet glyph for the first 3 list nesting levels.
    BULLET_ARROW3D_CIRCLE_SQUARE = "BULLET_ARROW3D_CIRCLE_SQUARE"  # A bulleted list with a ARROW3D, CIRCLE and SQUARE bullet glyph for the first 3 list nesting levels.
    BULLET_LEFTTRIANGLE_DIAMOND_DISC = "BULLET_LEFTTRIANGLE_DIAMOND_DISC"  # A bulleted list with a LEFTTRIANGLE, DIAMOND and DISC bullet glyph for the first 3 list nesting levels.
    BULLET_DIAMONDX_HOLLOWDIAMOND_SQUARE = "BULLET_DIAMONDX_HOLLOWDIAMOND_SQUARE"  # A bulleted list with a DIAMONDX, HOLLOWDIAMOND and SQUARE bullet glyph for the first 3 list nesting levels.
    BULLET_DIAMOND_CIRCLE_SQUARE = "BULLET_DIAMOND_CIRCLE_SQUARE"  # A bulleted list with a DIAMOND, CIRCLE and SQUARE bullet glyph for the first 3 list nesting levels.
    NUMBERED_DECIMAL_ALPHA_ROMAN = "NUMBERED_DECIMAL_ALPHA_ROMAN"  # A numbered list with DECIMAL, ALPHA and ROMAN numeric glyphs for the first 3 list nesting levels, followed by periods.
    NUMBERED_DECIMAL_ALPHA_ROMAN_PARENS = "NUMBERED_DECIMAL_ALPHA_ROMAN_PARENS"  # A numbered list with DECIMAL, ALPHA and ROMAN numeric glyphs for the first 3 list nesting levels, followed by parenthesis.
    NUMBERED_DECIMAL_NESTED = "NUMBERED_DECIMAL_NESTED"  # A numbered list with DECIMAL numeric glyphs separated by periods, where each nesting level uses the previous nesting level's glyph as a prefix. For example: '1.', '1.1.', '2.', '2.2.'.
    NUMBERED_UPPERALPHA_ALPHA_ROMAN = "NUMBERED_UPPERALPHA_ALPHA_ROMAN"  # A numbered list with UPPERALPHA, ALPHA and ROMAN numeric glyphs for the first 3 list nesting levels, followed by periods.
    NUMBERED_UPPERROMAN_UPPERALPHA_DECIMAL = "NUMBERED_UPPERROMAN_UPPERALPHA_DECIMAL"  # A numbered list with UPPERROMAN, UPPERALPHA and DECIMAL numeric glyphs for the first 3 list nesting levels, followed by periods.
    NUMBERED_ZERODECIMAL_ALPHA_ROMAN = "NUMBERED_ZERODECIMAL_ALPHA_ROMAN"  # A numbered list with ZERODECIMAL, ALPHA and ROMAN numeric glyphs for the first 3 list nesting levels, followed by periods.


class CreateNamedRangeRequest(BaseModel):
    """
    Creates a NamedRange referencing the given range.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#createnamedrangerequest
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    name: Optional[str] = Field(
        description=(
            "The name of the NamedRange. Names do not need to be unique. Names must be at least 1 character and n",
            "o more than 256 characters, measured in UTF-16 code units.",
        ),
        default=None,
    )
    range: Optional[Range] = Field(
        description="The range to apply the name to.",
        default=None,
    )


class CreateParagraphBulletsRequest(str, Enum):
    """
    Creates bullets for all of the paragraphs that overlap with the given range.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#createparagraphbulletsrequest
    """

    RANGE = "range"  # The range to apply the bullet preset to.
    BULLET_PRESET = "bullet_preset"  # The kinds of bullet glyphs to be used.


class DeleteContentRangeRequest(BaseModel):
    """
    Deletes content from the document.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#deletecontentrangerequest
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    range: Optional[Range] = Field(
        description=(
            "The range of content to delete. Deleting text that crosses a paragraph boundary may result in change",
            "s to paragraph styles, lists, positioned objects and bookmarks as the two paragraphs are merged. Att",
            "empting to delete certain ranges can result in an invalid document structure in which case a 400 bad",
            " request error is returned. Some examples of invalid delete requests include:",
        ),
        default=None,
    )


class DeleteFooterRequest(BaseModel):
    """
    Deletes a Footer from the document.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#deletefooterrequest
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    footer_id: Optional[str] = Field(
        description=(
            "The id of the footer to delete. If this footer is defined on DocumentStyle, the reference to this fo",
            "oter is removed, resulting in no footer of that type for the first section of the document. If this ",
            "footer is defined on a SectionStyle, the reference to this footer is removed and the footer of that ",
            "type is now continued from the previous section.",
        ),
        default=None,
    )
    tab_id: Optional[str] = Field(
        description=(
            "The tab that contains the footer to delete. When omitted, the request is applied to the first tab. I",
            "n a document containing a single tab: If provided, must match the singular tab's ID. If omitted, the",
            " request applies to the singular tab. In a document containing multiple tabs: If provided, the reque",
            "st applies to the specified tab. If omitted, the request applies to the first tab in the document.",
        ),
        default=None,
    )


class DeleteHeaderRequest(BaseModel):
    """
    Deletes a Header from the document.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#deleteheaderrequest
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    header_id: Optional[str] = Field(
        description=(
            "The id of the header to delete. If this header is defined on DocumentStyle, the reference to this he",
            "ader is removed, resulting in no header of that type for the first section of the document. If this ",
            "header is defined on a SectionStyle, the reference to this header is removed and the header of that ",
            "type is now continued from the previous section.",
        ),
        default=None,
    )
    tab_id: Optional[str] = Field(
        description=(
            "The tab containing the header to delete. When omitted, the request is applied to the first tab. In a",
            " document containing a single tab: If provided, must match the singular tab's ID. If omitted, the re",
            "quest applies to the singular tab. In a document containing multiple tabs: If provided, the request ",
            "applies to the specified tab. If omitted, the request applies to the first tab in the document.",
        ),
        default=None,
    )


class DeleteParagraphBulletsRequest(BaseModel):
    """
    Deletes bullets from all of the paragraphs that overlap with the given range.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#deleteparagraphbulletsrequest
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    range: Optional[Range] = Field(
        description="The range to delete bullets from.",
        default=None,
    )


class DeletePositionedObjectRequest(BaseModel):
    """
    Deletes a PositionedObject from the document.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#deletepositionedobjectrequest
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    object_id: Optional[str] = Field(
        description="The ID of the positioned object to delete.",
        default=None,
    )
    tab_id: Optional[str] = Field(
        description=(
            "The tab that the positioned object to delete is in. When omitted, the request is applied to the firs",
            "t tab. In a document containing a single tab: If provided, must match the singular tab's ID. If omit",
            "ted, the request applies to the singular tab. In a document containing multiple tabs: If provided, t",
            "he request applies to the specified tab. If omitted, the request applies to the first tab in the doc",
            "ument.",
        ),
        default=None,
    )


class EndOfSegmentLocation(BaseModel):
    """
    Location at the end of a body, header, footer or footnote. The location is immediately before the last newline in the document segment.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#endofsegmentlocation
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    segment_id: Optional[str] = Field(
        description=(
            "The ID of the header, footer or footnote the location is in. An empty segment ID signifies the docum",
            "ent's body.",
        ),
        default=None,
    )
    tab_id: Optional[str] = Field(
        description=(
            "The tab that the location is in. When omitted, the request is applied to the first tab. In a documen",
            "t containing a single tab: If provided, must match the singular tab's ID. If omitted, the request ap",
            "plies to the singular tab. In a document containing multiple tabs: If provided, the request applies ",
            "to the specified tab. If omitted, the request applies to the first tab in the document.",
        ),
        default=None,
    )


class ImageReplaceMethod(str, Enum):
    """
    The image replace method.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#imagereplacemethod
    """

    IMAGE_REPLACE_METHOD_UNSPECIFIED = "IMAGE_REPLACE_METHOD_UNSPECIFIED"  # Unspecified image replace method. This value must not be used.
    CENTER_CROP = "CENTER_CROP"  # Scales and centers the image to fill the bounds of the original image. The image may be cropped in order to fill the original image's bounds. The rendered size of the image will be the same as the original image.


class Location(BaseModel):
    """
    A particular location in the document.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#location
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    segment_id: Optional[str] = Field(
        description=(
            "The ID of the header, footer or footnote the location is in. An empty segment ID signifies the docum",
            "ent's body.",
        ),
        default=None,
    )
    index: Optional[int] = Field(
        description=(
            "The zero-based index, in UTF-16 code units. The index is relative to the beginning of the segment sp",
            "ecified by segmentId.",
        ),
        default=None,
    )
    tab_id: Optional[str] = Field(
        description=(
            "The tab that the location is in. When omitted, the request is applied to the first tab. In a documen",
            "t containing a single tab: If provided, must match the singular tab's ID. If omitted, the request ap",
            "plies to the singular tab. In a document containing multiple tabs: If provided, the request applies ",
            "to the specified tab. If omitted, the request applies to the first tab in the document.",
        ),
        default=None,
    )


class PinTableHeaderRowsRequest(BaseModel):
    """
    Updates the number of pinned table header rows in a table.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#pintableheaderrowsrequest
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    table_start_location: Optional[Location] = Field(
        description="The location where the table starts in the document.",
        default=None,
    )
    pinned_header_rows_count: Optional[int] = Field(
        description="The number of table rows to pin, where 0 implies that all rows are unpinned.",
        default=None,
    )


class ReplaceImageRequest(str, Enum):
    """
    Replaces an existing image with a new image.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#replaceimagerequest
    """

    IMAGE_OBJECT_ID = "image_object_id"  # The ID of the existing image that will be replaced. The ID can be retrieved from the response of a get request.
    URI = "uri"  # The URI of the new image. The image is fetched once at insertion time and a copy is stored for display inside the document. Images must be less than 50MB, cannot exceed 25 megapixels, and must be in PNG, JPEG, or GIF format. The provided URI can't surpass 2 KB in length. The URI is saved with the image, and exposed through the ImageProperties.source_uri field.
    IMAGE_REPLACE_METHOD = "image_replace_method"  # The replacement method.
    TAB_ID = "tab_id"  # The tab that the image to be replaced is in. When omitted, the request is applied to the first tab. In a document containing a single tab: If provided, must match the singular tab's ID. If omitted, the request applies to the singular tab. In a document containing multiple tabs: If provided, the request applies to the specified tab. If omitted, the request applies to the first tab in the document.


class SubstringMatchCriteria(BaseModel):
    """
    A criteria that matches a specific string of text in the document.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#substringmatchcriteria
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    text: Optional[str] = Field(
        description="The text to search for in the document.",
        default=None,
    )
    match_case: Optional[bool] = Field(
        description="Indicates whether the search should respect case:",
        default=None,
    )
    search_by_regex: Optional[list[bool]] = Field(
        description=(
            "Optional. True if the find value should be treated as a regular expression. Any backslashes in the p",
            "attern should be escaped.",
        ),
        default=None,
    )


class TableCellLocation(BaseModel):
    """
    Location of a single cell within a table.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#tablecelllocation
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    table_start_location: Optional[Location] = Field(
        description="The location where the table starts in the document.",
        default=None,
    )
    row_index: Optional[int] = Field(
        description="The zero-based row index. For example, the second row in the table has a row index of 1.",
        default=None,
    )
    column_index: Optional[int] = Field(
        description="The zero-based column index. For example, the second column in the table has a column index of 1.",
        default=None,
    )


class TableRange(BaseModel):
    """
    A table range represents a reference to a subset of a table.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#tablerange
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    table_cell_location: Optional[TableCellLocation] = Field(
        description="The cell location where the table range starts.",
        default=None,
    )
    row_span: Optional[int] = Field(
        description="The row span of the table range.",
        default=None,
    )
    column_span: Optional[int] = Field(
        description="The column span of the table range.",
        default=None,
    )


class TabsCriteria(BaseModel):
    """
    A criteria that specifies in which tabs a request executes.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#tabscriteria
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    tab_ids: Optional[str] = Field(
        description="The list of tab IDs in which the request executes.",
        default=None,
    )


class UnmergeTableCellsRequest(BaseModel):
    """
    Unmerges cells in a Table.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#unmergetablecellsrequest
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    table_range: Optional[TableRange] = Field(
        description=(
            "The table range specifying which cells of the table to unmerge. All merged cells in this range will ",
            "be unmerged, and cells that are already unmerged will not be affected. If the range has no merged ce",
            "lls, the request will do nothing. If there is text in any of the merged cells, the text will remain ",
            'in the "head" cell of the resulting block of unmerged cells. The "head" cell is the upper-left c',
            "ell when the content direction is from left to right, and the upper-right otherwise.",
        ),
        default=None,
    )


class UpdateDocumentStyleRequest(BaseModel):
    """
    Updates the DocumentStyle.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#updatedocumentstylerequest
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    document_style: Optional[DocumentStyle] = Field(
        description=(
            "The styles to set on the document. Certain document style changes may cause other changes in order t",
            "o mirror the behavior of the Docs editor. See the documentation of DocumentStyle for more informatio",
            "n.",
        ),
        default=None,
    )
    fields: Optional[str] = Field(
        description=(
            "The fields that should be updated. At least one field must be specified. The root documentStyle is i",
            'mplied and should not be specified. A single "*" can be used as short-hand for listing every field',
            '. For example to update the background, set fields to "background".',
        ),
        default=None,
    )
    tab_id: Optional[str] = Field(
        description=(
            "The tab that contains the style to update. When omitted, the request applies to the first tab. In a ",
            "document containing a single tab: If provided, must match the singular tab's ID. If omitted, the req",
            "uest applies to the singular tab. In a document containing multiple tabs: If provided, the request a",
            "pplies to the specified tab. If not provided, the request applies to the first tab in the document.",
        ),
        default=None,
    )


class UpdateParagraphStyleRequest(BaseModel):
    """
    Update the styling of all paragraphs that overlap with the given range.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#updateparagraphstylerequest
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    paragraph_style: Optional[ParagraphStyle] = Field(
        description=(
            "The styles to set on the paragraphs. Certain paragraph style changes may cause other changes in orde",
            "r to mirror the behavior of the Docs editor. See the documentation of ParagraphStyle for more inform",
            "ation.",
        ),
        default=None,
    )
    fields: Optional[str] = Field(
        description=(
            "The fields that should be updated. At least one field must be specified. The root paragraphStyle is ",
            'implied and should not be specified. A single "*" can be used as short-hand for listing every fiel',
            'd. For example, to update the paragraph style\'s alignment property, set fields to "alignment". To ',
            "reset a property to its default value, include its field name in the field mask but leave the field ",
            "itself unset.",
        ),
        default=None,
    )
    range: Optional[Range] = Field(
        description="The range overlapping the paragraphs to style.",
        default=None,
    )


class UpdateSectionStyleRequest(BaseModel):
    """
    Updates the SectionStyle.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#updatesectionstylerequest
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    range: Optional[Range] = Field(
        description=(
            "The range overlapping the sections to style. Because section breaks can only be inserted inside the ",
            "body, the segment ID field must be empty.",
        ),
        default=None,
    )
    section_style: Optional[SectionStyle] = Field(
        description=(
            "The styles to be set on the section. Certain section style changes may cause other changes in order ",
            "to mirror the behavior of the Docs editor. See the documentation of SectionStyle for more informatio",
            "n.",
        ),
        default=None,
    )
    fields: Optional[str] = Field(
        description=(
            "The fields that should be updated. At least one field must be specified. The root sectionStyle is im",
            'plied and must not be specified. A single "*" can be used as short-hand for listing every field. F',
            'or example to update the left margin, set fields to "marginLeft".',
        ),
        default=None,
    )


class UpdateTableCellStyleRequest(BaseModel):
    """
    Updates the style of a range of table cells.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#updatetablecellstylerequest
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    table_cell_style: Optional[TableCellStyle] = Field(
        description=(
            "The style to set on the table cells. When updating borders, if a cell shares a border with an adjace",
            "nt cell, the corresponding border property of the adjacent cell is updated as well. Borders that are",
            " merged and invisible are not updated. Since updating a border shared by adjacent cells in the same ",
            "request can cause conflicting border updates, border updates are applied in the following order:",
        ),
        default=None,
    )
    fields: Optional[str] = Field(
        description=(
            "The fields that should be updated. At least one field must be specified. The root tableCellStyle is ",
            'implied and should not be specified. A single "*" can be used as short-hand for listing every fiel',
            'd. For example to update the table cell background color, set fields to "backgroundColor". To rese',
            "t a property to its default value, include its field name in the field mask but leave the field itse",
            "lf unset.",
        ),
        default=None,
    )
    table_range: Optional[TableRange] = Field(
        description="The table range representing the subset of the table to which the updates are applied.",
        default=None,
    )
    table_start_location: Optional[Location] = Field(
        description=(
            "The location where the table starts in the document. When specified, the updates are applied to all ",
            "the cells in the table.",
        ),
        default=None,
    )


class UpdateTableColumnPropertiesRequest(BaseModel):
    """
    Updates the TableColumnProperties of columns in a table.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#updatetablecolumnpropertiesrequest
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    table_start_location: Optional[list[Location]] = Field(
        description="The location where the table starts in the document.",
        default=None,
    )
    column_indices: Optional[int] = Field(
        description=(
            "The list of zero-based column indices whose property should be updated. If no indices are specified,",
            " all columns will be updated.",
        ),
        default=None,
    )
    table_column_properties: Optional[TableColumnProperties] = Field(
        description=(
            "The table column properties to update. If the value of tableColumnProperties#width is less than 5 po",
            "ints (5/72 inch), a 400 bad request error is returned.",
        ),
        default=None,
    )
    fields: Optional[str] = Field(
        description=(
            "The fields that should be updated. At least one field must be specified. The root tableColumnPropert",
            'ies is implied and should not be specified. A single "*" can be used as short-hand for listing eve',
            'ry field. For example to update the column width, set fields to "width".',
        ),
        default=None,
    )


class UpdateTableRowStyleRequest(BaseModel):
    """
    Updates the TableRowStyle of rows in a table.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#updatetablerowstylerequest
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    table_start_location: Optional[list[Location]] = Field(
        description="The location where the table starts in the document.",
        default=None,
    )
    row_indices: Optional[int] = Field(
        description=(
            "The list of zero-based row indices whose style should be updated. If no indices are specified, all r",
            "ows will be updated.",
        ),
        default=None,
    )
    table_row_style: Optional[TableRowStyle] = Field(
        description="The styles to be set on the rows.",
        default=None,
    )
    fields: Optional[str] = Field(
        description=(
            "The fields that should be updated. At least one field must be specified. The root tableRowStyle is i",
            'mplied and should not be specified. A single "*" can be used as short-hand for listing every field',
            '. For example to update the minimum row height, set fields to "minRowHeight".',
        ),
        default=None,
    )


class UpdateTextStyleRequest(BaseModel):
    """
    Update the styling of text.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#updatetextstylerequest
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    text_style: Optional[TextStyle] = Field(
        description=(
            "The styles to set on the text. If the value for a particular style matches that of the parent, that ",
            "style will be set to inherit. Certain text style changes may cause other changes in order to to mirr",
            "or the behavior of the Docs editor. See the documentation of TextStyle for more information.",
        ),
        default=None,
    )
    fields: Optional[str] = Field(
        description=(
            "The fields that should be updated. At least one field must be specified. The root textStyle is impli",
            'ed and should not be specified. A single "*" can be used as short-hand for listing every field. Fo',
            'r example, to update the text style to bold, set fields to "bold". To reset a property to its defa',
            "ult value, include its field name in the field mask but leave the field itself unset.",
        ),
        default=None,
    )
    range: Optional[Range] = Field(
        description=(
            "The range of text to style. The range may be extended to include adjacent newlines. If the range ful",
            "ly contains a paragraph belonging to a list, the paragraph's bullet is also updated with the matchin",
            "g text style. Ranges cannot be inserted inside a relative UpdateTextStyleRequest.",
        ),
        default=None,
    )


class CreateFooterRequest(str, Enum):
    """
    Creates a Footer. The new footer is applied to the SectionStyle at the location of the SectionBreak if specified, otherwise it is applied to the DocumentStyle.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#createfooterrequest
    """

    TYPE = "type"  # The type of footer to create.
    SECTION_BREAK_LOCATION = "section_break_location"  # The location of the SectionBreak immediately preceding the section whose SectionStyle this footer should belong to. If this is unset or refers to the first section break in the document, the footer applies to the document style.


class CreateFootnoteRequest(BaseModel):
    """
    Creates a Footnote segment and inserts a new FootnoteReference to it at the given location.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#createfootnoterequest
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    location: Optional[Location] = Field(
        description=(
            "Inserts the footnote reference at a specific index in the document. The footnote reference must be i",
            "nserted inside the bounds of an existing Paragraph. For instance, it cannot be inserted at a table's",
            " start index (i.e. between the table and its preceding paragraph). Footnote references cannot be ins",
            "erted inside an equation, header, footer or footnote. Since footnote references can only be inserted",
            " in the body, the segment ID field must be empty.",
        ),
        default=None,
    )
    end_of_segment_location: Optional[EndOfSegmentLocation] = Field(
        description=(
            "Inserts the footnote reference at the end of the document body. Footnote references cannot be insert",
            "ed inside a header, footer or footnote. Since footnote references can only be inserted in the body, ",
            "the segment ID field must be empty.",
        ),
        default=None,
    )


class CreateHeaderRequest(str, Enum):
    """
    Creates a Header. The new header is applied to the SectionStyle at the location of the SectionBreak if specified, otherwise it is applied to the DocumentStyle.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#createheaderrequest
    """

    TYPE = "type"  # The type of header to create.
    SECTION_BREAK_LOCATION = "section_break_location"  # The location of the SectionBreak which begins the section this header should belong to. If `sectionBreakLocation' is unset or if it refers to the first section break in the document body, the header applies to the DocumentStyle


class DeleteNamedRangeRequest(BaseModel):
    """
    Deletes a NamedRange.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#deletenamedrangerequest
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    tabs_criteria: Optional[TabsCriteria] = Field(
        description=(
            "Optional. The criteria used to specify which tab(s) the range deletion should occur in. When omitted",
            ", the range deletion is applied to all tabs. In a document containing a single tab: If provided, mus",
            "t match the singular tab's ID. If omitted, the range deletion applies to the singular tab. In a docu",
            "ment containing multiple tabs: If provided, the range deletion applies to the specified tabs. If not",
            " provided, the range deletion applies to all tabs.",
        ),
        default=None,
    )
    named_range_id: Optional[str] = Field(
        description="The ID of the named range to delete.",
        default=None,
    )
    name: Optional[str] = Field(
        description="The name of the range(s) to delete. All named ranges with the given name will be deleted.",
        default=None,
    )


class DeleteTableColumnRequest(BaseModel):
    """
    Deletes a column from a table.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#deletetablecolumnrequest
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    table_cell_location: Optional[TableCellLocation] = Field(
        description=(
            "The reference table cell location from which the column will be deleted. The column this cell spans ",
            "will be deleted. If this is a merged cell that spans multiple columns, all columns that the cell spa",
            "ns will be deleted. If no columns remain in the table after this deletion, the whole table is delete",
            "d.",
        ),
        default=None,
    )


class DeleteTableRowRequest(BaseModel):
    """
    Deletes a row from a table.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#deletetablerowrequest
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    table_cell_location: Optional[TableCellLocation] = Field(
        description=(
            "The reference table cell location from which the row will be deleted. The row this cell spans will b",
            "e deleted. If this is a merged cell that spans multiple rows, all rows that the cell spans will be d",
            "eleted. If no rows remain in the table after this deletion, the whole table is deleted.",
        ),
        default=None,
    )


class InsertInlineImageRequest(BaseModel):
    """
    Inserts an InlineObject containing an image at the given location.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#insertinlineimagerequest
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    uri: Optional[str] = Field(
        description=(
            "The image URI. The image is fetched once at insertion time and a copy is stored for display inside t",
            "he document. Images must be less than 50MB in size, cannot exceed 25 megapixels, and must be in one ",
            "of PNG, JPEG, or GIF format. The provided URI must be publicly accessible and at most 2 kB in length",
            ". The URI itself is saved with the image, and exposed via the ImageProperties.content_uri field.",
        ),
        default=None,
    )
    object_size: Optional[Size] = Field(
        description=(
            "The size that the image should appear as in the document. This property is optional and the final si",
            "ze of the image in the document is determined by the following rules: * If neither width nor height ",
            "is specified, then a default size of the image is calculated based on its resolution. * If one dimen",
            "sion is specified then the other dimension is calculated to preserve the aspect ratio of the image. ",
            "* If both width and height are specified, the image is scaled to fit within the provided dimensions ",
            "while maintaining its aspect ratio.",
        ),
        default=None,
    )
    location: Optional[Location] = Field(
        description=(
            "Inserts the image at a specific index in the document. The image must be inserted inside the bounds ",
            "of an existing Paragraph. For instance, it cannot be inserted at a table's start index (i.e. between",
            " the table and its preceding paragraph). Inline images cannot be inserted inside a footnote or equat",
            "ion.",
        ),
        default=None,
    )
    end_of_segment_location: Optional[EndOfSegmentLocation] = Field(
        description=(
            "Inserts the text at the end of a header, footer or the document body. Inline images cannot be insert",
            "ed inside a footnote.",
        ),
        default=None,
    )


class InsertPageBreakRequest(BaseModel):
    """
    Inserts a page break followed by a newline at the specified location.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#insertpagebreakrequest
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    location: Optional[Location] = Field(
        description=(
            "Inserts the page break at a specific index in the document. The page break must be inserted inside t",
            "he bounds of an existing Paragraph. For instance, it cannot be inserted at a table's start index (i.",
            "e. between the table and its preceding paragraph). Page breaks cannot be inserted inside a table, eq",
            "uation, footnote, header or footer. Since page breaks can only be inserted inside the body, the segm",
            "ent ID field must be empty.",
        ),
        default=None,
    )
    end_of_segment_location: Optional[EndOfSegmentLocation] = Field(
        description=(
            "Inserts the page break at the end of the document body. Page breaks cannot be inserted inside a foot",
            "note, header or footer. Since page breaks can only be inserted inside the body, the segment ID field",
            " must be empty.",
        ),
        default=None,
    )


class InsertSectionBreakRequest(str, Enum):
    """
    Inserts a section break at the given location.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#insertsectionbreakrequest
    """

    SECTION_TYPE = "section_type"  # The type of section to insert.
    LOCATION = "location"  # Inserts a newline and a section break at a specific index in the document. The section break must be inserted inside the bounds of an existing Paragraph. For instance, it cannot be inserted at a table's start index (i.e. between the table and its preceding paragraph). Section breaks cannot be inserted inside a table, equation, footnote, header, or footer. Since section breaks can only be inserted inside the body, the segment ID field must be empty.
    END_OF_SEGMENT_LOCATION = "end_of_segment_location"  # Inserts a newline and a section break at the end of the document body. Section breaks cannot be inserted inside a footnote, header or footer. Because section breaks can only be inserted inside the body, the segment ID field must be empty.


class InsertTableColumnRequest(BaseModel):
    """
    Inserts an empty column into a table.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#inserttablecolumnrequest
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    table_cell_location: Optional[TableCellLocation] = Field(
        description=(
            "The reference table cell location from which columns will be inserted. A new column will be inserted",
            " to the left (or right) of the column where the reference cell is. If the reference cell is a merged",
            " cell, a new column will be inserted to the left (or right) of the merged cell.",
        ),
        default=None,
    )
    insert_right: Optional[bool] = Field(
        description="Whether to insert new column to the right of the reference cell location.",
        default=None,
    )


class InsertTableRequest(BaseModel):
    """
    Inserts a table at the specified location.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#inserttablerequest
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    rows: Optional[int] = Field(
        description="The number of rows in the table.",
        default=None,
    )
    columns: Optional[int] = Field(
        description="The number of columns in the table.",
        default=None,
    )
    location: Optional[Location] = Field(
        description=(
            "Inserts the table at a specific model index. A newline character will be inserted before the inserte",
            "d table, therefore the table start index will be at the specified location index + 1. The table must",
            " be inserted inside the bounds of an existing Paragraph. For instance, it cannot be inserted at a ta",
            "ble's start index (i.e. between an existing table and its preceding paragraph). Tables cannot be ins",
            "erted inside a footnote or equation.",
        ),
        default=None,
    )
    end_of_segment_location: Optional[EndOfSegmentLocation] = Field(
        description=(
            "Inserts the table at the end of the given header, footer or document body. A newline character will ",
            "be inserted before the inserted table. Tables cannot be inserted inside a footnote.",
        ),
        default=None,
    )


class InsertTableRowRequest(BaseModel):
    """
    Inserts an empty row into a table.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#inserttablerowrequest
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    table_cell_location: Optional[TableCellLocation] = Field(
        description=(
            "The reference table cell location from which rows will be inserted. A new row will be inserted above",
            " (or below) the row where the reference cell is. If the reference cell is a merged cell, a new row w",
            "ill be inserted above (or below) the merged cell.",
        ),
        default=None,
    )
    insert_below: Optional[bool] = Field(
        description="Whether to insert new row below the reference cell location.",
        default=None,
    )


class InsertTextRequest(BaseModel):
    """
    Inserts text at the specified location.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#inserttextrequest
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    text: Optional[str] = Field(
        description=(
            "The text to be inserted. Inserting a newline character will implicitly create a new Paragraph at tha",
            "t index. The paragraph style of the new paragraph will be copied from the paragraph at the current i",
            "nsertion index, including lists and bullets. Text styles for inserted text will be determined automa",
            "tically, generally preserving the styling of neighboring text. In most cases, the text style for the",
            " inserted text will match the text immediately before the insertion index. Some control characters (",
            "U+0000-U+0008, U+000C-U+001F) and characters from the Unicode Basic Multilingual Plane Private Use A",
            "rea (U+E000-U+F8FF) will be stripped out of the inserted text.",
        ),
        default=None,
    )
    location: Optional[Location] = Field(
        description=(
            "Inserts the text at a specific index in the document. Text must be inserted inside the bounds of an ",
            "existing Paragraph. For instance, text cannot be inserted at a table's start index (i.e. between the",
            " table and its preceding paragraph). The text must be inserted in the preceding paragraph.",
        ),
        default=None,
    )
    end_of_segment_location: Optional[EndOfSegmentLocation] = Field(
        description="Inserts the text at the end of a header, footer, footnote or the document body.",
        default=None,
    )


class MergeTableCellsRequest(BaseModel):
    """
    Merges cells in a Table.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#mergetablecellsrequest
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    table_range: Optional[TableRange] = Field(
        description=(
            "The table range specifying which cells of the table to merge. Any text in the cells being merged wil",
            'l be concatenated and stored in the "head" cell of the range. This is the upper-left cell of the r',
            "ange when the content direction is left to right, and the upper-right cell of the range otherwise. I",
            "f the range is non-rectangular (which can occur in some cases where the range covers cells that are ",
            "already merged or where the table is non-rectangular), a 400 bad request error is returned.",
        ),
        default=None,
    )


class ReplaceAllTextRequest(BaseModel):
    """
    Replaces all instances of text matching a criteria with replace text.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#replacealltextrequest
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    replace_text: Optional[str] = Field(
        description="The text that will replace the matched text.",
        default=None,
    )
    tabs_criteria: Optional[TabsCriteria] = Field(
        description=(
            "Optional. The criteria used to specify in which tabs the replacement occurs. When omitted, the repla",
            "cement applies to all tabs. In a document containing a single tab: If provided, must match the singu",
            "lar tab's ID. If omitted, the replacement applies to the singular tab. In a document containing mult",
            "iple tabs: If provided, the replacement applies to the specified tabs. If omitted, the replacement a",
            "pplies to all tabs.",
        ),
        default=None,
    )
    contains_text: Optional[SubstringMatchCriteria] = Field(
        description="Finds text in the document matching this substring.",
        default=None,
    )


class ReplaceNamedRangeContentRequest(BaseModel):
    """
    Replaces the contents of the specified NamedRange or NamedRanges with the given replacement content.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#replacenamedrangecontentrequest
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    tabs_criteria: Optional[TabsCriteria] = Field(
        description=(
            "Optional. The criteria used to specify in which tabs the replacement occurs. When omitted, the repla",
            "cement applies to all tabs. In a document containing a single tab: If provided, must match the singu",
            "lar tab's ID. If omitted, the replacement applies to the singular tab. In a document containing mult",
            "iple tabs: If provided, the replacement applies to the specified tabs. If omitted, the replacement a",
            "pplies to all tabs.",
        ),
        default=None,
    )
    text: Optional[str] = Field(
        description="Replaces the content of the specified named range(s) with the given text.",
        default=None,
    )
    named_range_id: Optional[str] = Field(
        description=(
            "The ID of the named range whose content will be replaced. If there is no named range with the given ",
            "ID a 400 bad request error is returned.",
        ),
        default=None,
    )
    named_range_name: Optional[str] = Field(
        description=(
            "The name of the NamedRanges whose content will be replaced. If there are multiple named ranges with ",
            "the given name, then the content of each one will be replaced. If there are no named ranges with the",
            " given name, then the request will be a no-op.",
        ),
        default=None,
    )


class Request(BaseModel):
    """
    A single update to apply to a document.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#request
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    replace_all_text: Optional[ReplaceAllTextRequest] = Field(
        description="Replaces all instances of the specified text.",
        default=None,
    )
    insert_text: Optional[InsertTextRequest] = Field(
        description="Inserts text at the specified location.",
        default=None,
    )
    update_text_style: Optional[UpdateTextStyleRequest] = Field(
        description="Updates the text style at the specified range.",
        default=None,
    )
    create_paragraph_bullets: Optional[CreateParagraphBulletsRequest] = Field(
        description="Creates bullets for paragraphs.",
        default=None,
    )
    delete_paragraph_bullets: Optional[DeleteParagraphBulletsRequest] = Field(
        description="Deletes bullets from paragraphs.",
        default=None,
    )
    create_named_range: Optional[CreateNamedRangeRequest] = Field(
        description="Creates a named range.",
        default=None,
    )
    delete_named_range: Optional[DeleteNamedRangeRequest] = Field(
        description="Deletes a named range.",
        default=None,
    )
    update_paragraph_style: Optional[UpdateParagraphStyleRequest] = Field(
        description="Updates the paragraph style at the specified range.",
        default=None,
    )
    delete_content_range: Optional[DeleteContentRangeRequest] = Field(
        description="Deletes content from the document.",
        default=None,
    )
    insert_inline_image: Optional[InsertInlineImageRequest] = Field(
        description="Inserts an inline image at the specified location.",
        default=None,
    )
    insert_table: Optional[InsertTableRequest] = Field(
        description="Inserts a table at the specified location.",
        default=None,
    )
    insert_table_row: Optional[InsertTableRowRequest] = Field(
        description="Inserts an empty row into a table.",
        default=None,
    )
    insert_table_column: Optional[InsertTableColumnRequest] = Field(
        description="Inserts an empty column into a table.",
        default=None,
    )
    delete_table_row: Optional[DeleteTableRowRequest] = Field(
        description="Deletes a row from a table.",
        default=None,
    )
    delete_table_column: Optional[DeleteTableColumnRequest] = Field(
        description="Deletes a column from a table.",
        default=None,
    )
    insert_page_break: Optional[InsertPageBreakRequest] = Field(
        description="Inserts a page break at the specified location.",
        default=None,
    )
    delete_positioned_object: Optional[DeletePositionedObjectRequest] = Field(
        description="Deletes a positioned object from the document.",
        default=None,
    )
    update_table_column_properties: Optional[UpdateTableColumnPropertiesRequest] = (
        Field(
            description="Updates the properties of columns in a table.",
            default=None,
        )
    )
    update_table_cell_style: Optional[UpdateTableCellStyleRequest] = Field(
        description="Updates the style of table cells.",
        default=None,
    )
    update_table_row_style: Optional[UpdateTableRowStyleRequest] = Field(
        description="Updates the row style in a table.",
        default=None,
    )
    replace_image: Optional[ReplaceImageRequest] = Field(
        description="Replaces an image in the document.",
        default=None,
    )
    update_document_style: Optional[UpdateDocumentStyleRequest] = Field(
        description="Updates the style of the document.",
        default=None,
    )
    merge_table_cells: Optional[MergeTableCellsRequest] = Field(
        description="Merges cells in a table.",
        default=None,
    )
    unmerge_table_cells: Optional[UnmergeTableCellsRequest] = Field(
        description="Unmerges cells in a table.",
        default=None,
    )
    create_header: Optional[CreateHeaderRequest] = Field(
        description="Creates a header.",
        default=None,
    )
    create_footer: Optional[CreateFooterRequest] = Field(
        description="Creates a footer.",
        default=None,
    )
    create_footnote: Optional[CreateFootnoteRequest] = Field(
        description="Creates a footnote.",
        default=None,
    )
    replace_named_range_content: Optional[ReplaceNamedRangeContentRequest] = Field(
        description="Replaces the content in a named range.",
        default=None,
    )
    update_section_style: Optional[UpdateSectionStyleRequest] = Field(
        description="Updates the section style of the specified range.",
        default=None,
    )
    insert_section_break: Optional[InsertSectionBreakRequest] = Field(
        description="Inserts a section break at the specified location.",
        default=None,
    )
    delete_header: Optional[DeleteHeaderRequest] = Field(
        description="Deletes a header from the document.",
        default=None,
    )
    delete_footer: Optional[DeleteFooterRequest] = Field(
        description="Deletes a footer from the document.",
        default=None,
    )
    pin_table_header_rows: Optional[PinTableHeaderRowsRequest] = Field(
        description="Updates the number of pinned header rows in a table.",
        default=None,
    )
