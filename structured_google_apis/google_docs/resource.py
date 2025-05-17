from __future__ import annotations

from enum import Enum
from typing import Any, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, alias_generators


class GlyphType(str, Enum):
    """
    The types of glyphs used by bullets when paragraphs at this level of nesting is ordered.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#glyphtype

    GLYPH_TYPE_UNSPECIFIED: The glyph type is unspecified or unsupported.

    NONE: An empty string.

    DECIMAL: A number, like 1, 2, or 3.

    ZERO_DECIMAL: A number where single digit numbers are prefixed with a zero, like 01, 02, or 03. Numbers with more than one digit are not prefixed with a zero.

    UPPER_ALPHA: An uppercase letter, like A, B, or C.

    ALPHA: A lowercase letter, like a, b, or c.

    UPPER_ROMAN: An uppercase Roman numeral, like I, II, or III.

    ROMAN: A lowercase Roman numeral, like i, ii, or iii.
    """

    GLYPH_TYPE_UNSPECIFIED = "GLYPH_TYPE_UNSPECIFIED"
    NONE = "NONE"
    DECIMAL = "DECIMAL"
    ZERO_DECIMAL = "ZERO_DECIMAL"
    UPPER_ALPHA = "UPPER_ALPHA"
    ALPHA = "ALPHA"
    UPPER_ROMAN = "UPPER_ROMAN"
    ROMAN = "ROMAN"


class NamedStyleType(str, Enum):
    """
    The types of named styles.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#namedstyletype

    NAMED_STYLE_TYPE_UNSPECIFIED: The type of named style is unspecified.

    NORMAL_TEXT: Normal text.

    TITLE: Title.

    SUBTITLE: Subtitle.

    HEADING_1: Heading 1.

    HEADING_2: Heading 2.

    HEADING_3: Heading 3.

    HEADING_4: Heading 4.

    HEADING_5: Heading 5.

    HEADING_6: Heading 6.
    """

    NAMED_STYLE_TYPE_UNSPECIFIED = "NAMED_STYLE_TYPE_UNSPECIFIED"
    NORMAL_TEXT = "NORMAL_TEXT"
    TITLE = "TITLE"
    SUBTITLE = "SUBTITLE"
    HEADING_1 = "HEADING_1"
    HEADING_2 = "HEADING_2"
    HEADING_3 = "HEADING_3"
    HEADING_4 = "HEADING_4"
    HEADING_5 = "HEADING_5"
    HEADING_6 = "HEADING_6"


class SectionType(str, Enum):
    """
    Represents how the start of the current section is positioned relative to the previous section.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#sectiontype

    SECTION_TYPE_UNSPECIFIED: The section type is unspecified.

    CONTINUOUS: The section starts immediately after the last paragraph of the previous section.

    NEXT_PAGE: The section starts on the next page.
    """

    SECTION_TYPE_UNSPECIFIED = "SECTION_TYPE_UNSPECIFIED"
    CONTINUOUS = "CONTINUOUS"
    NEXT_PAGE = "NEXT_PAGE"


class Type(str, Enum):
    """
    The types of auto text.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#type

    TYPE_UNSPECIFIED: An unspecified auto text type.

    PAGE_NUMBER: Type for auto text that represents the current page number.

    PAGE_COUNT: Type for auto text that represents the total number of pages in the document.
    """

    TYPE_UNSPECIFIED = "TYPE_UNSPECIFIED"
    PAGE_NUMBER = "PAGE_NUMBER"
    PAGE_COUNT = "PAGE_COUNT"


class WidthType(str, Enum):
    """
    The type of width of the column.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#widthtype

    WIDTH_TYPE_UNSPECIFIED: The column width type is unspecified.

    EVENLY_DISTRIBUTED: The column width is evenly distributed among the other evenly distributed columns.
    The width of the column is automatically determined and will have an equal portion of
                                    the width remaining for the table after accounting for all columns with specified
                                    widths.

    FIXED_WIDTH: A fixed column width. The [width][google.apps.docs.v1.TableColumnProperties.width
                                  property contains the column's width.
    """

    WIDTH_TYPE_UNSPECIFIED = "WIDTH_TYPE_UNSPECIFIED"
    EVENLY_DISTRIBUTED = "EVENLY_DISTRIBUTED"
    FIXED_WIDTH = "FIXED_WIDTH"


class Alignment(str, Enum):
    """
    The types of text alignment for a paragraph.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#alignment

    ALIGNMENT_UNSPECIFIED: The paragraph alignment is inherited from the parent.

    START: The paragraph is aligned to the start of the line. Left-aligned for LTR text,
                                  right-aligned otherwise.

    CENTER: The paragraph is centered.

    END: The paragraph is aligned to the end of the line. Right-aligned for LTR text,
                                  left-aligned otherwise.

    JUSTIFIED: The paragraph is justified.
    """

    ALIGNMENT_UNSPECIFIED = "ALIGNMENT_UNSPECIFIED"
    START = "START"
    CENTER = "CENTER"
    END = "END"
    JUSTIFIED = "JUSTIFIED"


class BackgroundSuggestionState(BaseModel):
    """
    A mask that indicates which of the fields on the base Background have been changed in this suggestion. For any field set to true, the Backgound has a new suggested value.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#backgroundsuggestionstate
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    background_color_suggested: Optional[bool] = Field(
        description="Indicates whether the current background color has been modified in this suggestion.",
        default=None,
    )


class BaselineOffset(str, Enum):
    """
    The ways in which text can be vertically offset from its normal position.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#baselineoffset

    BASELINE_OFFSET_UNSPECIFIED: The text's baseline offset is inherited from the parent.

    NONE: The text is not vertically offset.

    SUPERSCRIPT: The text is vertically offset upwards (superscript).

    SUBSCRIPT: The text is vertically offset downwards (subscript).
    """

    BASELINE_OFFSET_UNSPECIFIED = "BASELINE_OFFSET_UNSPECIFIED"
    NONE = "NONE"
    SUPERSCRIPT = "SUPERSCRIPT"
    SUBSCRIPT = "SUBSCRIPT"


class BookmarkLink(BaseModel):
    """
    A reference to a bookmark in this document.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#bookmarklink
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    id: Optional[str] = Field(
        description="The ID of a bookmark in this document.",
        default=None,
    )
    tab_id: Optional[str] = Field(
        description="The ID of the tab containing this bookmark.",
        default=None,
    )


class BulletAlignment(str, Enum):
    """
    The types of alignment for a bullet.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#bulletalignment

    BULLET_ALIGNMENT_UNSPECIFIED: The bullet alignment is unspecified.

    START: The bullet is aligned to the start of the space allotted for rendering the bullet.
                                  Left-aligned for LTR text, right-aligned otherwise.

    CENTER: The bullet is aligned to the center of the space allotted for rendering the bullet.

    END: The bullet is aligned to the end of the space allotted for rendering the bullet.
                                  Right-aligned for LTR text, left-aligned otherwise.
    """

    BULLET_ALIGNMENT_UNSPECIFIED = "BULLET_ALIGNMENT_UNSPECIFIED"
    START = "START"
    CENTER = "CENTER"
    END = "END"


class ColumnSeparatorStyle(str, Enum):
    """
    The style of column separators between columns.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#columnseparatorstyle

    COLUMN_SEPARATOR_STYLE_UNSPECIFIED: An unspecified column separator style.

    NONE: No column separator lines between columns.

    BETWEEN_EACH_COLUMN: Renders a column separator line between each column.
    """

    COLUMN_SEPARATOR_STYLE_UNSPECIFIED = "COLUMN_SEPARATOR_STYLE_UNSPECIFIED"
    NONE = "NONE"
    BETWEEN_EACH_COLUMN = "BETWEEN_EACH_COLUMN"


class ContentAlignment(str, Enum):
    """
    The types of content alignment.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#contentalignment

    CONTENT_ALIGNMENT_UNSPECIFIED: An unspecified content alignment. The content alignment is inherited from the parent if
                                  one exists.

    CONTENT_ALIGNMENT_UNSUPPORTED: An unsupported content alignment.

    TOP: An alignment that aligns the content to the top of the content holder. Corresponds to
                                  ECMA-376 ST_TextAnchoringType 't'.

    MIDDLE: An alignment that aligns the content to the middle of the content holder. Corresponds to
                                  ECMA-376 ST_TextAnchoringType 'ctr'.

    BOTTOM: An alignment that aligns the content to the bottom of the content holder. Corresponds to
                                  ECMA-376 ST_TextAnchoringType 'b'.
    """

    CONTENT_ALIGNMENT_UNSPECIFIED = "CONTENT_ALIGNMENT_UNSPECIFIED"
    CONTENT_ALIGNMENT_UNSUPPORTED = "CONTENT_ALIGNMENT_UNSUPPORTED"
    TOP = "TOP"
    MIDDLE = "MIDDLE"
    BOTTOM = "BOTTOM"


class ContentDirection(str, Enum):
    """
    The directions content can flow in.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#contentdirection

    CONTENT_DIRECTION_UNSPECIFIED: The content direction is unspecified.

    LEFT_TO_RIGHT: The content goes from left to right.

    RIGHT_TO_LEFT: The content goes from right to left.
    """

    CONTENT_DIRECTION_UNSPECIFIED = "CONTENT_DIRECTION_UNSPECIFIED"
    LEFT_TO_RIGHT = "LEFT_TO_RIGHT"
    RIGHT_TO_LEFT = "RIGHT_TO_LEFT"


class CropProperties(BaseModel):
    """
    The crop properties of an image.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#cropproperties
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    offset_left: Optional[float] = Field(
        description=(
            "The offset specifies how far inwards the left edge of the crop rectangle is from the left edge of th",
            "e original content as a fraction of the original content's width.",
        ),
        default=None,
    )
    offset_right: Optional[float] = Field(
        description=(
            "The offset specifies how far inwards the right edge of the crop rectangle is from the right edge of ",
            "the original content as a fraction of the original content's width.",
        ),
        default=None,
    )
    offset_top: Optional[float] = Field(
        description=(
            "The offset specifies how far inwards the top edge of the crop rectangle is from the top edge of the ",
            "original content as a fraction of the original content's height.",
        ),
        default=None,
    )
    offset_bottom: Optional[float] = Field(
        description=(
            "The offset specifies how far inwards the bottom edge of the crop rectangle is from the bottom edge o",
            "f the original content as a fraction of the original content's height.",
        ),
        default=None,
    )
    angle: Optional[float] = Field(
        description=(
            "The clockwise rotation angle of the crop rectangle around its center, in radians. Rotation is applie",
            "d after the offsets.",
        ),
        default=None,
    )


class CropPropertiesSuggestionState(BaseModel):
    """
    A mask that indicates which of the fields on the base CropProperties have been changed in this suggestion. For any field set to true, there's a new suggested value.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#croppropertiessuggestionstate
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    offset_left_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to offsetLeft.",
        default=None,
    )
    offset_right_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to offsetRight.",
        default=None,
    )
    offset_top_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to offsetTop.",
        default=None,
    )
    offset_bottom_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to offsetBottom.",
        default=None,
    )
    angle_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to angle.",
        default=None,
    )


class DashStyle(str, Enum):
    """
    The kinds of dashes with which linear geometry can be rendered. These values are based on the "ST_PresetLineDashVal" simple type described in section 20.1.10.49 of "Office Open XML File Formats - Fundamentals and Markup Language Reference", part 1 of ECMA-376 5th edition.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#dashstyle

    DASH_STYLE_UNSPECIFIED: Unspecified dash style.

    SOLID: Solid line. Corresponds to ECMA-376 ST_PresetLineDashVal value 'solid'. This is the
                                  default dash style.

    DOT: Dotted line. Corresponds to ECMA-376 ST_PresetLineDashVal value 'dot'.

    DASH: Dashed line. Corresponds to ECMA-376 ST_PresetLineDashVal value 'dash'.
    """

    DASH_STYLE_UNSPECIFIED = "DASH_STYLE_UNSPECIFIED"
    SOLID = "SOLID"
    DOT = "DOT"
    DASH = "DASH"


class EmbeddedDrawingProperties(BaseModel):
    """
    The properties of an embedded drawing and used to differentiate the object type. An embedded drawing is one that's created and edited within a document. Note that extensive details are not supported.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#embeddeddrawingproperties
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    pass


class EmbeddedDrawingPropertiesSuggestionState(BaseModel):
    """
    A mask that indicates which of the fields on the base EmbeddedDrawingProperties have been changed in this suggestion. For any field set to true, there's a new suggested value.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#embeddeddrawingpropertiessuggestionstate
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    pass


class EmbeddedObjectBorderSuggestionState(BaseModel):
    """
    A mask that indicates which of the fields on the base EmbeddedObjectBorder have been changed in this suggestion. For any field set to true, there's a new suggested value.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#embeddedobjectbordersuggestionstate
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    color_suggested: Optional[bool] = Field(
        description=(
            "Indicates if there was a suggested change to [color] [google.apps.docs.v1.EmbeddedBorderObject.color",
            "].",
        ),
        default=None,
    )
    width_suggested: Optional[bool] = Field(
        description=(
            "Indicates if there was a suggested change to [width] [google.apps.docs.v1.EmbeddedBorderObject.width",
            "].",
        ),
        default=None,
    )
    dash_style_suggested: Optional[bool] = Field(
        description=(
            "Indicates if there was a suggested change to [dashStyle] [google.apps.docs.v1.EmbeddedBorderObject.d",
            "ash_style].",
        ),
        default=None,
    )
    property_state_suggested: Optional[bool] = Field(
        description=(
            "Indicates if there was a suggested change to [propertyState] [google.apps.docs.v1.EmbeddedBorderObje",
            "ct.property_state].",
        ),
        default=None,
    )


class Equation(BaseModel):
    """
    A ParagraphElement representing an equation.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#equation
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    suggested_insertion_ids: Optional[list[str]] = Field(
        description=(
            "The suggested insertion IDs. An Equation may have multiple insertion IDs if it's a nested suggested ",
            "change. If empty, then this is not a suggested insertion.",
        ),
        default=None,
    )
    suggested_deletion_ids: Optional[str] = Field(
        description="The suggested deletion IDs. If empty, then there are no suggested deletions of this content.",
        default=None,
    )


