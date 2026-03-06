# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["WebhookUpdateParams"]


class WebhookUpdateParams(TypedDict, total=False):
    status: Required[Literal["active", "paused", "archived"]]
    """The desired status for the endpoint:

    - `active`: Enable/re-enable the endpoint
    - `paused`: Pause the endpoint (notifications are queued)
    - `archived`: Archive the endpoint (soft delete)
    """

    reason: str
    """Optional reason for the status change (for audit purposes)"""
