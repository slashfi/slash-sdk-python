# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AccountListParams"]


class AccountListParams(TypedDict, total=False):
    limit: str
    """The number of items to return (default 100, max 1000)"""

    offset: str
    """The number of items to skip before starting to collect the result set"""
