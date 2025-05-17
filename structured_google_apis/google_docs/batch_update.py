from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, alias_generators


class WriteControl(BaseModel):
    """
    Provides control over how write requests are executed.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#writecontrol
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    required_revision_id: Optional[str] = Field(
        description=(
            "The optional revision ID of the document the write request is applied to. If this is not the latest "
            "revision of the document, the request is not processed and returns a 400 bad request error. When a r"
            "equired revision ID is returned in a response, it indicates the revision ID of the document after th"
            "e request was applied."
        )
    )
    target_revision_id: Optional[str] = Field(
        description=(
            "The optional target revision ID of the document the write request is applied to. If collaborator cha"
            "nges have occurred after the document was read using the API, the changes produced by this write req"
            "uest are applied against the collaborator changes. This results in a new revision of the document th"
            "at incorporates both the collaborator changes and the changes in the request, with the Docs server r"
            "esolving conflicting changes. When using target revision ID, the API client can be thought of as ano"
            "ther collaborator of the document. The target revision ID can only be used to write to recent versio"
            "ns of a document. If the target revision is too far behind the latest revision, the request is not p"
            "rocessed and returns a 400 bad request error. The request should be tried again after retrieving the"
            " latest version of the document. Usually a revision ID remains valid for use as a target revision fo"
            "r several minutes after it's read, but for frequently edited documents this window might be shorter."
        )
    )