class HeadingLink(BaseModel):
    """
    A reference to a heading in this document.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#headinglink
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    id: Optional[str] = Field(
        description="The ID of a heading in this document.",
        default=None,
    )
    tab_id: Optional[str] = Field(
        description="The ID of the tab containing this heading.",
        default=None,
    )


class ImageProperties(BaseModel):
    """
    The properties of an image.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#imageproperties
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    content_uri: Optional[str] = Field(
        description=(
            "A URI to the image with a default lifetime of 30 minutes. This URI is tagged with the account of the",
            " requester. Anyone with the URI effectively accesses the image as the original requester. Access to ",
            "the image may be lost if the document's sharing settings change.",
        ),
        default=None,
    )
    source_uri: Optional[str] = Field(
        description="The source URI is the URI used to insert the image. The source URI can be empty.",
        default=None,
    )
    brightness: Optional[float] = Field(
        description=(
            "The brightness effect of the image. The value should be in the interval [-1.0, 1.0], where 0 means n",
            "o effect.",
        ),
        default=None,
    )
    contrast: Optional[float] = Field(
        description=(
            "The contrast effect of the image. The value should be in the interval [-1.0, 1.0], where 0 means no ",
            "effect.",
        ),
        default=None,
    )
    transparency: Optional[float] = Field(
        description=(
            "The transparency effect of the image. The value should be in the interval [0.0, 1.0], where 0 means ",
            "no effect and 1 means transparent.",
        ),
        default=None,
    )
    crop_properties: Optional[CropProperties] = Field(
        description="The crop properties of the image.",
        default=None,
    )
    angle: Optional[float] = Field(
        description="The clockwise rotation angle of the image, in radians.",
        default=None,
    )


class ImagePropertiesSuggestionState(BaseModel):
    """
    A mask that indicates which of the fields on the base ImageProperties have been changed in this suggestion. For any field set to true, there's a new suggested value.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#imagepropertiessuggestionstate
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    content_uri_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to contentUri.",
        default=None,
    )
    source_uri_suggested: Optional[bool] = Field(
        description=(
            "Indicates if there was a suggested change to [sourceUri] [google.apps.docs.v1.EmbeddedObject.source_",
            "uri].",
        ),
        default=None,
    )
    brightness_suggested: Optional[bool] = Field(
        description=(
            "Indicates if there was a suggested change to [brightness] [google.apps.docs.v1.EmbeddedObject.bright",
            "ness].",
        ),
        default=None,
    )
    contrast_suggested: Optional[bool] = Field(
        description=(
            "Indicates if there was a suggested change to [contrast] [google.apps.docs.v1.EmbeddedObject.contrast",
            "].",
        ),
        default=None,
    )
    transparency_suggested: Optional[bool] = Field(
        description=(
            "Indicates if there was a suggested change to [transparency] [google.apps.docs.v1.EmbeddedObject.tran",
            "sparency].",
        ),
        default=None,
    )
    crop_properties_suggestion_state: Optional[CropPropertiesSuggestionState] = Field(
        description="A mask that indicates which of the fields in cropProperties have been changed in this suggestion.",
        default=None,
    )
    angle_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to [angle] [google.apps.docs.v1.EmbeddedObject.angle].",
        default=None,
    )


class Link(BaseModel):
    """
    A reference to another portion of a document or an external URL resource.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#link
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    url: Optional[str] = Field(
        description="An external URL.",
        default=None,
    )
    tab_id: Optional[str] = Field(
        description="The ID of a tab in this document.",
        default=None,
    )
    bookmark: Optional[BookmarkLink] = Field(
        description=(
            "A bookmark in this document. In documents containing a single tab, links to bookmarks within the sin",
            "gular tab continue to return Link.bookmarkId when the includeTabsContent parameter is set to false o",
            "r unset. Otherwise, this field is returned.",
        ),
        default=None,
    )
    heading: Optional[HeadingLink] = Field(
        description=(
            "A heading in this document. In documents containing a single tab, links to headings within the singu",
            "lar tab continue to return Link.headingId when the includeTabsContent parameter is set to false or u",
            "nset. Otherwise, this field is returned.",
        ),
        default=None,
    )
    bookmark_id: Optional[str] = Field(
        description=(
            "The ID of a bookmark in this document. Legacy field: Instead, set includeTabsContent to true and use",
            " Link.bookmark for read and write operations. This field is only returned when includeTabsContent is",
            " set to false in documents containing a single tab and links to a bookmark within the singular tab. ",
            "Otherwise, Link.bookmark is returned. If this field is used in a write request, the bookmark is cons",
            "idered to be from the tab ID specified in the request. If a tab ID is not specified in the request, ",
            "it is considered to be from the first tab in the document.",
        ),
        default=None,
    )
    heading_id: Optional[str] = Field(
        description=(
            "The ID of a heading in this document. Legacy field: Instead, set includeTabsContent to true and use ",
            "Link.heading for read and write operations. This field is only returned when includeTabsContent is s",
            "et to false in documents containing a single tab and links to a heading within the singular tab. Oth",
            "erwise, Link.heading is returned. If this field is used in a write request, the heading is considere",
            "d to be from the tab ID specified in the request. If a tab ID is not specified in the request, it is",
            " considered to be from the first tab in the document.",
        ),
        default=None,
    )


class METHODS_SUMMARY(BaseModel):
    """

    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#methods
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    pass


class ObjectReferences(BaseModel):
    """
    A collection of object IDs.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#objectreferences
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    object_ids: Optional[list[str]] = Field(
        description="The object IDs.",
        default=None,
    )


class PersonProperties(BaseModel):
    """
    Properties specific to a linked Person.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#personproperties
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    name: Optional[str] = Field(
        description=(
            "Output only. The name of the person if it's displayed in the link text instead of the person's email",
            " address.",
        ),
        default=None,
    )
    email: Optional[str] = Field(
        description="Output only. The email address linked to this Person. This field is always present.",
        default=None,
    )


class PositionedObjectLayout(str, Enum):
    """
    The possible layouts of a [PositionedObject][google.aps.docs.v1.PositionedObject].
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#positionedobjectlayout

    POSITIONED_OBJECT_LAYOUT_UNSPECIFIED: The layout is unspecified.

    WRAP_TEXT: The text wraps around the positioned object.

    BREAK_LEFT: Breaks text such that the positioned object is on the left and text is on the right.

    BREAK_RIGHT: Breaks text such that the positioned object is on the right and text is on the left.

    BREAK_LEFT_RIGHT: Breaks text such that there's no text on the left or right of the positioned object.

    IN_FRONT_OF_TEXT: The positioned object is in front of the text.

    BEHIND_TEXT: The positioned object is behind the text.
    """

    POSITIONED_OBJECT_LAYOUT_UNSPECIFIED = "POSITIONED_OBJECT_LAYOUT_UNSPECIFIED"
    WRAP_TEXT = "WRAP_TEXT"
    BREAK_LEFT = "BREAK_LEFT"
    BREAK_RIGHT = "BREAK_RIGHT"
    BREAK_LEFT_RIGHT = "BREAK_LEFT_RIGHT"
    IN_FRONT_OF_TEXT = "IN_FRONT_OF_TEXT"
    BEHIND_TEXT = "BEHIND_TEXT"


class PositionedObjectPositioningSuggestionState(BaseModel):
    """
    A mask that indicates which of the fields on the base PositionedObjectPositioning have been changed in this suggestion. For any field set to true, there's a new suggested value.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#positionedobjectpositioningsuggestionstate
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    layout_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to layout.",
        default=None,
    )
    left_offset_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to leftOffset.",
        default=None,
    )
    top_offset_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to topOffset.",
        default=None,
    )


class PropertyState(str, Enum):
    """
    The possible states of a property.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#propertystate

    RENDERED: If a property's state is RENDERED, then the element has the corresponding property when
                                  rendered in the document. This is the default value.

    NOT_RENDERED: If a property's state is NOT_RENDERED, then the element does not have the corresponding
                                  property when rendered in the document.
    """

    RENDERED = "RENDERED"
    NOT_RENDERED = "NOT_RENDERED"


class Range(BaseModel):
    """
    Specifies a contiguous range of text.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#range
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    segment_id: Optional[str] = Field(
        description=(
            "The ID of the header, footer, or footnote that this range is contained in. An empty segment ID signi",
            "fies the document's body.",
        ),
        default=None,
    )
    start_index: Optional[int] = Field(
        description=(
            "The zero-based start index of this range, in UTF-16 code units. In all current uses, a start index m",
            "ust be provided. This field is an Int32Value in order to accommodate future use cases with open-ende",
            "d ranges.",
        ),
        default=None,
    )
    end_index: Optional[int] = Field(
        description=(
            "The zero-based end index of this range, exclusive, in UTF-16 code units. In all current uses, an end",
            " index must be provided. This field is an Int32Value in order to accommodate future use cases with o",
            "pen-ended ranges.",
        ),
        default=None,
    )
    tab_id: Optional[str] = Field(
        description=(
            "The tab that contains this range. When omitted, the request applies to the first tab. In a document ",
            "containing a single tab: If provided, must match the singular tab's ID. If omitted, the request appl",
            "ies to the singular tab. In a document containing multiple tabs: If provided, the request applies to",
            " the specified tab. If omitted, the request applies to the first tab in the document.",
        ),
        default=None,
    )


class RgbColor(BaseModel):
    """
    An RGB color.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#rgbcolor
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    red: Optional[float] = Field(
        description="The red component of the color, from 0.0 to 1.0.",
        default=None,
    )
    green: Optional[float] = Field(
        description="The green component of the color, from 0.0 to 1.0.",
        default=None,
    )
    blue: Optional[float] = Field(
        description="The blue component of the color, from 0.0 to 1.0.",
        default=None,
    )


class RichLinkProperties(BaseModel):
    """
    Properties specific to a RichLink.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#richlinkproperties
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    title: Optional[str] = Field(
        description=(
            "Output only. The title of the RichLink as displayed in the link. This title matches the title of the",
            " linked resource at the time of the insertion or last update of the link. This field is always prese",
            "nt.",
        ),
        default=None,
    )
    uri: Optional[str] = Field(
        description="Output only. The URI to the RichLink. This is always present.",
        default=None,
    )
    mime_type: Optional[str] = Field(
        description="Output only. The MIME type of the RichLink, if there's one (for example, when it's a file in Drive).",
        default=None,
    )


class ShadingSuggestionState(BaseModel):
    """
    A mask that indicates which of the fields on the base Shading have been changed in this suggested change. For any field set to true, there's a new suggested value.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#shadingsuggestionstate
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    background_color_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to the Shading.",
        default=None,
    )


class SheetsChartReference(BaseModel):
    """
    A reference to a linked chart embedded from Google Sheets.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#sheetschartreference
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    spreadsheet_id: Optional[str] = Field(
        description="The ID of the Google Sheets spreadsheet that contains the source chart.",
        default=None,
    )
    chart_id: Optional[int] = Field(
        description="The ID of the specific chart in the Google Sheets spreadsheet that's embedded.",
        default=None,
    )


class SheetsChartReferenceSuggestionState(BaseModel):
    """
    A mask that indicates which of the fields on the base SheetsChartReference have been changed in this suggestion. For any field set to true, there's a new suggested value.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#sheetschartreferencesuggestionstate
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    spreadsheet_id_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to spreadsheetId.",
        default=None,
    )
    chart_id_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to chartId.",
        default=None,
    )


class SizeSuggestionState(BaseModel):
    """
    A mask that indicates which of the fields on the base Size have been changed in this suggestion. For any field set to true, the Size has a new suggested value.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#sizesuggestionstate
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    height_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to height.",
        default=None,
    )
    width_suggested: Optional[list[bool]] = Field(
        description="Indicates if there was a suggested change to width.",
        default=None,
    )


class SpacingMode(str, Enum):
    """
    The different modes for paragraph spacing.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#spacingmode

    SPACING_MODE_UNSPECIFIED: The spacing mode is inherited from the parent.

    NEVER_COLLAPSE: Paragraph spacing is always rendered.

    COLLAPSE_LISTS: Paragraph spacing is skipped between list elements.
    """

    SPACING_MODE_UNSPECIFIED = "SPACING_MODE_UNSPECIFIED"
    NEVER_COLLAPSE = "NEVER_COLLAPSE"
    COLLAPSE_LISTS = "COLLAPSE_LISTS"


class SuggestionsViewMode(str, Enum):
    """
    The suggestions view mode applied to the document that indicates how suggested changes are represented. It provides options for reading the document with all suggestions inline, accepted, or rejected.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#suggestionsviewmode

    DEFAULT_FOR_CURRENT_ACCESS: The SuggestionsViewMode applied to the returned document depends on the user's current
                                  access level. If the user only has view access, PREVIEW_WITHOUT_SUGGESTIONS
                                  is applied. Otherwise, SUGGESTIONS_INLINE
                                  is applied. This is the default suggestions view mode.

    SUGGESTIONS_INLINE: The returned document has suggestions inline. Suggested changes will be differentiated
                                    from base content within the document.
    Requests to retrieve a document using this mode will return a 403 error if the user
                                    does not have permission to view suggested changes.

    PREVIEW_SUGGESTIONS_ACCEPTED: The returned document is a preview with all suggested changes accepted.
    Requests to retrieve a document using this mode will return a 403 error if the user
                                    does not have permission to view suggested changes.

    PREVIEW_WITHOUT_SUGGESTIONS: The returned document is a preview with all suggested changes rejected if there are any
                                  suggestions in the document.
    """

    DEFAULT_FOR_CURRENT_ACCESS = "DEFAULT_FOR_CURRENT_ACCESS"
    SUGGESTIONS_INLINE = "SUGGESTIONS_INLINE"
    PREVIEW_SUGGESTIONS_ACCEPTED = "PREVIEW_SUGGESTIONS_ACCEPTED"
    PREVIEW_WITHOUT_SUGGESTIONS = "PREVIEW_WITHOUT_SUGGESTIONS"


class TabProperties(BaseModel):
    """
    Properties of a tab.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#tabproperties
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    tab_id: Optional[str] = Field(
        description="Output only. The ID of the tab. This field can't be changed.",
        default=None,
    )
    title: Optional[str] = Field(
        description="The user-visible name of the tab.",
        default=None,
    )
    parent_tab_id: Optional[str] = Field(
        description=(
            "Optional. The ID of the parent tab. Empty when the current tab is a root-level tab, which means it d",
            "oesn't have any parents.",
        ),
        default=None,
    )
    index: Optional[int] = Field(
        description="The zero-based index of the tab within the parent.",
        default=None,
    )
    nesting_level: Optional[int] = Field(
        description="Output only. The depth of the tab within the document. Root-level tabs start at 0.",
        default=None,
    )


