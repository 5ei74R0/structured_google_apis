from pydantic import BaseModel


def get_fields(basemodel: BaseModel) -> str:
    """
    Get the fields of a Pydantic model as a list of tuples.

    Args:
        basemodel (BaseModel): The Pydantic model to get fields from.

    Returns:
        str: A list of used field names separated by commas.
    """
    fields = [field for field in get_dict_request(basemodel).keys()]
    if len(fields) == 0:
        return "*"
    return ",".join(fields)


def get_dict_request(basemodel: BaseModel) -> dict:
    """
    Get the dictionary representation of a Pydantic model.

    Args:
        basemodel (BaseModel): The Pydantic model to get the dictionary from.

    Returns:
        dict: A dictionary representation of the Pydantic model.
    """
    return basemodel.model_dump(by_alias=True, exclude_defaults=True)


def get_dict_batch_request(basemodels: list[BaseModel]) -> list[dict]:
    """
    Get the dictionary representation of a Pydantic model for batch requests.

    Args:
        basemodels (list[BaseModel]): The Pydantic model to get the dictionary from.

    Returns:
        dict: A dictionary representation of the Pydantic model for batch requests.
    """
    result = []
    for basemodel in basemodels:
        result.append(get_dict_request(basemodel))
    return result
