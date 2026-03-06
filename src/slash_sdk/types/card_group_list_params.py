# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CardGroupListParams"]


class CardGroupListParams(TypedDict, total=False):
    cursor: str
    """A cursor string to fetch the next page of results"""

    filter_name: Annotated[str, PropertyInfo(alias="filter:name")]
    """Pass in a name to filter for card groups with a matching name."""

    filter_status: Annotated[Literal["active", "archived"], PropertyInfo(alias="filter:status")]
    """Filter card groups by status. Defaults to 'active' if not provided."""

    filter_virtual_account_id: Annotated[str, PropertyInfo(alias="filter:virtualAccountId")]
    """
    Pass in a virtual account ID to filter for card groups under a specific virtual
    account.
    """