class TabStopAlignment(str, Enum):
    """
    The alignment of the tab stop.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#tabstopalignment

    TAB_STOP_ALIGNMENT_UNSPECIFIED: The tab stop alignment is unspecified.

    START: The tab stop is aligned to the start of the line. This is the default.

    CENTER: The tab stop is aligned to the center of the line.

    END: The tab stop is aligned to the end of the line.
    """

    TAB_STOP_ALIGNMENT_UNSPECIFIED = "TAB_STOP_ALIGNMENT_UNSPECIFIED"
    START = "START"
    CENTER = "CENTER"
    END = "END"


class TableCellStyleSuggestionState(BaseModel):
    """
    A mask that indicates which of the fields on the base TableCellStyle have been changed in this suggestion. For any field set to true, there's a new suggested value.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#tablecellstylesuggestionstate
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    row_span_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to rowSpan.",
        default=None,
    )
    column_span_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to columnSpan.",
        default=None,
    )
    background_color_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to backgroundColor.",
        default=None,
    )
    border_left_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to borderLeft.",
        default=None,
    )
    border_right_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to borderRight.",
        default=None,
    )
    border_top_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to borderTop.",
        default=None,
    )
    border_bottom_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to borderBottom.",
        default=None,
    )
    padding_left_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to paddingLeft.",
        default=None,
    )
    padding_right_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to paddingRight.",
        default=None,
    )
    padding_top_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to paddingTop.",
        default=None,
    )
    padding_bottom_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to paddingBottom.",
        default=None,
    )
    content_alignment_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to contentAlignment.",
        default=None,
    )


class TableRowStyleSuggestionState(BaseModel):
    """
    A mask that indicates which of the fields on the base TableRowStyle have been changed in this suggestion. For any field set to true, there's a new suggested value.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#tablerowstylesuggestionstate
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    min_row_height_suggested: Optional[list[bool]] = Field(
        description="Indicates if there was a suggested change to minRowHeight.",
        default=None,
    )


class TextStyleSuggestionState(BaseModel):
    """
    A mask that indicates which of the fields on the base TextStyle have been changed in this suggestion. For any field set to true, there's a new suggested value.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#textstylesuggestionstate
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    bold_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to bold.",
        default=None,
    )
    italic_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to italic.",
        default=None,
    )
    underline_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to underline.",
        default=None,
    )
    strikethrough_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to strikethrough.",
        default=None,
    )
    small_caps_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to smallCaps.",
        default=None,
    )
    background_color_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to backgroundColor.",
        default=None,
    )
    foreground_color_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to foregroundColor.",
        default=None,
    )
    font_size_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to fontSize.",
        default=None,
    )
    weighted_font_family_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to weightedFontFamily.",
        default=None,
    )
    baseline_offset_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to baselineOffset.",
        default=None,
    )
    link_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to link.",
        default=None,
    )


class Unit(str, Enum):
    """
    Units of measurement.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#unit

    UNIT_UNSPECIFIED: The units are unknown.

    PT: A point, 1/72 of an inch.
    """

    UNIT_UNSPECIFIED = "UNIT_UNSPECIFIED"
    PT = "PT"


class WeightedFontFamily(BaseModel):
    """
    Represents a font family and weight of text.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#weightedfontfamily
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    font_family: Optional[str] = Field(
        description=(
            "The font family of the text. The font family can be any font from the Font menu in Docs or from Goog",
            "le Fonts. If the font name is unrecognized, the text is rendered in Arial.",
        ),
        default=None,
    )
    weight: Optional[int] = Field(
        description=(
            "The weight of the font. This field can have any value that's a multiple of 100 between 100 and 900, ",
            "inclusive. This range corresponds to the numerical values described in the CSS 2.1 Specification, se",
            'ction 15.6, with non-numerical values disallowed. The default value is 400 ("normal"). The font we',
            "ight makes up just one component of the rendered font weight. A combination of the weight and the te",
            "xt style's resolved bold value determine the rendered weight, after accounting for inheritance:",
        ),
        default=None,
    )


class BulletSuggestionState(BaseModel):
    """
    A mask that indicates which of the fields on the base Bullet have been changed in this suggestion. For any field set to true, there's a new suggested value.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#bulletsuggestionstate
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    list_id_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to the listId.",
        default=None,
    )
    nesting_level_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to the nestingLevel.",
        default=None,
    )
    text_style_suggestion_state: Optional[list[TextStyleSuggestionState]] = Field(
        description="A mask that indicates which of the fields in text style have been changed in this suggestion.",
        default=None,
    )


class Color(BaseModel):
    """
    A solid color.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#color
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    rgb_color: Optional[RgbColor] = Field(
        description="The RGB color value.",
        default=None,
    )


class Dimension(BaseModel):
    """
    A magnitude in a single direction in the specified units.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#dimension
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    magnitude: Optional[float] = Field(
        description="The magnitude.",
        default=None,
    )
    unit: Unit = Field(
        description="The units for magnitude.",
        default=None,
    )


class DocumentStyleSuggestionState(BaseModel):
    """
    A mask that indicates which of the fields on the base DocumentStyle have been changed in this suggestion. For any field set to true, there's a new suggested value.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#documentstylesuggestionstate
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    background_suggestion_state: Optional[BackgroundSuggestionState] = Field(
        description="A mask that indicates which of the fields in background have been changed in this suggestion.",
        default=None,
    )
    default_header_id_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to defaultHeaderId.",
        default=None,
    )
    default_footer_id_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to defaultFooterId.",
        default=None,
    )
    even_page_header_id_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to evenPageHeaderId.",
        default=None,
    )
    even_page_footer_id_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to evenPageFooterId.",
        default=None,
    )
    first_page_header_id_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to firstPageHeaderId.",
        default=None,
    )
    first_page_footer_id_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to firstPageFooterId.",
        default=None,
    )
    use_first_page_header_footer_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to useFirstPageHeaderFooter.",
        default=None,
    )
    use_even_page_header_footer_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to useEvenPageHeaderFooter.",
        default=None,
    )
    page_number_start_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to pageNumberStart.",
        default=None,
    )
    margin_top_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to marginTop.",
        default=None,
    )
    margin_bottom_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to marginBottom.",
        default=None,
    )
    margin_right_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to marginRight.",
        default=None,
    )
    margin_left_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to marginLeft.",
        default=None,
    )
    page_size_suggestion_state: Optional[SizeSuggestionState] = Field(
        description=(
            "A mask that indicates which of the fields in [size] [google.apps.docs.v1.DocumentStyle.size] have be",
            "en changed in this suggestion.",
        ),
        default=None,
    )
    margin_header_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to marginHeader.",
        default=None,
    )
    margin_footer_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to marginFooter.",
        default=None,
    )
    use_custom_header_footer_margins_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to useCustomHeaderFooterMargins.",
        default=None,
    )
    flip_page_orientation_suggested: Optional[bool] = Field(
        description="Optional. Indicates if there was a suggested change to flipPageOrientation.",
        default=None,
    )


class LinkedContentReference(BaseModel):
    """
    A reference to the external linked source content.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#linkedcontentreference
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    sheets_chart_reference: Optional[SheetsChartReference] = Field(
        description="A reference to the linked chart.",
        default=None,
    )


class LinkedContentReferenceSuggestionState(BaseModel):
    """
    A mask that indicates which of the fields on the base LinkedContentReference have been changed in this suggestion. For any field set to true, there's a new suggested value.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#linkedcontentreferencesuggestionstate
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    sheets_chart_reference_suggestion_state: Optional[
        SheetsChartReferenceSuggestionState
    ] = Field(
        description=(
            "A mask that indicates which of the fields in sheetsChartReference have been changed in this suggesti",
            "on.",
        ),
        default=None,
    )


class NamedRange(BaseModel):
    """
    A collection of Ranges with the same named range ID.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#namedrange
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    named_range_id: Optional[str] = Field(
        description="The ID of the named range.",
        default=None,
    )
    name: Optional[list[str]] = Field(
        description="The name of the named range.",
        default=None,
    )
    ranges: Optional[Range] = Field(
        description="The ranges that belong to this named range.",
        default=None,
    )


class NamedRanges(BaseModel):
    """
    A collection of all the NamedRanges in the document that share a given name.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#namedranges
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    name: Optional[list[str]] = Field(
        description="The name that all the named ranges share.",
        default=None,
    )
    named_ranges: Optional[NamedRange] = Field(
        description="The NamedRanges that share the same name.",
        default=None,
    )


class NestingLevelSuggestionState(BaseModel):
    """
    A mask that indicates which of the fields on the base NestingLevel have been changed in this suggestion. For any field set to true, there's a new suggested value.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#nestinglevelsuggestionstate
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    bullet_alignment_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to bulletAlignment.",
        default=None,
    )
    glyph_type_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to glyphType.",
        default=None,
    )
    glyph_format_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to glyphFormat.",
        default=None,
    )
    glyph_symbol_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to glyphSymbol.",
        default=None,
    )
    indent_first_line_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to indentFirstLine.",
        default=None,
    )
    indent_start_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to indentStart.",
        default=None,
    )
    text_style_suggestion_state: Optional[TextStyleSuggestionState] = Field(
        description="A mask that indicates which of the fields in text style have been changed in this suggestion.",
        default=None,
    )
    start_number_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to startNumber.",
        default=None,
    )


class OptionalColor(BaseModel):
    """
    A color that can either be fully opaque or fully transparent.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#optionalcolor
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    color: Optional[Color] = Field(
        description="If set, this will be used as an opaque color. If unset, this represents a transparent color.",
        default=None,
    )


class ParagraphBorder(BaseModel):
    """
    A border around a paragraph.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#paragraphborder
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    color: Optional[OptionalColor] = Field(
        description="The color of the border.",
        default=None,
    )
    width: Optional[Dimension] = Field(
        description="The width of the border.",
        default=None,
    )
    padding: Optional[Dimension] = Field(
        description="The padding of the border.",
        default=None,
    )
    dash_style: DashStyle = Field(
        description="The dash style of the border.",
        default=None,
    )


class ParagraphStyleSuggestionState(BaseModel):
    """
    A mask that indicates which of the fields on the base ParagraphStyle have been changed in this suggestion. For any field set to true, there's a new suggested value.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#paragraphstylesuggestionstate
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    heading_id_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to headingId.",
        default=None,
    )
    named_style_type_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to namedStyleType.",
        default=None,
    )
    alignment_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to alignment.",
        default=None,
    )
    line_spacing_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to lineSpacing.",
        default=None,
    )
    direction_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to direction.",
        default=None,
    )
    spacing_mode_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to spacingMode.",
        default=None,
    )
    space_above_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to spaceAbove.",
        default=None,
    )
    space_below_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to spaceBelow.",
        default=None,
    )
    border_between_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to borderBetween.",
        default=None,
    )
    border_top_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to borderTop.",
        default=None,
    )
    border_bottom_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to borderBottom.",
        default=None,
    )
    border_left_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to borderLeft.",
        default=None,
    )
    border_right_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to borderRight.",
        default=None,
    )
    indent_first_line_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to indentFirstLine.",
        default=None,
    )
    indent_start_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to indentStart.",
        default=None,
    )
    indent_end_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to indentEnd.",
        default=None,
    )
    keep_lines_together_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to keepLinesTogether.",
        default=None,
    )
    keep_with_next_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to keepWithNext.",
        default=None,
    )
    avoid_widow_and_orphan_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to avoidWidowAndOrphan.",
        default=None,
    )
    shading_suggestion_state: Optional[ShadingSuggestionState] = Field(
        description="A mask that indicates which of the fields in shading have been changed in this suggestion.",
        default=None,
    )
    page_break_before_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to pageBreakBefore.",
        default=None,
    )


class PositionedObjectPositioning(BaseModel):
    """
    The positioning of a PositionedObject. The positioned object is positioned relative to the beginning of the Paragraph it's tethered to.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#positionedobjectpositioning
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    layout: PositionedObjectLayout = Field(
        description="The layout of this positioned object.",
        default=None,
    )
    left_offset: Optional[Dimension] = Field(
        description=(
            "The offset of the left edge of the positioned object relative to the beginning of the Paragraph it's",
            " tethered to. The exact positioning of the object can depend on other content in the document and th",
            "e document's styling.",
        ),
        default=None,
    )
    top_offset: Optional[Dimension] = Field(
        description=(
            "The offset of the top edge of the positioned object relative to the beginning of the Paragraph it's ",
            "tethered to. The exact positioning of the object can depend on other content in the document and the",
            " document's styling.",
        ),
        default=None,
    )


class SectionColumnProperties(BaseModel):
    """
    Properties that apply to a section's column.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#sectioncolumnproperties
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    width: Optional[Dimension] = Field(
        description="Output only. The width of the column.",
        default=None,
    )
    padding_end: Optional[Dimension] = Field(
        description="The padding at the end of the column.",
        default=None,
    )


