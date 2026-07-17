# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Webhook"]


class Webhook(BaseModel):
    id: str

    created_at: str = FieldInfo(alias="createdAt")

    name: str
    """The name of the webhook"""

    status: Literal["active", "paused", "backing-off", "disabled"]
    """The current status of the webhook endpoint:

    - `active`: The webhook is enabled and receiving events normally.
    - `paused`: The webhook has been paused by the user. Events are queued and will
      be delivered when the endpoint is set back to `active`.
    - `backing-off`: The system is temporarily backing off due to delivery failures.
      Delivery will be automatically retried at `backingOffUntil`. You can also
      immediately re-enable by setting status to `active` via the PATCH endpoint.
    - `disabled`: The webhook has been automatically disabled due to repeated
      delivery failures. Re-enable by setting status to `active` via the PATCH
      endpoint.
    """

    url: str
    """The URL that will receive the webhook payload"""

    archived_at: Optional[str] = FieldInfo(alias="archivedAt", default=None)

    backing_off_until: Optional[str] = FieldInfo(alias="backingOffUntil", default=None)
    """When the system will automatically retry delivery (ISO 8601 timestamp).

    Only present when status is `backing-off`.
    """

    disabled_at: Optional[str] = FieldInfo(alias="disabledAt", default=None)
    """
    When the endpoint was automatically disabled due to repeated failures (ISO 8601
    timestamp). Only present when status is `disabled`.
    """

    enabled_events: Optional[List[str]] = FieldInfo(alias="enabledEvents", default=None)
    """Public webhook event types this endpoint receives. Omitted means all events."""

    paused_at: Optional[str] = FieldInfo(alias="pausedAt", default=None)
    """When the endpoint was paused by the user (ISO 8601 timestamp)"""
