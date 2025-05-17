from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, alias_generators


class CreateFooterResponse(BaseModel):
    """
    The result of creating a footer.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#createfooterresponse
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    footer_id: Optional[str] = Field(
        description="The ID of the created footer.",
        default=None,
    )


class CreateFootnoteResponse(BaseModel):
    """
    The result of creating a footnote.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#createfootnoteresponse
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    footnote_id: Optional[str] = Field(
        description="The ID of the created footnote.",
        default=None,
    )


class CreateHeaderResponse(BaseModel):
    """
    The result of creating a header.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#createheaderresponse
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    header_id: Optional[str] = Field(
        description="The ID of the created header.",
        default=None,
    )


class CreateNamedRangeResponse(BaseModel):
    """
    The result of creating a named range.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#createnamedrangeresponse
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    named_range_id: Optional[str] = Field(
        description="The ID of the created named range.",
        default=None,
    )


class InsertInlineImageResponse(BaseModel):
    """
    The result of inserting an inline image.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#insertinlineimageresponse
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    object_id: Optional[str] = Field(
        description="The ID of the created InlineObject.",
        default=None,
    )


class InsertInlineSheetsChartResponse(BaseModel):
    """
    The result of inserting an embedded Google Sheets chart.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#insertinlinesheetschartresponse
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    object_id: Optional[str] = Field(
        description="The object ID of the inserted chart.",
        default=None,
    )


class ReplaceAllTextResponse(BaseModel):
    """
    The result of replacing text.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#replacealltextresponse
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    occurrences_changed: Optional[int] = Field(
        description="The number of occurrences changed by replacing all text.",
        default=None,
    )


class Response(BaseModel):
    """
    A single response from an update.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#response
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    replace_all_text: Optional[ReplaceAllTextResponse] = Field(
        description="The result of replacing text.",
        default=None,
    )
    create_named_range: Optional[CreateNamedRangeResponse] = Field(
        description="The result of creating a named range.",
        default=None,
    )
    insert_inline_image: Optional[InsertInlineImageResponse] = Field(
        description="The result of inserting an inline image.",
        default=None,
    )
    insert_inline_sheets_chart: Optional[InsertInlineSheetsChartResponse] = Field(
        description="The result of inserting an inline Google Sheets chart.",
        default=None,
    )
    create_header: Optional[CreateHeaderResponse] = Field(
        description="The result of creating a header.",
        default=None,
    )
    create_footer: Optional[CreateFooterResponse] = Field(
        description="The result of creating a footer.",
        default=None,
    )
    create_footnote: Optional[CreateFootnoteResponse] = Field(
        description="The result of creating a footnote.",
        default=None,
    )