class SectionStyle(BaseModel):
    """
    The styling that applies to a section.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#sectionstyle
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    column_properties: Optional[SectionColumnProperties] = Field(
        description=(
            "The section's columns properties. If empty, the section contains one column with the default propert",
            "ies in the Docs editor. A section can be updated to have no more than 3 columns. When updating this ",
            "property, setting a concrete value is required. Unsetting this property will result in a 400 bad req",
            "uest error.",
        ),
        default=None,
    )
    column_separator_style: ColumnSeparatorStyle = Field(
        description=(
            "The style of column separators. This style can be set even when there's one column in the section. W",
            "hen updating this property, setting a concrete value is required. Unsetting this property results in",
            " a 400 bad request error.",
        ),
        default=None,
    )
    content_direction: ContentDirection = Field(
        description=(
            "The content direction of this section. If unset, the value defaults to LEFT_TO_RIGHT. When updating ",
            "this property, setting a concrete value is required. Unsetting this property results in a 400 bad re",
            "quest error.",
        ),
        default=None,
    )
    margin_top: Optional[Dimension] = Field(
        description=(
            "The top page margin of the section. If unset, the value defaults to marginTop from DocumentStyle. Wh",
            "en updating this property, setting a concrete value is required. Unsetting this property results in ",
            "a 400 bad request error.",
        ),
        default=None,
    )
    margin_bottom: Optional[Dimension] = Field(
        description=(
            "The bottom page margin of the section. If unset, the value defaults to marginBottom from DocumentSty",
            "le. When updating this property, setting a concrete value is required. Unsetting this property resul",
            "ts in a 400 bad request error.",
        ),
        default=None,
    )
    margin_right: Optional[Dimension] = Field(
        description=(
            "The right page margin of the section. If unset, the value defaults to marginRight from DocumentStyle",
            ". Updating the right margin causes columns in this section to resize. Since the margin affects colum",
            "n width, it's applied before column properties. When updating this property, setting a concrete valu",
            "e is required. Unsetting this property results in a 400 bad request error.",
        ),
        default=None,
    )
    margin_left: Optional[Dimension] = Field(
        description=(
            "The left page margin of the section. If unset, the value defaults to marginLeft from DocumentStyle. ",
            "Updating the left margin causes columns in this section to resize. Since the margin affects column w",
            "idth, it's applied before column properties. When updating this property, setting a concrete value i",
            "s required. Unsetting this property results in a 400 bad request error.",
        ),
        default=None,
    )
    margin_header: Optional[Dimension] = Field(
        description=(
            "The header margin of the section. If unset, the value defaults to marginHeader from DocumentStyle. I",
            "f updated, useCustomHeaderFooterMargins is set to true on DocumentStyle. The value of useCustomHeade",
            "rFooterMargins on DocumentStyle indicates if a header margin is being respected for this section. Wh",
            "en updating this property, setting a concrete value is required. Unsetting this property results in ",
            "a 400 bad request error.",
        ),
        default=None,
    )
    margin_footer: Optional[Dimension] = Field(
        description=(
            "The footer margin of the section. If unset, the value defaults to marginFooter from DocumentStyle. I",
            "f updated, useCustomHeaderFooterMargins is set to true on DocumentStyle. The value of useCustomHeade",
            "rFooterMargins on DocumentStyle indicates if a footer margin is being respected for this section Whe",
            "n updating this property, setting a concrete value is required. Unsetting this property results in a",
            " 400 bad request error.",
        ),
        default=None,
    )
    section_type: SectionType = Field(
        description="Output only. The type of section.",
        default=None,
    )
    default_header_id: Optional[str] = Field(
        description=(
            "The ID of the default header. If unset, the value inherits from the previous SectionBreak's SectionS",
            "tyle. If the value is unset in the first SectionBreak, it inherits from DocumentStyle's defaultHeade",
            "rId. This property is read-only.",
        ),
        default=None,
    )
    default_footer_id: Optional[str] = Field(
        description=(
            "The ID of the default footer. If unset, the value inherits from the previous SectionBreak's SectionS",
            "tyle. If the value is unset in the first SectionBreak, it inherits from DocumentStyle's defaultFoote",
            "rId. This property is read-only.",
        ),
        default=None,
    )
    first_page_header_id: Optional[str] = Field(
        description=(
            "The ID of the header used only for the first page of the section. If useFirstPageHeaderFooter is tru",
            "e, this value is used for the header on the first page of the section. If it's false, the header on ",
            "the first page of the section uses the defaultHeaderId. If unset, the value inherits from the previo",
            "us SectionBreak's SectionStyle. If the value is unset in the first SectionBreak, it inherits from Do",
            "cumentStyle's firstPageHeaderId. This property is read-only.",
        ),
        default=None,
    )
    first_page_footer_id: Optional[str] = Field(
        description=(
            "The ID of the footer used only for the first page of the section. If useFirstPageHeaderFooter is tru",
            "e, this value is used for the footer on the first page of the section. If it's false, the footer on ",
            "the first page of the section uses the defaultFooterId. If unset, the value inherits from the previo",
            "us SectionBreak's SectionStyle. If the value is unset in the first SectionBreak, it inherits from Do",
            "cumentStyle's firstPageFooterId. This property is read-only.",
        ),
        default=None,
    )
    even_page_header_id: Optional[str] = Field(
        description=(
            "The ID of the header used only for even pages. If the value of DocumentStyle's useEvenPageHeaderFoot",
            "er is true, this value is used for the headers on even pages in the section. If it is false, the hea",
            "ders on even pages use the defaultHeaderId. If unset, the value inherits from the previous SectionBr",
            "eak's SectionStyle. If the value is unset in the first SectionBreak, it inherits from DocumentStyle'",
            "s evenPageHeaderId. This property is read-only.",
        ),
        default=None,
    )
    even_page_footer_id: Optional[str] = Field(
        description=(
            "The ID of the footer used only for even pages. If the value of DocumentStyle's useEvenPageHeaderFoot",
            "er is true, this value is used for the footers on even pages in the section. If it is false, the foo",
            "ters on even pages use the defaultFooterId. If unset, the value inherits from the previous SectionBr",
            "eak's SectionStyle. If the value is unset in the first SectionBreak, it inherits from DocumentStyle'",
            "s evenPageFooterId. This property is read-only.",
        ),
        default=None,
    )
    use_first_page_header_footer: Optional[bool] = Field(
        description=(
            "Indicates whether to use the first page header / footer IDs for the first page of the section. If un",
            "set, it inherits from DocumentStyle's useFirstPageHeaderFooter for the first section. If the value i",
            "s unset for subsequent sectors, it should be interpreted as false. When updating this property, sett",
            "ing a concrete value is required. Unsetting this property results in a 400 bad request error.",
        ),
        default=None,
    )
    page_number_start: Optional[int] = Field(
        description=(
            "The page number from which to start counting the number of pages for this section. If unset, page nu",
            "mbering continues from the previous section. If the value is unset in the first SectionBreak, refer ",
            "to DocumentStyle's pageNumberStart. When updating this property, setting a concrete value is require",
            "d. Unsetting this property results in a 400 bad request error.",
        ),
        default=None,
    )
    flip_page_orientation: Optional[bool] = Field(
        description=(
            "Optional. Indicates whether to flip the dimensions of DocumentStyle's pageSize for this section, whi",
            "ch allows changing the page orientation between portrait and landscape. If unset, the value inherits",
            " from DocumentStyle's flipPageOrientation. When updating this property, setting a concrete value is ",
            "required. Unsetting this property results in a 400 bad request error.",
        ),
        default=None,
    )


class Shading(BaseModel):
    """
    The shading of a paragraph.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#shading
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    background_color: Optional[OptionalColor] = Field(
        description="The background color of this paragraph shading.",
        default=None,
    )


class Size(BaseModel):
    """
    A width and height.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#size
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    height: Optional[Dimension] = Field(
        description="The height of the object.",
        default=None,
    )
    width: Optional[Dimension] = Field(
        description="The width of the object.",
        default=None,
    )


class TabStop(BaseModel):
    """
    A tab stop within a paragraph.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#tabstop
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    offset: Optional[Dimension] = Field(
        description="The offset between this tab stop and the start margin.",
        default=None,
    )
    alignment: TabStopAlignment = Field(
        description="The alignment of this tab stop. If unset, the value defaults to START.",
        default=None,
    )


class TableCellBorder(BaseModel):
    """
    A border around a table cell.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#tablecellborder
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    color: Optional[OptionalColor] = Field(
        description="The color of the border. This color cannot be transparent.",
        default=None,
    )
    width: Optional[Dimension] = Field(
        description="The width of the border.",
        default=None,
    )
    dash_style: DashStyle = Field(
        description="The dash style of the border.",
        default=None,
    )


class TableCellStyle(BaseModel):
    """
    The style of a TableCell.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#tablecellstyle
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    row_span: Optional[int] = Field(
        description="The row span of the cell. This property is read-only.",
        default=None,
    )
    column_span: Optional[int] = Field(
        description="The column span of the cell. This property is read-only.",
        default=None,
    )
    background_color: Optional[OptionalColor] = Field(
        description="The background color of the cell.",
        default=None,
    )
    border_left: Optional[TableCellBorder] = Field(
        description="The left border of the cell.",
        default=None,
    )
    border_right: Optional[TableCellBorder] = Field(
        description="The right border of the cell.",
        default=None,
    )
    border_top: Optional[TableCellBorder] = Field(
        description="The top border of the cell.",
        default=None,
    )
    border_bottom: Optional[TableCellBorder] = Field(
        description="The bottom border of the cell.",
        default=None,
    )
    padding_left: Optional[Dimension] = Field(
        description="The left padding of the cell.",
        default=None,
    )
    padding_right: Optional[Dimension] = Field(
        description="The right padding of the cell.",
        default=None,
    )
    padding_top: Optional[Dimension] = Field(
        description="The top padding of the cell.",
        default=None,
    )
    padding_bottom: Optional[Dimension] = Field(
        description="The bottom padding of the cell.",
        default=None,
    )
    content_alignment: ContentAlignment = Field(
        description=(
            "The alignment of the content in the table cell. The default alignment matches the alignment for newl",
            "y created table cells in the Docs editor.",
        ),
        default=None,
    )


class TableColumnProperties(BaseModel):
    """
    The properties of a column in a table.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#tablecolumnproperties
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    width_type: WidthType = Field(
        description="The width type of the column.",
        default=None,
    )
    width: Optional[Dimension] = Field(
        description="The width of the column. Set when the column's widthType is FIXED_WIDTH.",
        default=None,
    )


class TableRowStyle(BaseModel):
    """
    Styles that apply to a table row.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#tablerowstyle
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    min_row_height: Optional[Dimension] = Field(
        description=(
            "The minimum height of the row. The row will be rendered in the Docs editor at a height equal to or g",
            "reater than this value in order to show all the content in the row's cells.",
        ),
        default=None,
    )
    table_header: Optional[bool] = Field(
        description="Whether the row is a table header.",
        default=None,
    )
    prevent_overflow: Optional[bool] = Field(
        description="Whether the row cannot overflow across page or column boundaries.",
        default=None,
    )


class TableStyle(BaseModel):
    """
    Styles that apply to a table.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#tablestyle
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    table_column_properties: Optional[TableColumnProperties] = Field(
        description=(
            "The properties of each column. Note that in Docs, tables contain rows and rows contain cells, simila",
            "r to HTML. So the properties for a row can be found on the row's tableRowStyle.",
        ),
        default=None,
    )


class TextStyle(BaseModel):
    """
    Represents the styling that can be applied to text.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#textstyle
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    bold: Optional[bool] = Field(
        description="Whether or not the text is rendered as bold.",
        default=None,
    )
    italic: Optional[bool] = Field(
        description="Whether or not the text is italicized.",
        default=None,
    )
    underline: Optional[bool] = Field(
        description="Whether or not the text is underlined.",
        default=None,
    )
    strikethrough: Optional[bool] = Field(
        description="Whether or not the text is struck through.",
        default=None,
    )
    small_caps: Optional[bool] = Field(
        description="Whether or not the text is in small capital letters.",
        default=None,
    )
    background_color: Optional[OptionalColor] = Field(
        description=(
            "The background color of the text. If set, the color is either an RGB color or transparent, depending",
            " on the color field.",
        ),
        default=None,
    )
    foreground_color: Optional[OptionalColor] = Field(
        description=(
            "The foreground color of the text. If set, the color is either an RGB color or transparent, depending",
            " on the color field.",
        ),
        default=None,
    )
    font_size: Optional[Dimension] = Field(
        description="The size of the text's font.",
        default=None,
    )
    weighted_font_family: Optional[WeightedFontFamily] = Field(
        description=(
            "The font family and rendered weight of the text. If an update request specifies values for both weig",
            "htedFontFamily and bold, the weightedFontFamily is applied first, then bold. If weightedFontFamily#w",
            "eight is not set, it defaults to 400. If weightedFontFamily is set, then weightedFontFamily#fontFami",
            "ly must also be set with a non-empty value. Otherwise, a 400 bad request error is returned.",
        ),
        default=None,
    )
    baseline_offset: BaselineOffset = Field(
        description=(
            "The text's vertical offset from its normal position. Text with SUPERSCRIPT or SUBSCRIPT baseline off",
            "sets is automatically rendered in a smaller font size, computed based on the fontSize field. Changes",
            " in this field don't affect the fontSize.",
        ),
        default=None,
    )
    link: Optional[Link] = Field(
        description=(
            "The hyperlink destination of the text. If unset, there's no link. Links are not inherited from paren",
            "t text. Changing the link in an update request causes some other changes to the text style of the ra",
            "nge:",
        ),
        default=None,
    )


class Background(BaseModel):
    """
    Represents the background of a document.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#background
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    color: Optional[OptionalColor] = Field(
        description="The background color.",
        default=None,
    )


class Bullet(BaseModel):
    """
    Describes the bullet of a paragraph.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#bullet
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    list_id: Optional[str] = Field(
        description="The ID of the list this paragraph belongs to.",
        default=None,
    )
    nesting_level: Optional[int] = Field(
        description="The nesting level of this paragraph in the list.",
        default=None,
    )
    text_style: Optional[TextStyle] = Field(
        description="The paragraph-specific text style applied to this bullet.",
        default=None,
    )


