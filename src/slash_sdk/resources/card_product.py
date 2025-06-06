# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import card_product_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.card_product_list_response import CardProductListResponse

__all__ = ["CardProductResource", "AsyncCardProductResource"]


class CardProductResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CardProductResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/slashfi/slash-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CardProductResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardProductResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/slashfi/slash-sdk-python#with_streaming_response
        """
        return CardProductResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardProductListResponse:
        """
        Get all card products

        Args:
          cursor: A cursor string to fetch the next page of results

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/card-product",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"cursor": cursor}, card_product_list_params.CardProductListParams),
            ),
            cast_to=CardProductListResponse,
        )


class AsyncCardProductResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCardProductResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/slashfi/slash-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCardProductResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardProductResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/slashfi/slash-sdk-python#with_streaming_response
        """
        return AsyncCardProductResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardProductListResponse:
        """
        Get all card products

        Args:
          cursor: A cursor string to fetch the next page of results

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/card-product",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"cursor": cursor}, card_product_list_params.CardProductListParams),
            ),
            cast_to=CardProductListResponse,
        )


class CardProductResourceWithRawResponse:
    def __init__(self, card_product: CardProductResource) -> None:
        self._card_product = card_product

        self.list = to_raw_response_wrapper(
            card_product.list,
        )


class AsyncCardProductResourceWithRawResponse:
    def __init__(self, card_product: AsyncCardProductResource) -> None:
        self._card_product = card_product

        self.list = async_to_raw_response_wrapper(
            card_product.list,
        )


class CardProductResourceWithStreamingResponse:
    def __init__(self, card_product: CardProductResource) -> None:
        self._card_product = card_product

        self.list = to_streamed_response_wrapper(
            card_product.list,
        )


class AsyncCardProductResourceWithStreamingResponse:
    def __init__(self, card_product: AsyncCardProductResource) -> None:
        self._card_product = card_product

        self.list = async_to_streamed_response_wrapper(
            card_product.list,
        )
