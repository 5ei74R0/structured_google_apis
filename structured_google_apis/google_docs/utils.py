from pydantic import BaseModel


def get_fields(basemodel: BaseModel) -> str:
    """
    Get the fields of a Pydantic model as a list of tuples.

    Args:
        basemodel (BaseModel): The Pydantic model to get fields from.

    Returns:
        str: A list of field names separated by commas.
    """
    return ", ".join([name for name, _ in basemodel.__annotations__.items()])