class DocumentStyle(BaseModel):
    """
    The style of the document.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#documentstyle
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    background: Optional[Background] = Field(
        description="The background of the document. Documents cannot have a transparent background color.",
        default=None,
    )
    default_header_id: Optional[str] = Field(
        description="The ID of the default header. If not set, there's no default header. This property is read-only.",
        default=None,
    )
    default_footer_id: Optional[str] = Field(
        description="The ID of the default footer. If not set, there's no default footer. This property is read-only.",
        default=None,
    )
    even_page_header_id: Optional[str] = Field(
        description=(
            "The ID of the header used only for even pages. The value of useEvenPageHeaderFooter determines wheth",
            "er to use the defaultHeaderId or this value for the header on even pages. If not set, there's no eve",
            "n page header. This property is read-only.",
        ),
        default=None,
    )
    even_page_footer_id: Optional[str] = Field(
        description=(
            "The ID of the footer used only for even pages. The value of useEvenPageHeaderFooter determines wheth",
            "er to use the defaultFooterId or this value for the footer on even pages. If not set, there's no eve",
            "n page footer. This property is read-only.",
        ),
        default=None,
    )
    first_page_header_id: Optional[str] = Field(
        description=(
            "The ID of the header used only for the first page. If not set then a unique header for the first pag",
            "e does not exist. The value of useFirstPageHeaderFooter determines whether to use the defaultHeaderI",
            "d or this value for the header on the first page. If not set, there's no first page header. This pro",
            "perty is read-only.",
        ),
        default=None,
    )
    first_page_footer_id: Optional[str] = Field(
        description=(
            "The ID of the footer used only for the first page. If not set then a unique footer for the first pag",
            "e does not exist. The value of useFirstPageHeaderFooter determines whether to use the defaultFooterI",
            "d or this value for the footer on the first page. If not set, there's no first page footer. This pro",
            "perty is read-only.",
        ),
        default=None,
    )
    use_first_page_header_footer: Optional[bool] = Field(
        description="Indicates whether to use the first page header / footer IDs for the first page.",
        default=None,
    )
    use_even_page_header_footer: Optional[bool] = Field(
        description="Indicates whether to use the even page header / footer IDs for the even pages.",
        default=None,
    )
    page_number_start: Optional[int] = Field(
        description="The page number from which to start counting the number of pages.",
        default=None,
    )
    margin_top: Optional[Dimension] = Field(
        description=(
            "The top page margin. Updating the top page margin on the document style clears the top page margin o",
            "n all section styles.",
        ),
        default=None,
    )
    margin_bottom: Optional[Dimension] = Field(
        description=(
            "The bottom page margin. Updating the bottom page margin on the document style clears the bottom page",
            " margin on all section styles.",
        ),
        default=None,
    )
    margin_right: Optional[Dimension] = Field(
        description=(
            "The right page margin. Updating the right page margin on the document style clears the right page ma",
            "rgin on all section styles. It may also cause columns to resize in all sections.",
        ),
        default=None,
    )
    margin_left: Optional[Dimension] = Field(
        description=(
            "The left page margin. Updating the left page margin on the document style clears the left page margi",
            "n on all section styles. It may also cause columns to resize in all sections.",
        ),
        default=None,
    )
    page_size: Optional[Size] = Field(
        description="The size of a page in the document.",
        default=None,
    )
    margin_header: Optional[Dimension] = Field(
        description="The amount of space between the top of the page and the contents of the header.",
        default=None,
    )
    margin_footer: Optional[Dimension] = Field(
        description="The amount of space between the bottom of the page and the contents of the footer.",
        default=None,
    )
    use_custom_header_footer_margins: Optional[bool] = Field(
        description=(
            "Indicates whether DocumentStyle marginHeader, SectionStyle marginHeader and DocumentStyle marginFoot",
            "er, SectionStyle marginFooter are respected. When false, the default values in the Docs editor for h",
            "eader and footer margin is used. This property is read-only.",
        ),
        default=None,
    )
    flip_page_orientation: Optional[bool] = Field(
        description=(
            "Optional. Indicates whether to flip the dimensions of the pageSize, which allows changing the page o",
            "rientation between portrait and landscape.",
        ),
        default=None,
    )


class EmbeddedObjectBorder(BaseModel):
    """
    A border around an EmbeddedObject.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#embeddedobjectborder
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    color: Optional[OptionalColor] = Field(
        description="The color of the border.",
        default=None,
    )
    width: Optional[Dimension] = Field(
        description="The width of the border.",
        default=None,
    )
    dash_style: DashStyle = Field(
        description="The dash style of the border.",
        default=None,
    )
    property_state: PropertyState = Field(
        description="The property state of the border property.",
        default=None,
    )


class EmbeddedObjectSuggestionState(BaseModel):
    """
    A mask that indicates which of the fields on the base EmbeddedObject have been changed in this suggestion. For any field set to true, there's a new suggested value.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#embeddedobjectsuggestionstate
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    embedded_drawing_properties_suggestion_state: Optional[
        EmbeddedDrawingPropertiesSuggestionState
    ] = Field(
        description=(
            "A mask that indicates which of the fields in embeddedDrawingProperties have been changed in this sug",
            "gestion.",
        ),
        default=None,
    )
    image_properties_suggestion_state: Optional[ImagePropertiesSuggestionState] = Field(
        description="A mask that indicates which of the fields in imageProperties have been changed in this suggestion.",
        default=None,
    )
    title_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to title.",
        default=None,
    )
    description_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to description.",
        default=None,
    )
    embedded_object_border_suggestion_state: Optional[
        EmbeddedObjectBorderSuggestionState
    ] = Field(
        description=(
            "A mask that indicates which of the fields in embeddedObjectBorder have been changed in this suggesti",
            "on.",
        ),
        default=None,
    )
    size_suggestion_state: Optional[SizeSuggestionState] = Field(
        description="A mask that indicates which of the fields in size have been changed in this suggestion.",
        default=None,
    )
    margin_left_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to marginLeft.",
        default=None,
    )
    margin_right_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to marginRight.",
        default=None,
    )
    margin_top_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to marginTop.",
        default=None,
    )
    margin_bottom_suggested: Optional[bool] = Field(
        description="Indicates if there was a suggested change to marginBottom.",
        default=None,
    )
    linked_content_reference_suggestion_state: Optional[
        LinkedContentReferenceSuggestionState
    ] = Field(
        description=(
            "A mask that indicates which of the fields in linkedContentReference have been changed in this sugges",
            "tion.",
        ),
        default=None,
    )


class InlineObjectPropertiesSuggestionState(BaseModel):
    """
    A mask that indicates which of the fields on the base InlineObjectProperties have been changed in this suggestion. For any field set to true, there's a new suggested value.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#inlineobjectpropertiessuggestionstate
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    embedded_object_suggestion_state: Optional[EmbeddedObjectSuggestionState] = Field(
        description="A mask that indicates which of the fields in embeddedObject have been changed in this suggestion.",
        default=None,
    )


class ListPropertiesSuggestionState(BaseModel):
    """
    A mask that indicates which of the fields on the base ListProperties have been changed in this suggestion. For any field set to true, there's a new suggested value.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#listpropertiessuggestionstate
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    nesting_levels_suggestion_states: Optional[NestingLevelSuggestionState] = Field(
        description=(
            "A mask that indicates which of the fields on the corresponding NestingLevel in nestingLevels have be",
            "en changed in this suggestion. The nesting level suggestion states are returned in ascending order o",
            "f the nesting level with the least nested returned first.",
        ),
        default=None,
    )


class NamedStyleSuggestionState(BaseModel):
    """
    A suggestion state of a NamedStyle message.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#namedstylesuggestionstate
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    named_style_type: NamedStyleType = Field(
        description=(
            "The named style type that this suggestion state corresponds to. This field is provided as a convenie",
            "nce for matching the NamedStyleSuggestionState with its corresponding NamedStyle.",
        ),
        default=None,
    )
    text_style_suggestion_state: Optional[TextStyleSuggestionState] = Field(
        description="A mask that indicates which of the fields in text style have been changed in this suggestion.",
        default=None,
    )
    paragraph_style_suggestion_state: Optional[ParagraphStyleSuggestionState] = Field(
        description="A mask that indicates which of the fields in paragraph style have been changed in this suggestion.",
        default=None,
    )


class NamedStylesSuggestionState(BaseModel):
    """
    The suggestion state of a NamedStyles message.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#namedstylessuggestionstate
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    styles_suggestion_states: Optional[NamedStyleSuggestionState] = Field(
        description=(
            "A mask that indicates which of the fields on the corresponding NamedStyle in styles have been change",
            "d in this suggestion. The order of these named style suggestion states matches the order of the corr",
            "esponding named style within the named styles suggestion.",
        ),
        default=None,
    )


class NestingLevel(BaseModel):
    """
    Contains properties describing the look and feel of a list bullet at a given level of nesting.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#nestinglevel
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    bullet_alignment: BulletAlignment = Field(
        description="The alignment of the bullet within the space allotted for rendering the bullet.",
        default=None,
    )
    glyph_format: Optional[str] = Field(
        description=(
            "The format string used by bullets at this level of nesting. The glyph format contains one or more pl",
            "aceholders, and these placeholders are replaced with the appropriate values depending on the glyphTy",
            "pe or glyphSymbol. The placeholders follow the pattern %[nestingLevel]. Furthermore, placeholders ca",
            "n have prefixes and suffixes. Thus, the glyph format follows the pattern %[nestingLevel]. Note that ",
            "the prefix and suffix are optional and can be arbitrary strings. For example, the glyph format %0. i",
            "ndicates that the rendered glyph will replace the placeholder with the corresponding glyph for nesti",
            "ng level 0 followed by a period as the suffix. So a list with a glyph type of UPPER_ALPHA and glyph ",
            "format %0. at nesting level 0 will result in a list with rendered glyphs A. B. C. The glyph format c",
            "an contain placeholders for the current nesting level as well as placeholders for parent nesting lev",
            "els. For example, a list can have a glyph format of %0. at nesting level 0 and a glyph format of %0.",
            "%1. at nesting level 1. Assuming both nesting levels have DECIMAL glyph types, this would result in ",
            "a list with rendered glyphs 1. 2. 2.1. 2.2. 3. For nesting levels that are ordered, the string that ",
            "replaces a placeholder in the glyph format for a particular paragraph depends on the paragraph's ord",
            "er within the list.",
        ),
        default=None,
    )
    indent_first_line: Optional[Dimension] = Field(
        description="The amount of indentation for the first line of paragraphs at this level of nesting.",
        default=None,
    )
    indent_start: Optional[Dimension] = Field(
        description=(
            "The amount of indentation for paragraphs at this level of nesting. Applied to the side that correspo",
            "nds to the start of the text, based on the paragraph's content direction.",
        ),
        default=None,
    )
    text_style: Optional[TextStyle] = Field(
        description="The text style of bullets at this level of nesting.",
        default=None,
    )
    start_number: Optional[int] = Field(
        description=(
            "The number of the first list item at this nesting level. A value of 0 is treated as a value of 1 for",
            " lettered lists and Roman numeral lists. For values of both 0 and 1, lettered and Roman numeral list",
            "s will begin at a and i respectively. This value is ignored for nesting levels with unordered glyphs",
            ".",
        ),
        default=None,
    )
    glyph_type: GlyphType = Field(
        description=(
            "The type of glyph used by bullets when paragraphs at this level of nesting is ordered. The glyph typ",
            "e determines the type of glyph used to replace placeholders within the glyphFormat when paragraphs a",
            "t this level of nesting are ordered. For example, if the nesting level is 0, the glyphFormat is %0. ",
            "and the glyph type is DECIMAL, then the rendered glyph would replace the placeholder %0 in the glyph",
            " format with a number corresponding to the list item's order within the list.",
        ),
        default=None,
    )
    glyph_symbol: Optional[str] = Field(
        description=(
            "A custom glyph symbol used by bullets when paragraphs at this level of nesting is unordered. The gly",
            "ph symbol replaces placeholders within the glyphFormat. For example, if the glyphSymbol is the solid",
            " circle corresponding to Unicode U+25cf code point and the glyphFormat is %0, the rendered glyph wou",
            "ld be the solid circle.",
        ),
        default=None,
    )


class ParagraphStyle(BaseModel):
    """
    Styles that apply to a whole paragraph.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#paragraphstyle
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    heading_id: Optional[str] = Field(
        description=(
            "The heading ID of the paragraph. If empty, then this paragraph is not a heading. This property is re",
            "ad-only.",
        ),
        default=None,
    )
    named_style_type: NamedStyleType = Field(
        description=(
            "The named style type of the paragraph. Since updating the named style type affects other properties ",
            "within ParagraphStyle, the named style type is applied before the other properties are updated.",
        ),
        default=None,
    )
    alignment: Alignment = Field(
        description="The text alignment for this paragraph.",
        default=None,
    )
    line_spacing: Optional[float] = Field(
        description=(
            "The amount of space between lines, as a percentage of normal, where normal is represented as 100.0. ",
            "If unset, the value is inherited from the parent.",
        ),
        default=None,
    )
    direction: ContentDirection = Field(
        description=(
            "The text direction of this paragraph. If unset, the value defaults to LEFT_TO_RIGHT since paragraph ",
            "direction is not inherited.",
        ),
        default=None,
    )
    spacing_mode: SpacingMode = Field(
        description="The spacing mode for the paragraph.",
        default=None,
    )
    space_above: Optional[Dimension] = Field(
        description="The amount of extra space above the paragraph. If unset, the value is inherited from the parent.",
        default=None,
    )
    space_below: Optional[Dimension] = Field(
        description="The amount of extra space below the paragraph. If unset, the value is inherited from the parent.",
        default=None,
    )
    border_between: Optional[ParagraphBorder] = Field(
        description=(
            "The border between this paragraph and the next and previous paragraphs. If unset, the value is inher",
            "ited from the parent. The between border is rendered when the adjacent paragraph has the same border",
            " and indent properties. Paragraph borders cannot be partially updated. When changing a paragraph bor",
            "der, the new border must be specified in its entirety.",
        ),
        default=None,
    )
    border_top: Optional[ParagraphBorder] = Field(
        description=(
            "The border at the top of this paragraph. If unset, the value is inherited from the parent. The top b",
            "order is rendered when the paragraph above has different border and indent properties. Paragraph bor",
            "ders cannot be partially updated. When changing a paragraph border, the new border must be specified",
            " in its entirety.",
        ),
        default=None,
    )
    border_bottom: Optional[ParagraphBorder] = Field(
        description=(
            "The border at the bottom of this paragraph. If unset, the value is inherited from the parent. The bo",
            "ttom border is rendered when the paragraph below has different border and indent properties. Paragra",
            "ph borders cannot be partially updated. When changing a paragraph border, the new border must be spe",
            "cified in its entirety.",
        ),
        default=None,
    )
    border_left: Optional[ParagraphBorder] = Field(
        description=(
            "The border to the left of this paragraph. If unset, the value is inherited from the parent. Paragrap",
            "h borders cannot be partially updated. When changing a paragraph border, the new border must be spec",
            "ified in its entirety.",
        ),
        default=None,
    )
    border_right: Optional[ParagraphBorder] = Field(
        description=(
            "The border to the right of this paragraph. If unset, the value is inherited from the parent. Paragra",
            "ph borders cannot be partially updated. When changing a paragraph border, the new border must be spe",
            "cified in its entirety.",
        ),
        default=None,
    )
    indent_first_line: Optional[Dimension] = Field(
        description=(
            "The amount of indentation for the first line of the paragraph. If unset, the value is inherited from",
            " the parent.",
        ),
        default=None,
    )
    indent_start: Optional[Dimension] = Field(
        description=(
            "The amount of indentation for the paragraph on the side that corresponds to the start of the text, b",
            "ased on the current paragraph direction. If unset, the value is inherited from the parent.",
        ),
        default=None,
    )
    indent_end: Optional[list[Dimension]] = Field(
        description=(
            "The amount of indentation for the paragraph on the side that corresponds to the end of the text, bas",
            "ed on the current paragraph direction. If unset, the value is inherited from the parent.",
        ),
        default=None,
    )
    tab_stops: Optional[TabStop] = Field(
        description=(
            "A list of the tab stops for this paragraph. The list of tab stops is not inherited. This property is",
            " read-only.",
        ),
        default=None,
    )
    keep_lines_together: Optional[bool] = Field(
        description=(
            "Whether all lines of the paragraph should be laid out on the same page or column if possible. If uns",
            "et, the value is inherited from the parent.",
        ),
        default=None,
    )
    keep_with_next: Optional[bool] = Field(
        description=(
            "Whether at least a part of this paragraph should be laid out on the same page or column as the next ",
            "paragraph if possible. If unset, the value is inherited from the parent.",
        ),
        default=None,
    )
    avoid_widow_and_orphan: Optional[bool] = Field(
        description=(
            "Whether to avoid widows and orphans for the paragraph. If unset, the value is inherited from the par",
            "ent.",
        ),
        default=None,
    )
    shading: Optional[Shading] = Field(
        description="The shading of the paragraph. If unset, the value is inherited from the parent.",
        default=None,
    )
    page_break_before: Optional[bool] = Field(
        description=(
            "Whether the current paragraph should always start at the beginning of a page. If unset, the value is",
            " inherited from the parent. Attempting to update pageBreakBefore for paragraphs in unsupported regio",
            "ns, including Table, Header, Footer and Footnote, can result in an invalid document state that retur",
            "ns a 400 bad request error.",
        ),
        default=None,
    )


class PositionedObjectPropertiesSuggestionState(BaseModel):
    """
    A mask that indicates which of the fields on the base PositionedObjectProperties have been changed in this suggestion. For any field set to true, there's a new suggested value.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#positionedobjectpropertiessuggestionstate
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    positioning_suggestion_state: Optional[
        PositionedObjectPositioningSuggestionState
    ] = Field(
        description="A mask that indicates which of the fields in positioning have been changed in this suggestion.",
        default=None,
    )
    embedded_object_suggestion_state: Optional[EmbeddedObjectSuggestionState] = Field(
        description="A mask that indicates which of the fields in embeddedObject have been changed in this suggestion.",
        default=None,
    )


