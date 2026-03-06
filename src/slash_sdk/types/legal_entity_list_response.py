# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .pagination_response import PaginationResponse

__all__ = ["LegalEntityListResponse", "Item"]


class Item(BaseModel):
    """
    A legal entity is an entity (either a person or a business) that can own accounts.
    If you are using the API with an API key, your API key will only be associated with one legal entity, so you will not need to specify the legal entity ID in most endpoints.
    If you are using the API with an OAuth2 access token, you can filter the results of most endpoints to only show data for a specific legal entity by specifying the legal entity ID in the URL.
    """

    id: str

    name: str

    structure: Optional[
        Literal["person", "llc", "lp", "llp", "gp", "partnership", "cooperative", "ccorp", "scorp", "other"]
    ] = None
    """
    Will be empty in rare cases where the legal entity has not yet been fully
    created.
    """


class LegalEntityListResponse(BaseModel):
    items: List[Item]

    metadata: PaginationResponse
    """Response sent when requesting a list of data"""