class SectionBreak(BaseModel):
    """
    A StructuralElement representing a section break. A section is a range of content that has the same SectionStyle. A section break represents the start of a new section, and the section style applies to the section after the section break.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#sectionbreak
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    suggested_insertion_ids: Optional[list[str]] = Field(
        description=(
            "The suggested insertion IDs. A SectionBreak may have multiple insertion IDs if it's a nested suggest",
            "ed change. If empty, then this is not a suggested insertion.",
        ),
        default=None,
    )
    suggested_deletion_ids: Optional[str] = Field(
        description="The suggested deletion IDs. If empty, then there are no suggested deletions of this content.",
        default=None,
    )
    section_style: Optional[list[SectionStyle]] = Field(
        description="The style of the section after this section break.",
        default=None,
    )


class SuggestedBullet(BaseModel):
    """
    A suggested change to a Bullet.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#suggestedbullet
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    bullet: Optional[Bullet] = Field(
        description=(
            "A Bullet that only includes the changes made in this suggestion. This can be used along with the bul",
            "letSuggestionState to see which fields have changed and their new values.",
        ),
        default=None,
    )
    bullet_suggestion_state: Optional[BulletSuggestionState] = Field(
        description="A mask that indicates which of the fields on the base Bullet have been changed in this suggestion.",
        default=None,
    )


class SuggestedDocumentStyle(BaseModel):
    """
    A suggested change to the DocumentStyle.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#suggesteddocumentstyle
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    document_style: Optional[DocumentStyle] = Field(
        description=(
            "A DocumentStyle that only includes the changes made in this suggestion. This can be used along with ",
            "the documentStyleSuggestionState to see which fields have changed and their new values.",
        ),
        default=None,
    )
    document_style_suggestion_state: Optional[DocumentStyleSuggestionState] = Field(
        description=(
            "A mask that indicates which of the fields on the base DocumentStyle have been changed in this sugges",
            "tion.",
        ),
        default=None,
    )


class SuggestedParagraphStyle(BaseModel):
    """
    A suggested change to a ParagraphStyle.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#suggestedparagraphstyle
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    paragraph_style: Optional[ParagraphStyle] = Field(
        description=(
            "A ParagraphStyle that only includes the changes made in this suggestion. This can be used along with",
            " the paragraphStyleSuggestionState to see which fields have changed and their new values.",
        ),
        default=None,
    )
    paragraph_style_suggestion_state: Optional[ParagraphStyleSuggestionState] = Field(
        description=(
            "A mask that indicates which of the fields on the base ParagraphStyle have been changed in this sugge",
            "stion.",
        ),
        default=None,
    )


class SuggestedTableCellStyle(BaseModel):
    """
    A suggested change to a TableCellStyle.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#suggestedtablecellstyle
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    table_cell_style: Optional[TableCellStyle] = Field(
        description=(
            "A TableCellStyle that only includes the changes made in this suggestion. This can be used along with",
            " the tableCellStyleSuggestionState to see which fields have changed and their new values.",
        ),
        default=None,
    )
    table_cell_style_suggestion_state: Optional[TableCellStyleSuggestionState] = Field(
        description=(
            "A mask that indicates which of the fields on the base TableCellStyle have been changed in this sugge",
            "stion.",
        ),
        default=None,
    )


class SuggestedTableRowStyle(BaseModel):
    """
    A suggested change to a TableRowStyle.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#suggestedtablerowstyle
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    table_row_style: Optional[TableRowStyle] = Field(
        description=(
            "A TableRowStyle that only includes the changes made in this suggestion. This can be used along with ",
            "the tableRowStyleSuggestionState to see which fields have changed and their new values.",
        ),
        default=None,
    )
    table_row_style_suggestion_state: Optional[TableRowStyleSuggestionState] = Field(
        description=(
            "A mask that indicates which of the fields on the base TableRowStyle have been changed in this sugges",
            "tion.",
        ),
        default=None,
    )


class SuggestedTextStyle(BaseModel):
    """
    A suggested change to a TextStyle.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#suggestedtextstyle
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    text_style: Optional[TextStyle] = Field(
        description=(
            "A TextStyle that only includes the changes made in this suggestion. This can be used along with the ",
            "textStyleSuggestionState to see which fields have changed and their new values.",
        ),
        default=None,
    )
    text_style_suggestion_state: Optional[TextStyleSuggestionState] = Field(
        description=(
            "A mask that indicates which of the fields on the base TextStyle have been changed in this suggestion",
            ".",
        ),
        default=None,
    )


class TextRun(BaseModel):
    """
    A ParagraphElement that represents a run of text that all has the same styling.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#textrun
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    content: Optional[list[str]] = Field(
        description=(
            "The text of this run. Any non-text elements in the run are replaced with the Unicode character U+E90",
            "7.",
        ),
        default=None,
    )
    suggested_insertion_ids: Optional[list[str]] = Field(
        description=(
            "The suggested insertion IDs. A TextRun may have multiple insertion IDs if it's a nested suggested ch",
            "ange. If empty, then this is not a suggested insertion.",
        ),
        default=None,
    )
    suggested_deletion_ids: Optional[str] = Field(
        description="The suggested deletion IDs. If empty, then there are no suggested deletions of this content.",
        default=None,
    )
    text_style: Optional[TextStyle] = Field(
        description="The text style of this run.",
        default=None,
    )
    suggested_text_style_changes: Optional[dict[str, SuggestedTextStyle]] = Field(
        description="The suggested text style changes to this run, keyed by suggestion ID.",
        default=None,
    )


class AutoText(BaseModel):
    """
    A ParagraphElement representing a spot in the text that's dynamically replaced with content that can change over time, like a page number.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#autotext
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    type: Type = Field(
        description="The type of this auto text.",
        default=None,
    )
    suggested_insertion_ids: Optional[list[str]] = Field(
        description=(
            "The suggested insertion IDs. An AutoText may have multiple insertion IDs if it's a nested suggested ",
            "change. If empty, then this is not a suggested insertion.",
        ),
        default=None,
    )
    suggested_deletion_ids: Optional[str] = Field(
        description="The suggested deletion IDs. If empty, then there are no suggested deletions of this content.",
        default=None,
    )
    text_style: Optional[TextStyle] = Field(
        description="The text style of this AutoText.",
        default=None,
    )
    suggested_text_style_changes: Optional[dict[str, SuggestedTextStyle]] = Field(
        description="The suggested text style changes to this AutoText, keyed by suggestion ID.",
        default=None,
    )


class ColumnBreak(BaseModel):
    """
    A ParagraphElement representing a column break. A column break makes the subsequent text start at the top of the next column.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#columnbreak
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    suggested_insertion_ids: Optional[list[str]] = Field(
        description=(
            "The suggested insertion IDs. A ColumnBreak may have multiple insertion IDs if it's a nested suggeste",
            "d change. If empty, then this is not a suggested insertion.",
        ),
        default=None,
    )
    suggested_deletion_ids: Optional[str] = Field(
        description="The suggested deletion IDs. If empty, then there are no suggested deletions of this content.",
        default=None,
    )
    text_style: Optional[TextStyle] = Field(
        description=(
            "The text style of this ColumnBreak. Similar to text content, like text runs and footnote references,",
            " the text style of a column break can affect content layout as well as the styling of text inserted ",
            "next to it.",
        ),
        default=None,
    )
    suggested_text_style_changes: Optional[dict[str, SuggestedTextStyle]] = Field(
        description="The suggested text style changes to this ColumnBreak, keyed by suggestion ID.",
        default=None,
    )


class EmbeddedObject(BaseModel):
    """
    An embedded object in the document.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#embeddedobject
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    title: Optional[str] = Field(
        description="The title of the embedded object. The title and description are both combined to display alt text.",
        default=None,
    )
    description: Optional[str] = Field(
        description=(
            "The description of the embedded object. The title and description are both combined to display alt t",
            "ext.",
        ),
        default=None,
    )
    embedded_object_border: Optional[EmbeddedObjectBorder] = Field(
        description="The border of the embedded object.",
        default=None,
    )
    size: Optional[Size] = Field(
        description="The visible size of the image after cropping.",
        default=None,
    )
    margin_top: Optional[Dimension] = Field(
        description="The top margin of the embedded object.",
        default=None,
    )
    margin_bottom: Optional[Dimension] = Field(
        description="The bottom margin of the embedded object.",
        default=None,
    )
    margin_right: Optional[Dimension] = Field(
        description="The right margin of the embedded object.",
        default=None,
    )
    margin_left: Optional[Dimension] = Field(
        description="The left margin of the embedded object.",
        default=None,
    )
    linked_content_reference: Optional[LinkedContentReference] = Field(
        description=(
            "A reference to the external linked source content. For example, it contains a reference to the sourc",
            "e Google Sheets chart when the embedded object is a linked chart. If unset, then the embedded object",
            " is not linked.",
        ),
        default=None,
    )
    embedded_drawing_properties: Optional[EmbeddedDrawingProperties] = Field(
        description="The properties of an embedded drawing.",
        default=None,
    )
    image_properties: Optional[ImageProperties] = Field(
        description="The properties of an image.",
        default=None,
    )


class FootnoteReference(BaseModel):
    """
    A ParagraphElement representing a footnote reference. A footnote reference is the inline content rendered with a number and is used to identify the footnote.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#footnotereference
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    footnote_id: Optional[str] = Field(
        description="The ID of the footnote that contains the content of this footnote reference.",
        default=None,
    )
    footnote_number: Optional[list[str]] = Field(
        description="The rendered number of this footnote.",
        default=None,
    )
    suggested_insertion_ids: Optional[list[str]] = Field(
        description=(
            "The suggested insertion IDs. A FootnoteReference may have multiple insertion IDs if it's a nested su",
            "ggested change. If empty, then this is not a suggested insertion.",
        ),
        default=None,
    )
    suggested_deletion_ids: Optional[str] = Field(
        description="The suggested deletion IDs. If empty, then there are no suggested deletions of this content.",
        default=None,
    )
    text_style: Optional[TextStyle] = Field(
        description="The text style of this FootnoteReference.",
        default=None,
    )
    suggested_text_style_changes: Optional[list[dict[str, SuggestedTextStyle]]] = Field(
        description="The suggested text style changes to this FootnoteReference, keyed by suggestion ID.",
        default=None,
    )


class HorizontalRule(BaseModel):
    """
    A ParagraphElement representing a horizontal line.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#horizontalrule
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    suggested_insertion_ids: Optional[list[str]] = Field(
        description=(
            "The suggested insertion IDs. A HorizontalRule may have multiple insertion IDs if it is a nested sugg",
            "ested change. If empty, then this is not a suggested insertion.",
        ),
        default=None,
    )
    suggested_deletion_ids: Optional[str] = Field(
        description="The suggested deletion IDs. If empty, then there are no suggested deletions of this content.",
        default=None,
    )
    text_style: Optional[TextStyle] = Field(
        description=(
            "The text style of this HorizontalRule. Similar to text content, like text runs and footnote referenc",
            "es, the text style of a horizontal rule can affect content layout as well as the styling of text ins",
            "erted next to it.",
        ),
        default=None,
    )
    suggested_text_style_changes: Optional[list[dict[str, SuggestedTextStyle]]] = Field(
        description="The suggested text style changes to this HorizontalRule, keyed by suggestion ID.",
        default=None,
    )


class InlineObjectElement(BaseModel):
    """
    A ParagraphElement that contains an InlineObject.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#inlineobjectelement
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    inline_object_id: Optional[list[str]] = Field(
        description="The ID of the InlineObject this element contains.",
        default=None,
    )
    suggested_insertion_ids: Optional[list[str]] = Field(
        description=(
            "The suggested insertion IDs. An InlineObjectElement may have multiple insertion IDs if it's a nested",
            " suggested change. If empty, then this is not a suggested insertion.",
        ),
        default=None,
    )
    suggested_deletion_ids: Optional[str] = Field(
        description="The suggested deletion IDs. If empty, then there are no suggested deletions of this content.",
        default=None,
    )
    text_style: Optional[TextStyle] = Field(
        description=(
            "The text style of this InlineObjectElement. Similar to text content, like text runs and footnote ref",
            "erences, the text style of an inline object element can affect content layout as well as the styling",
            " of text inserted next to it.",
        ),
        default=None,
    )
    suggested_text_style_changes: Optional[dict[str, SuggestedTextStyle]] = Field(
        description="The suggested text style changes to this InlineObject, keyed by suggestion ID.",
        default=None,
    )


class InlineObjectProperties(BaseModel):
    """
    Properties of an InlineObject.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#inlineobjectproperties
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    embedded_object: Optional[EmbeddedObject] = Field(
        description="The embedded object of this inline object.",
        default=None,
    )


class ListProperties(BaseModel):
    """
    The properties of a list that describe the look and feel of bullets belonging to paragraphs associated with a list.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#listproperties
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    nesting_levels: Optional[NestingLevel] = Field(
        description=(
            "Describes the properties of the bullets at the associated level. A list has at most 9 levels of nest",
            "ing with nesting level 0 corresponding to the top-most level and nesting level 8 corresponding to th",
            "e most nested level. The nesting levels are returned in ascending order with the least nested return",
            "ed first.",
        ),
        default=None,
    )


class NamedStyle(BaseModel):
    """
    A named style. Paragraphs in the document can inherit their TextStyle and ParagraphStyle from this named style when they have the same named style type.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#namedstyle
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    named_style_type: NamedStyleType = Field(
        description="The type of this named style.",
        default=None,
    )
    text_style: Optional[TextStyle] = Field(
        description="The text style of this named style.",
        default=None,
    )
    paragraph_style: Optional[ParagraphStyle] = Field(
        description="The paragraph style of this named style.",
        default=None,
    )


class NamedStyles(BaseModel):
    """
    The named styles. Paragraphs in the document can inherit their TextStyle and ParagraphStyle from these named styles.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#namedstyles
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    styles: Optional[NamedStyle] = Field(
        description="The named styles. There's an entry for each of the possible named style types.",
        default=None,
    )


class PageBreak(BaseModel):
    """
    A ParagraphElement representing a page break. A page break makes the subsequent text start at the top of the next page.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#pagebreak
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    suggested_insertion_ids: Optional[list[str]] = Field(
        description=(
            "The suggested insertion IDs. A PageBreak may have multiple insertion IDs if it's a nested suggested ",
            "change. If empty, then this is not a suggested insertion.",
        ),
        default=None,
    )
    suggested_deletion_ids: Optional[str] = Field(
        description="The suggested deletion IDs. If empty, then there are no suggested deletions of this content.",
        default=None,
    )
    text_style: Optional[TextStyle] = Field(
        description=(
            "The text style of this PageBreak. Similar to text content, like text runs and footnote references, t",
            "he text style of a page break can affect content layout as well as the styling of text inserted next",
            " to it.",
        ),
        default=None,
    )
    suggested_text_style_changes: Optional[list[dict[str, SuggestedTextStyle]]] = Field(
        description="The suggested text style changes to this PageBreak, keyed by suggestion ID.",
        default=None,
    )


class Person(BaseModel):
    """
    A person or email address mentioned in a document. These mentions behave as a single, immutable element containing the person's name or email address.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#person
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    person_id: Optional[list[str]] = Field(
        description="Output only. The unique ID of this link.",
        default=None,
    )
    suggested_insertion_ids: Optional[list[str]] = Field(
        description=(
            "IDs for suggestions that insert this person link into the document. A Person might have multiple ins",
            "ertion IDs if it's a nested suggested change (a suggestion within a suggestion made by a different u",
            "ser, for example). If empty, then this person link isn't a suggested insertion.",
        ),
        default=None,
    )
    suggested_deletion_ids: Optional[str] = Field(
        description=(
            "IDs for suggestions that remove this person link from the document. A Person might have multiple del",
            "etion IDs if, for example, multiple users suggest deleting it. If empty, then this person link isn't",
            " suggested for deletion.",
        ),
        default=None,
    )
    text_style: Optional[TextStyle] = Field(
        description="The text style of this Person.",
        default=None,
    )
    suggested_text_style_changes: Optional[dict[str, SuggestedTextStyle]] = Field(
        description="The suggested text style changes to this Person, keyed by suggestion ID.",
        default=None,
    )
    person_properties: Optional[PersonProperties] = Field(
        description="Output only. The properties of this Person. This field is always present.",
        default=None,
    )


class PositionedObjectProperties(BaseModel):
    """
    Properties of a PositionedObject.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#positionedobjectproperties
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    positioning: Optional[PositionedObjectPositioning] = Field(
        description=(
            "The positioning of this positioned object relative to the newline of the Paragraph that references t",
            "his positioned object.",
        ),
        default=None,
    )
    embedded_object: Optional[EmbeddedObject] = Field(
        description="The embedded object of this positioned object.",
        default=None,
    )


class RichLink(BaseModel):
    """
    A link to a Google resource (such as a file in Drive, a YouTube video, or a Calendar event).
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#richlink
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    rich_link_id: Optional[list[str]] = Field(
        description="Output only. The ID of this link.",
        default=None,
    )
    suggested_insertion_ids: Optional[list[str]] = Field(
        description=(
            "IDs for suggestions that insert this link into the document. A RichLink might have multiple insertio",
            "n IDs if it's a nested suggested change (a suggestion within a suggestion made by a different user, ",
            "for example). If empty, then this person link isn't a suggested insertion.",
        ),
        default=None,
    )
    suggested_deletion_ids: Optional[str] = Field(
        description=(
            "IDs for suggestions that remove this link from the document. A RichLink might have multiple deletion",
            " IDs if, for example, multiple users suggest deleting it. If empty, then this person link isn't sugg",
            "ested for deletion.",
        ),
        default=None,
    )
    text_style: Optional[TextStyle] = Field(
        description="The text style of this RichLink.",
        default=None,
    )
    suggested_text_style_changes: Optional[dict[str, SuggestedTextStyle]] = Field(
        description="The suggested text style changes to this RichLink, keyed by suggestion ID.",
        default=None,
    )
    rich_link_properties: Optional[RichLinkProperties] = Field(
        description="Output only. The properties of this RichLink. This field is always present.",
        default=None,
    )


class SuggestedInlineObjectProperties(BaseModel):
    """
    A suggested change to InlineObjectProperties.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#suggestedinlineobjectproperties
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    inline_object_properties: Optional[InlineObjectProperties] = Field(
        description=(
            "An InlineObjectProperties that only includes the changes made in this suggestion. This can be used a",
            "long with the inlineObjectPropertiesSuggestionState to see which fields have changed and their new v",
            "alues.",
        ),
        default=None,
    )
    inline_object_properties_suggestion_state: Optional[
        InlineObjectPropertiesSuggestionState
    ] = Field(
        description=(
            "A mask that indicates which of the fields on the base InlineObjectProperties have been changed in th",
            "is suggestion.",
        ),
        default=None,
    )


class SuggestedListProperties(BaseModel):
    """
    A suggested change to ListProperties.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#suggestedlistproperties
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    list_properties: Optional[ListProperties] = Field(
        description=(
            "A ListProperties that only includes the changes made in this suggestion. This can be used along with",
            " the listPropertiesSuggestionState to see which fields have changed and their new values.",
        ),
        default=None,
    )
    list_properties_suggestion_state: Optional[list[ListPropertiesSuggestionState]] = (
        Field(
            description=(
                "A mask that indicates which of the fields on the base ListProperties have been changed in this sugge",
                "stion.",
            ),
            default=None,
        )
    )


class SuggestedNamedStyles(BaseModel):
    """
    A suggested change to the NamedStyles.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#suggestednamedstyles
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    named_styles: Optional[NamedStyles] = Field(
        description=(
            "A NamedStyles that only includes the changes made in this suggestion. This can be used along with th",
            "e namedStylesSuggestionState to see which fields have changed and their new values.",
        ),
        default=None,
    )
    named_styles_suggestion_state: Optional[list[NamedStylesSuggestionState]] = Field(
        description=(
            "A mask that indicates which of the fields on the base NamedStyles have been changed in this suggesti",
            "on.",
        ),
        default=None,
    )


class SuggestedPositionedObjectProperties(BaseModel):
    """
    A suggested change to PositionedObjectProperties.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#suggestedpositionedobjectproperties
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    positioned_object_properties: Optional[PositionedObjectProperties] = Field(
        description=(
            "A PositionedObjectProperties that only includes the changes made in this suggestion. This can be use",
            "d along with the positionedObjectPropertiesSuggestionState to see which fields have changed and thei",
            "r new values.",
        ),
        default=None,
    )
    positioned_object_properties_suggestion_state: Optional[
        PositionedObjectPropertiesSuggestionState
    ] = Field(
        description=(
            "A mask that indicates which of the fields on the base PositionedObjectProperties have been changed i",
            "n this suggestion.",
        ),
        default=None,
    )


class InlineObject(BaseModel):
    """
    An object that appears inline with text. An InlineObject contains an EmbeddedObject such as an image.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#inlineobject
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    object_id: Optional[str] = Field(
        description="The ID of this inline object. Can be used to update an object’s properties.",
        default=None,
    )
    inline_object_properties: Optional[InlineObjectProperties] = Field(
        description="The properties of this inline object.",
        default=None,
    )
    suggested_inline_object_properties_changes: Optional[
        dict[str, SuggestedInlineObjectProperties]
    ] = Field(
        description="The suggested changes to the inline object properties, keyed by suggestion ID.",
        default=None,
    )
    suggested_insertion_id: Optional[list[str]] = Field(
        description="The suggested insertion ID. If empty, then this is not a suggested insertion.",
        default=None,
    )
    suggested_deletion_ids: Optional[str] = Field(
        description="The suggested deletion IDs. If empty, then there are no suggested deletions of this content.",
        default=None,
    )


class List(BaseModel):
    """
    A List represents the list attributes for a group of paragraphs that all belong to the same list. A paragraph that's part of a list has a reference to the list's ID in its bullet.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#list
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    list_properties: Optional[ListProperties] = Field(
        description="The properties of the list.",
        default=None,
    )
    suggested_list_properties_changes: Optional[dict[str, SuggestedListProperties]] = (
        Field(
            description="The suggested changes to the list properties, keyed by suggestion ID.",
            default=None,
        )
    )
    suggested_insertion_id: Optional[list[str]] = Field(
        description="The suggested insertion ID. If empty, then this is not a suggested insertion.",
        default=None,
    )
    suggested_deletion_ids: Optional[list[str]] = Field(
        description="The suggested deletion IDs. If empty, then there are no suggested deletions of this list.",
        default=None,
    )


class ParagraphElement(BaseModel):
    """
    A ParagraphElement describes content within a Paragraph.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#paragraphelement
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    start_index: Optional[int] = Field(
        description="The zero-based start index of this paragraph element, in UTF-16 code units.",
        default=None,
    )
    end_index: Optional[int] = Field(
        description="The zero-base end index of this paragraph element, exclusive, in UTF-16 code units.",
        default=None,
    )
    text_run: Optional[TextRun] = Field(
        description="A text run paragraph element.",
        default=None,
    )
    auto_text: Optional[AutoText] = Field(
        description="An auto text paragraph element.",
        default=None,
    )
    page_break: Optional[PageBreak] = Field(
        description="A page break paragraph element.",
        default=None,
    )
    column_break: Optional[ColumnBreak] = Field(
        description="A column break paragraph element.",
        default=None,
    )
    footnote_reference: Optional[FootnoteReference] = Field(
        description="A footnote reference paragraph element.",
        default=None,
    )
    horizontal_rule: Optional[HorizontalRule] = Field(
        description="A horizontal rule paragraph element.",
        default=None,
    )
    equation: Optional[Equation] = Field(
        description="An equation paragraph element.",
        default=None,
    )
    inline_object_element: Optional[InlineObjectElement] = Field(
        description="An inline object paragraph element.",
        default=None,
    )
    person: Optional[Person] = Field(
        description="A paragraph element that links to a person or email address.",
        default=None,
    )
    rich_link: Optional[RichLink] = Field(
        description=(
            "A paragraph element that links to a Google resource (such as a file in Google Drive, a YouTube video",
            ", or a Calendar event.)",
        ),
        default=None,
    )


class PositionedObject(BaseModel):
    """
    An object that's tethered to a Paragraph and positioned relative to the beginning of the paragraph. A PositionedObject contains an EmbeddedObject such as an image.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#positionedobject
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    object_id: Optional[str] = Field(
        description="The ID of this positioned object.",
        default=None,
    )
    positioned_object_properties: Optional[PositionedObjectProperties] = Field(
        description="The properties of this positioned object.",
        default=None,
    )
    suggested_positioned_object_properties_changes: Optional[
        dict[str, SuggestedPositionedObjectProperties]
    ] = Field(
        description="The suggested changes to the positioned object properties, keyed by suggestion ID.",
        default=None,
    )
    suggested_insertion_id: Optional[list[str]] = Field(
        description="The suggested insertion ID. If empty, then this is not a suggested insertion.",
        default=None,
    )
    suggested_deletion_ids: Optional[str] = Field(
        description="The suggested deletion IDs. If empty, then there are no suggested deletions of this content.",
        default=None,
    )


class Paragraph(BaseModel):
    """
    A StructuralElement representing a paragraph. A paragraph is a range of content that's terminated with a newline character.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#paragraph
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    elements: Optional[ParagraphElement] = Field(
        description="The content of the paragraph, broken down into its component parts.",
        default=None,
    )
    paragraph_style: Optional[ParagraphStyle] = Field(
        description="The style of this paragraph.",
        default=None,
    )
    suggested_paragraph_style_changes: Optional[dict[str, SuggestedParagraphStyle]] = (
        Field(
            description="The suggested paragraph style changes to this paragraph, keyed by suggestion ID.",
            default=None,
        )
    )
    bullet: Optional[Bullet] = Field(
        description="The bullet for this paragraph. If not present, the paragraph does not belong to a list.",
        default=None,
    )
    suggested_bullet_changes: Optional[list[dict[str, SuggestedBullet]]] = Field(
        description="The suggested changes to this paragraph's bullet.",
        default=None,
    )
    positioned_object_ids: Optional[str] = Field(
        description="The IDs of the positioned objects tethered to this paragraph.",
        default=None,
    )
    suggested_positioned_object_ids: Optional[dict[str, ObjectReferences]] = Field(
        description=(
            "The IDs of the positioned objects suggested to be attached to this paragraph, keyed by suggestion ID",
            ".",
        ),
        default=None,
    )


class Body(BaseModel):
    """
    The document body.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#body
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    content: Optional[StructuralElement] = Field(
        description="The contents of the body. The indexes for the body's content begin at zero.",
        default=None,
    )


class Document(BaseModel):
    """
    A Google Docs document.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#resource:-document
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    document_id: Optional[str] = Field(
        description="Output only. The ID of the document.",
        default=None,
    )
    title: Optional[list[str]] = Field(
        description="The title of the document.",
        default=None,
    )
    tabs: Optional[Tab] = Field(
        description=(
            "Tabs that are part of a document. Tabs can contain child tabs, a tab nested within another tab. Chil",
            "d tabs are represented by the Tab.childTabs field.",
        ),
        default=None,
    )
    revision_id: Optional[str] = Field(
        description=(
            "Output only. The revision ID of the document. Can be used in update requests to specify which revisi",
            "on of a document to apply updates to and how the request should behave if the document has been edit",
            "ed since that revision. Only populated if the user has edit access to the document. The revision ID ",
            "is not a sequential number but an opaque string. The format of the revision ID might change over tim",
            "e. A returned revision ID is only guaranteed to be valid for 24 hours after it has been returned and",
            " cannot be shared across users. If the revision ID is unchanged between calls, then the document has",
            " not changed. Conversely, a changed ID (for the same document and user) usually means the document h",
            "as been updated. However, a changed ID can also be due to internal factors such as ID format changes",
            ".",
        ),
        default=None,
    )
    suggestions_view_mode: SuggestionsViewMode = Field(
        description=(
            "Output only. The suggestions view mode applied to the document. Note: When editing a document, chang",
            "es must be based on a document with SUGGESTIONS_INLINE.",
        ),
        default=None,
    )
    body: Optional[Body] = Field(
        description=(
            "Output only. The main body of the document. Legacy field: Instead, use Document.tabs.documentTab.bod",
            "y, which exposes the actual document content from all tabs when the includeTabsContent parameter is ",
            "set to true. If false or unset, this field contains information about the first tab in the document.",
        ),
        default=None,
    )
    headers: Optional[dict[str, Header]] = Field(
        description=(
            "Output only. The headers in the document, keyed by header ID. Legacy field: Instead, use Document.ta",
            "bs.documentTab.headers, which exposes the actual document content from all tabs when the includeTabs",
            "Content parameter is set to true. If false or unset, this field contains information about the first",
            " tab in the document.",
        ),
        default=None,
    )
    footers: Optional[dict[str, Footer]] = Field(
        description=(
            "Output only. The footers in the document, keyed by footer ID. Legacy field: Instead, use Document.ta",
            "bs.documentTab.footers, which exposes the actual document content from all tabs when the includeTabs",
            "Content parameter is set to true. If false or unset, this field contains information about the first",
            " tab in the document.",
        ),
        default=None,
    )
    footnotes: Optional[dict[str, Footnote]] = Field(
        description=(
            "Output only. The footnotes in the document, keyed by footnote ID. Legacy field: Instead, use Documen",
            "t.tabs.documentTab.footnotes, which exposes the actual document content from all tabs when the inclu",
            "deTabsContent parameter is set to true. If false or unset, this field contains information about the",
            " first tab in the document.",
        ),
        default=None,
    )
    document_style: Optional[DocumentStyle] = Field(
        description=(
            "Output only. The style of the document. Legacy field: Instead, use Document.tabs.documentTab.documen",
            "tStyle, which exposes the actual document content from all tabs when the includeTabsContent paramete",
            "r is set to true. If false or unset, this field contains information about the first tab in the docu",
            "ment.",
        ),
        default=None,
    )
    suggested_document_style_changes: Optional[dict[str, SuggestedDocumentStyle]] = (
        Field(
            description=(
                "Output only. The suggested changes to the style of the document, keyed by suggestion ID. Legacy fiel",
                "d: Instead, use Document.tabs.documentTab.suggestedDocumentStyleChanges, which exposes the actual do",
                "cument content from all tabs when the includeTabsContent parameter is set to true. If false or unset",
                ", this field contains information about the first tab in the document.",
            ),
            default=None,
        )
    )
    named_styles: Optional[NamedStyles] = Field(
        description=(
            "Output only. The named styles of the document. Legacy field: Instead, use Document.tabs.documentTab.",
            "namedStyles, which exposes the actual document content from all tabs when the includeTabsContent par",
            "ameter is set to true. If false or unset, this field contains information about the first tab in the",
            " document.",
        ),
        default=None,
    )
    suggested_named_styles_changes: Optional[dict[str, SuggestedNamedStyles]] = Field(
        description=(
            "Output only. The suggested changes to the named styles of the document, keyed by suggestion ID. Lega",
            "cy field: Instead, use Document.tabs.documentTab.suggestedNamedStylesChanges, which exposes the actu",
            "al document content from all tabs when the includeTabsContent parameter is set to true. If false or ",
            "unset, this field contains information about the first tab in the document.",
        ),
        default=None,
    )
    lists: Optional[dict[str, List]] = Field(
        description=(
            "Output only. The lists in the document, keyed by list ID. Legacy field: Instead, use Document.tabs.d",
            "ocumentTab.lists, which exposes the actual document content from all tabs when the includeTabsConten",
            "t parameter is set to true. If false or unset, this field contains information about the first tab i",
            "n the document.",
        ),
        default=None,
    )
    named_ranges: Optional[dict[str, NamedRanges]] = Field(
        description=(
            "Output only. The named ranges in the document, keyed by name. Legacy field: Instead, use Document.ta",
            "bs.documentTab.namedRanges, which exposes the actual document content from all tabs when the include",
            "TabsContent parameter is set to true. If false or unset, this field contains information about the f",
            "irst tab in the document.",
        ),
        default=None,
    )
    inline_objects: Optional[dict[str, InlineObject]] = Field(
        description=(
            "Output only. The inline objects in the document, keyed by object ID. Legacy field: Instead, use Docu",
            "ment.tabs.documentTab.inlineObjects, which exposes the actual document content from all tabs when th",
            "e includeTabsContent parameter is set to true. If false or unset, this field contains information ab",
            "out the first tab in the document.",
        ),
        default=None,
    )
    positioned_objects: Optional[dict[str, PositionedObject]] = Field(
        description=(
            "Output only. The positioned objects in the document, keyed by object ID. Legacy field: Instead, use ",
            "Document.tabs.documentTab.positionedObjects, which exposes the actual document content from all tabs",
            " when the includeTabsContent parameter is set to true. If false or unset, this field contains inform",
            "ation about the first tab in the document.",
        ),
        default=None,
    )


class DocumentTab(BaseModel):
    """
    A tab with document contents.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#documenttab
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    body: Optional[Body] = Field(
        description="The main body of the document tab.",
        default=None,
    )
    headers: Optional[dict[str, Header]] = Field(
        description="The headers in the document tab, keyed by header ID.",
        default=None,
    )
    footers: Optional[dict[str, Footer]] = Field(
        description="The footers in the document tab, keyed by footer ID.",
        default=None,
    )
    footnotes: Optional[dict[str, Footnote]] = Field(
        description="The footnotes in the document tab, keyed by footnote ID.",
        default=None,
    )
    document_style: Optional[DocumentStyle] = Field(
        description="The style of the document tab.",
        default=None,
    )
    suggested_document_style_changes: Optional[dict[str, SuggestedDocumentStyle]] = (
        Field(
            description="The suggested changes to the style of the document tab, keyed by suggestion ID.",
            default=None,
        )
    )
    named_styles: Optional[NamedStyles] = Field(
        description="The named styles of the document tab.",
        default=None,
    )
    suggested_named_styles_changes: Optional[dict[str, SuggestedNamedStyles]] = Field(
        description="The suggested changes to the named styles of the document tab, keyed by suggestion ID.",
        default=None,
    )
    lists: Optional[dict[str, List]] = Field(
        description="The lists in the document tab, keyed by list ID.",
        default=None,
    )
    named_ranges: Optional[dict[str, NamedRanges]] = Field(
        description="The named ranges in the document tab, keyed by name.",
        default=None,
    )
    inline_objects: Optional[dict[str, InlineObject]] = Field(
        description="The inline objects in the document tab, keyed by object ID.",
        default=None,
    )
    positioned_objects: Optional[list[dict[str, PositionedObject]]] = Field(
        description="The positioned objects in the document tab, keyed by object ID.",
        default=None,
    )


class Footer(BaseModel):
    """
    A document footer.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#footer
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    footer_id: Optional[list[str]] = Field(
        description="The ID of the footer.",
        default=None,
    )
    content: Optional[StructuralElement] = Field(
        description="The contents of the footer. The indexes for a footer's content begin at zero.",
        default=None,
    )


class Footnote(BaseModel):
    """
    A document footnote.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#footnote
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    footnote_id: Optional[list[str]] = Field(
        description="The ID of the footnote.",
        default=None,
    )
    content: Optional[StructuralElement] = Field(
        description="The contents of the footnote. The indexes for a footnote's content begin at zero.",
        default=None,
    )


class Header(BaseModel):
    """
    A document header.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#header
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    header_id: Optional[list[str]] = Field(
        description="The ID of the header.",
        default=None,
    )
    content: Optional[StructuralElement] = Field(
        description="The contents of the header. The indexes for a header's content begin at zero.",
        default=None,
    )


class StructuralElement(BaseModel):
    """
    A StructuralElement describes content that provides structure to the document.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#structuralelement
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    start_index: Optional[int] = Field(
        description="The zero-based start index of this structural element, in UTF-16 code units.",
        default=None,
    )
    end_index: Optional[int] = Field(
        description="The zero-based end index of this structural element, exclusive, in UTF-16 code units.",
        default=None,
    )
    paragraph: Optional[Paragraph] = Field(
        description="A paragraph type of structural element.",
        default=None,
    )
    section_break: Optional[SectionBreak] = Field(
        description="A section break type of structural element.",
        default=None,
    )
    table: Optional[Table] = Field(
        description="A table type of structural element.",
        default=None,
    )
    table_of_contents: Optional[list[TableOfContents]] = Field(
        description="A table of contents type of structural element.",
        default=None,
    )


class TableCell(BaseModel):
    """
    The contents and style of a cell in a Table.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#tablecell
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    start_index: Optional[int] = Field(
        description="The zero-based start index of this cell, in UTF-16 code units.",
        default=None,
    )
    end_index: Optional[list[int]] = Field(
        description="The zero-based end index of this cell, exclusive, in UTF-16 code units.",
        default=None,
    )
    content: Optional[StructuralElement] = Field(
        description="The content of the cell.",
        default=None,
    )
    table_cell_style: Optional[list[TableCellStyle]] = Field(
        description="The style of the cell.",
        default=None,
    )
    suggested_insertion_ids: Optional[list[str]] = Field(
        description=(
            "The suggested insertion IDs. A TableCell may have multiple insertion IDs if it's a nested suggested ",
            "change. If empty, then this is not a suggested insertion.",
        ),
        default=None,
    )
    suggested_deletion_ids: Optional[str] = Field(
        description="The suggested deletion IDs. If empty, then there are no suggested deletions of this content.",
        default=None,
    )
    suggested_table_cell_style_changes: Optional[dict[str, SuggestedTableCellStyle]] = (
        Field(
            description="The suggested changes to the table cell style, keyed by suggestion ID.",
            default=None,
        )
    )


class TableOfContents(BaseModel):
    """
    A StructuralElement representing a table of contents.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#tableofcontents
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    content: Optional[list[StructuralElement]] = Field(
        description="The content of the table of contents.",
        default=None,
    )
    suggested_insertion_ids: Optional[list[str]] = Field(
        description=(
            "The suggested insertion IDs. A TableOfContents may have multiple insertion IDs if it is a nested sug",
            "gested change. If empty, then this is not a suggested insertion.",
        ),
        default=None,
    )
    suggested_deletion_ids: Optional[str] = Field(
        description="The suggested deletion IDs. If empty, then there are no suggested deletions of this content.",
        default=None,
    )


class TableRow(BaseModel):
    """
    The contents and style of a row in a Table.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#tablerow
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    start_index: Optional[int] = Field(
        description="The zero-based start index of this row, in UTF-16 code units.",
        default=None,
    )
    end_index: Optional[list[int]] = Field(
        description="The zero-based end index of this row, exclusive, in UTF-16 code units.",
        default=None,
    )
    table_cells: Optional[list[TableCell]] = Field(
        description=(
            "The contents and style of each cell in this row. It's possible for a table to be non-rectangular, so",
            " some rows may have a different number of cells than other rows in the same table.",
        ),
        default=None,
    )
    suggested_insertion_ids: Optional[list[str]] = Field(
        description=(
            "The suggested insertion IDs. A TableRow may have multiple insertion IDs if it's a nested suggested c",
            "hange. If empty, then this is not a suggested insertion.",
        ),
        default=None,
    )
    suggested_deletion_ids: Optional[str] = Field(
        description="The suggested deletion IDs. If empty, then there are no suggested deletions of this content.",
        default=None,
    )
    table_row_style: Optional[TableRowStyle] = Field(
        description="The style of the table row.",
        default=None,
    )
    suggested_table_row_style_changes: Optional[dict[str, SuggestedTableRowStyle]] = (
        Field(
            description="The suggested style changes to this row, keyed by suggestion ID.",
            default=None,
        )
    )


class Table(BaseModel):
    """
    A StructuralElement representing a table.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#table
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    rows: Optional[int] = Field(
        description="Number of rows in the table.",
        default=None,
    )
    columns: Optional[list[int]] = Field(
        description=(
            "Number of columns in the table. It's possible for a table to be non-rectangular, so some rows may ha",
            "ve a different number of cells.",
        ),
        default=None,
    )
    table_rows: Optional[list[TableRow]] = Field(
        description="The contents and style of each row.",
        default=None,
    )
    suggested_insertion_ids: Optional[list[str]] = Field(
        description=(
            "The suggested insertion IDs. A Table may have multiple insertion IDs if it's a nested suggested chan",
            "ge. If empty, then this is not a suggested insertion.",
        ),
        default=None,
    )
    suggested_deletion_ids: Optional[str] = Field(
        description="The suggested deletion IDs. If empty, then there are no suggested deletions of this content.",
        default=None,
    )
    table_style: Optional[TableStyle] = Field(
        description="The style of the table.",
        default=None,
    )


class Tab(BaseModel):
    """
    A tab in a document.
    https://developers.google.com/workspace/docs/api/reference/rest/v1/documents?hl=en#tab
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=alias_generators.to_camel,
    )

    tab_properties: Optional[list[TabProperties]] = Field(
        description="The properties of the tab, like ID and title.",
        default=None,
    )
    child_tabs: Optional[Tab] = Field(
        description="The child tabs nested within this tab.",
        default=None,
    )
    document_tab: Optional[DocumentTab] = Field(
        description="A tab with document contents, like text and images.",
        default=None,
    )
