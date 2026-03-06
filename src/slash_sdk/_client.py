# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
import base64
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        fdx,
        pay,
        card,
        crypto,
        oauth2,
        account,
        webhook,
        merchant,
        transfer,
        card_group,
        well_known,
        transaction,
        card_product,
        legal_entity,
        slash_handle,
        virtual_account,
        developer_account,
        merchant_category,
        developer_application,
    )
    from .resources.pay import PayResource, AsyncPayResource
    from .resources.crypto import CryptoResource, AsyncCryptoResource
    from .resources.account import AccountResource, AsyncAccountResource
    from .resources.fdx.fdx import FdxResource, AsyncFdxResource
    from .resources.webhook import WebhookResource, AsyncWebhookResource
    from .resources.merchant import MerchantResource, AsyncMerchantResource
    from .resources.transfer import TransferResource, AsyncTransferResource
    from .resources.card.card import CardResource, AsyncCardResource
    from .resources.well_known import WellKnownResource, AsyncWellKnownResource
    from .resources.transaction import TransactionResource, AsyncTransactionResource
    from .resources.card_product import CardProductResource, AsyncCardProductResource
    from .resources.legal_entity import LegalEntityResource, AsyncLegalEntityResource
    from .resources.slash_handle import SlashHandleResource, AsyncSlashHandleResource
    from .resources.oauth2.oauth2 import Oauth2Resource, AsyncOauth2Resource
    from .resources.virtual_account import VirtualAccountResource, AsyncVirtualAccountResource
    from .resources.developer_account import DeveloperAccountResource, AsyncDeveloperAccountResource
    from .resources.merchant_category import MerchantCategoryResource, AsyncMerchantCategoryResource
    from .resources.card_group.card_group import CardGroupResource, AsyncCardGroupResource
    from .resources.developer_application import DeveloperApplicationResource, AsyncDeveloperApplicationResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "SlashSDK",
    "AsyncSlashSDK",
    "Client",
    "AsyncClient",
]


class SlashSDK(SyncAPIClient):
    # client options
    api_key: str | None
    bearer_token: str | None
    username: str | None
    password: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous SlashSDK client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `SLASH_SDK_API_KEY`
        - `bearer_token` from `SLASH_SDK_BEARER_TOKEN`
        - `username` from `SLASH_SDK_USERNAME`
        - `password` from `SLASH_SDK_PASSWORD`
        """
        if api_key is None:
            api_key = os.environ.get("SLASH_SDK_API_KEY")
        self.api_key = api_key

        if bearer_token is None:
            bearer_token = os.environ.get("SLASH_SDK_BEARER_TOKEN")
        self.bearer_token = bearer_token

        if username is None:
            username = os.environ.get("SLASH_SDK_USERNAME")
        self.username = username

        if password is None:
            password = os.environ.get("SLASH_SDK_PASSWORD")
        self.password = password

        if base_url is None:
            base_url = os.environ.get("SLASH_SDK_BASE_URL")
        if base_url is None:
            base_url = f"https://api.joinslash.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def legal_entity(self) -> LegalEntityResource:
        from .resources.legal_entity import LegalEntityResource

        return LegalEntityResource(self)

    @cached_property
    def account(self) -> AccountResource:
        from .resources.account import AccountResource

        return AccountResource(self)

    @cached_property
    def virtual_account(self) -> VirtualAccountResource:
        from .resources.virtual_account import VirtualAccountResource

        return VirtualAccountResource(self)

    @cached_property
    def transaction(self) -> TransactionResource:
        from .resources.transaction import TransactionResource

        return TransactionResource(self)

    @cached_property
    def transfer(self) -> TransferResource:
        from .resources.transfer import TransferResource

        return TransferResource(self)

    @cached_property
    def card(self) -> CardResource:
        from .resources.card import CardResource

        return CardResource(self)

    @cached_property
    def card_group(self) -> CardGroupResource:
        from .resources.card_group import CardGroupResource

        return CardGroupResource(self)

    @cached_property
    def card_product(self) -> CardProductResource:
        from .resources.card_product import CardProductResource

        return CardProductResource(self)

    @cached_property
    def slash_handle(self) -> SlashHandleResource:
        from .resources.slash_handle import SlashHandleResource

        return SlashHandleResource(self)

    @cached_property
    def pay(self) -> PayResource:
        from .resources.pay import PayResource

        return PayResource(self)

    @cached_property
    def webhook(self) -> WebhookResource:
        from .resources.webhook import WebhookResource

        return WebhookResource(self)

    @cached_property
    def merchant(self) -> MerchantResource:
        from .resources.merchant import MerchantResource

        return MerchantResource(self)

    @cached_property
    def merchant_category(self) -> MerchantCategoryResource:
        from .resources.merchant_category import MerchantCategoryResource

        return MerchantCategoryResource(self)

    @cached_property
    def developer_account(self) -> DeveloperAccountResource:
        from .resources.developer_account import DeveloperAccountResource

        return DeveloperAccountResource(self)

    @cached_property
    def developer_application(self) -> DeveloperApplicationResource:
        from .resources.developer_application import DeveloperApplicationResource

        return DeveloperApplicationResource(self)

    @cached_property
    def well_known(self) -> WellKnownResource:
        from .resources.well_known import WellKnownResource

        return WellKnownResource(self)

    @cached_property
    def oauth2(self) -> Oauth2Resource:
        from .resources.oauth2 import Oauth2Resource

        return Oauth2Resource(self)

    @cached_property
    def fdx(self) -> FdxResource:
        from .resources.fdx import FdxResource

        return FdxResource(self)

    @cached_property
    def crypto(self) -> CryptoResource:
        from .resources.crypto import CryptoResource

        return CryptoResource(self)

    @cached_property
    def with_raw_response(self) -> SlashSDKWithRawResponse:
        return SlashSDKWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SlashSDKWithStreamedResponse:
        return SlashSDKWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._api_key, **self._bearer, **self._developer_application}

    @property
    def _api_key(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"X-API-Key": api_key}

    @property
    def _bearer(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        if bearer_token is None:
            return {}
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    def _developer_application(self) -> dict[str, str]:
        if self.username is None:
            return {}
        if self.password is None:
            return {}
        credentials = f"{self.username}:{self.password}".encode("ascii")
        header = f"Basic {base64.b64encode(credentials).decode('ascii')}"
        return {"Authorization": header}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("X-API-Key") or isinstance(custom_headers.get("X-API-Key"), Omit):
            return

        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected one of api_key, bearer_token, username or password to be set. Or for one of the `X-API-Key`, `Authorization` or `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            bearer_token=bearer_token or self.bearer_token,
            username=username or self.username,
            password=password or self.password,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncSlashSDK(AsyncAPIClient):
    # client options
    api_key: str | None
    bearer_token: str | None
    username: str | None
    password: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncSlashSDK client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `SLASH_SDK_API_KEY`
        - `bearer_token` from `SLASH_SDK_BEARER_TOKEN`
        - `username` from `SLASH_SDK_USERNAME`
        - `password` from `SLASH_SDK_PASSWORD`
        """
        if api_key is None:
            api_key = os.environ.get("SLASH_SDK_API_KEY")
        self.api_key = api_key

        if bearer_token is None:
            bearer_token = os.environ.get("SLASH_SDK_BEARER_TOKEN")
        self.bearer_token = bearer_token

        if username is None:
            username = os.environ.get("SLASH_SDK_USERNAME")
        self.username = username

        if password is None:
            password = os.environ.get("SLASH_SDK_PASSWORD")
        self.password = password

        if base_url is None:
            base_url = os.environ.get("SLASH_SDK_BASE_URL")
        if base_url is None:
            base_url = f"https://api.joinslash.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def legal_entity(self) -> AsyncLegalEntityResource:
        from .resources.legal_entity import AsyncLegalEntityResource

        return AsyncLegalEntityResource(self)

    @cached_property
    def account(self) -> AsyncAccountResource:
        from .resources.account import AsyncAccountResource

        return AsyncAccountResource(self)

    @cached_property
    def virtual_account(self) -> AsyncVirtualAccountResource:
        from .resources.virtual_account import AsyncVirtualAccountResource

        return AsyncVirtualAccountResource(self)

    @cached_property
    def transaction(self) -> AsyncTransactionResource:
        from .resources.transaction import AsyncTransactionResource

        return AsyncTransactionResource(self)

    @cached_property
    def transfer(self) -> AsyncTransferResource:
        from .resources.transfer import AsyncTransferResource

        return AsyncTransferResource(self)

    @cached_property
    def card(self) -> AsyncCardResource:
        from .resources.card import AsyncCardResource

        return AsyncCardResource(self)

    @cached_property
    def card_group(self) -> AsyncCardGroupResource:
        from .resources.card_group import AsyncCardGroupResource

        return AsyncCardGroupResource(self)

    @cached_property
    def card_product(self) -> AsyncCardProductResource:
        from .resources.card_product import AsyncCardProductResource

        return AsyncCardProductResource(self)

    @cached_property
    def slash_handle(self) -> AsyncSlashHandleResource:
        from .resources.slash_handle import AsyncSlashHandleResource

        return AsyncSlashHandleResource(self)

    @cached_property
    def pay(self) -> AsyncPayResource:
        from .resources.pay import AsyncPayResource

        return AsyncPayResource(self)

    @cached_property
    def webhook(self) -> AsyncWebhookResource:
        from .resources.webhook import AsyncWebhookResource

        return AsyncWebhookResource(self)

    @cached_property
    def merchant(self) -> AsyncMerchantResource:
        from .resources.merchant import AsyncMerchantResource

        return AsyncMerchantResource(self)

    @cached_property
    def merchant_category(self) -> AsyncMerchantCategoryResource:
        from .resources.merchant_category import AsyncMerchantCategoryResource

        return AsyncMerchantCategoryResource(self)

    @cached_property
    def developer_account(self) -> AsyncDeveloperAccountResource:
        from .resources.developer_account import AsyncDeveloperAccountResource

        return AsyncDeveloperAccountResource(self)

    @cached_property
    def developer_application(self) -> AsyncDeveloperApplicationResource:
        from .resources.developer_application import AsyncDeveloperApplicationResource

        return AsyncDeveloperApplicationResource(self)

    @cached_property
    def well_known(self) -> AsyncWellKnownResource:
        from .resources.well_known import AsyncWellKnownResource

        return AsyncWellKnownResource(self)

    @cached_property
    def oauth2(self) -> AsyncOauth2Resource:
        from .resources.oauth2 import AsyncOauth2Resource

        return AsyncOauth2Resource(self)

    @cached_property
    def fdx(self) -> AsyncFdxResource:
        from .resources.fdx import AsyncFdxResource

        return AsyncFdxResource(self)

    @cached_property
    def crypto(self) -> AsyncCryptoResource:
        from .resources.crypto import AsyncCryptoResource

        return AsyncCryptoResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncSlashSDKWithRawResponse:
        return AsyncSlashSDKWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSlashSDKWithStreamedResponse:
        return AsyncSlashSDKWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._api_key, **self._bearer, **self._developer_application}

    @property
    def _api_key(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"X-API-Key": api_key}

    @property
    def _bearer(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        if bearer_token is None:
            return {}
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    def _developer_application(self) -> dict[str, str]:
        if self.username is None:
            return {}
        if self.password is None:
            return {}
        credentials = f"{self.username}:{self.password}".encode("ascii")
        header = f"Basic {base64.b64encode(credentials).decode('ascii')}"
        return {"Authorization": header}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("X-API-Key") or isinstance(custom_headers.get("X-API-Key"), Omit):
            return

        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected one of api_key, bearer_token, username or password to be set. Or for one of the `X-API-Key`, `Authorization` or `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            bearer_token=bearer_token or self.bearer_token,
            username=username or self.username,
            password=password or self.password,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class SlashSDKWithRawResponse:
    _client: SlashSDK

    def __init__(self, client: SlashSDK) -> None:
        self._client = client

    @cached_property
    def legal_entity(self) -> legal_entity.LegalEntityResourceWithRawResponse:
        from .resources.legal_entity import LegalEntityResourceWithRawResponse

        return LegalEntityResourceWithRawResponse(self._client.legal_entity)

    @cached_property
    def account(self) -> account.AccountResourceWithRawResponse:
        from .resources.account import AccountResourceWithRawResponse

        return AccountResourceWithRawResponse(self._client.account)

    @cached_property
    def virtual_account(self) -> virtual_account.VirtualAccountResourceWithRawResponse:
        from .resources.virtual_account import VirtualAccountResourceWithRawResponse

        return VirtualAccountResourceWithRawResponse(self._client.virtual_account)

    @cached_property
    def transaction(self) -> transaction.TransactionResourceWithRawResponse:
        from .resources.transaction import TransactionResourceWithRawResponse

        return TransactionResourceWithRawResponse(self._client.transaction)

    @cached_property
    def transfer(self) -> transfer.TransferResourceWithRawResponse:
        from .resources.transfer import TransferResourceWithRawResponse

        return TransferResourceWithRawResponse(self._client.transfer)

    @cached_property
    def card(self) -> card.CardResourceWithRawResponse:
        from .resources.card import CardResourceWithRawResponse

        return CardResourceWithRawResponse(self._client.card)

    @cached_property
    def card_group(self) -> card_group.CardGroupResourceWithRawResponse:
        from .resources.card_group import CardGroupResourceWithRawResponse

        return CardGroupResourceWithRawResponse(self._client.card_group)

    @cached_property
    def card_product(self) -> card_product.CardProductResourceWithRawResponse:
        from .resources.card_product import CardProductResourceWithRawResponse

        return CardProductResourceWithRawResponse(self._client.card_product)

    @cached_property
    def slash_handle(self) -> slash_handle.SlashHandleResourceWithRawResponse:
        from .resources.slash_handle import SlashHandleResourceWithRawResponse

        return SlashHandleResourceWithRawResponse(self._client.slash_handle)

    @cached_property
    def pay(self) -> pay.PayResourceWithRawResponse:
        from .resources.pay import PayResourceWithRawResponse

        return PayResourceWithRawResponse(self._client.pay)

    @cached_property
    def webhook(self) -> webhook.WebhookResourceWithRawResponse:
        from .resources.webhook import WebhookResourceWithRawResponse

        return WebhookResourceWithRawResponse(self._client.webhook)

    @cached_property
    def merchant(self) -> merchant.MerchantResourceWithRawResponse:
        from .resources.merchant import MerchantResourceWithRawResponse

        return MerchantResourceWithRawResponse(self._client.merchant)

    @cached_property
    def merchant_category(self) -> merchant_category.MerchantCategoryResourceWithRawResponse:
        from .resources.merchant_category import MerchantCategoryResourceWithRawResponse

        return MerchantCategoryResourceWithRawResponse(self._client.merchant_category)

    @cached_property
    def developer_account(self) -> developer_account.DeveloperAccountResourceWithRawResponse:
        from .resources.developer_account import DeveloperAccountResourceWithRawResponse

        return DeveloperAccountResourceWithRawResponse(self._client.developer_account)

    @cached_property
    def developer_application(self) -> developer_application.DeveloperApplicationResourceWithRawResponse:
        from .resources.developer_application import DeveloperApplicationResourceWithRawResponse

        return DeveloperApplicationResourceWithRawResponse(self._client.developer_application)

    @cached_property
    def well_known(self) -> well_known.WellKnownResourceWithRawResponse:
        from .resources.well_known import WellKnownResourceWithRawResponse

        return WellKnownResourceWithRawResponse(self._client.well_known)

    @cached_property
    def oauth2(self) -> oauth2.Oauth2ResourceWithRawResponse:
        from .resources.oauth2 import Oauth2ResourceWithRawResponse

        return Oauth2ResourceWithRawResponse(self._client.oauth2)

    @cached_property
    def fdx(self) -> fdx.FdxResourceWithRawResponse:
        from .resources.fdx import FdxResourceWithRawResponse

        return FdxResourceWithRawResponse(self._client.fdx)

    @cached_property
    def crypto(self) -> crypto.CryptoResourceWithRawResponse:
        from .resources.crypto import CryptoResourceWithRawResponse

        return CryptoResourceWithRawResponse(self._client.crypto)


class AsyncSlashSDKWithRawResponse:
    _client: AsyncSlashSDK

    def __init__(self, client: AsyncSlashSDK) -> None:
        self._client = client

    @cached_property
    def legal_entity(self) -> legal_entity.AsyncLegalEntityResourceWithRawResponse:
        from .resources.legal_entity import AsyncLegalEntityResourceWithRawResponse

        return AsyncLegalEntityResourceWithRawResponse(self._client.legal_entity)

    @cached_property
    def account(self) -> account.AsyncAccountResourceWithRawResponse:
        from .resources.account import AsyncAccountResourceWithRawResponse

        return AsyncAccountResourceWithRawResponse(self._client.account)

    @cached_property
    def virtual_account(self) -> virtual_account.AsyncVirtualAccountResourceWithRawResponse:
        from .resources.virtual_account import AsyncVirtualAccountResourceWithRawResponse

        return AsyncVirtualAccountResourceWithRawResponse(self._client.virtual_account)

    @cached_property
    def transaction(self) -> transaction.AsyncTransactionResourceWithRawResponse:
        from .resources.transaction import AsyncTransactionResourceWithRawResponse

        return AsyncTransactionResourceWithRawResponse(self._client.transaction)

    @cached_property
    def transfer(self) -> transfer.AsyncTransferResourceWithRawResponse:
        from .resources.transfer import AsyncTransferResourceWithRawResponse

        return AsyncTransferResourceWithRawResponse(self._client.transfer)

    @cached_property
    def card(self) -> card.AsyncCardResourceWithRawResponse:
        from .resources.card import AsyncCardResourceWithRawResponse

        return AsyncCardResourceWithRawResponse(self._client.card)

    @cached_property
    def card_group(self) -> card_group.AsyncCardGroupResourceWithRawResponse:
        from .resources.card_group import AsyncCardGroupResourceWithRawResponse

        return AsyncCardGroupResourceWithRawResponse(self._client.card_group)

    @cached_property
    def card_product(self) -> card_product.AsyncCardProductResourceWithRawResponse:
        from .resources.card_product import AsyncCardProductResourceWithRawResponse

        return AsyncCardProductResourceWithRawResponse(self._client.card_product)

    @cached_property
    def slash_handle(self) -> slash_handle.AsyncSlashHandleResourceWithRawResponse:
        from .resources.slash_handle import AsyncSlashHandleResourceWithRawResponse

        return AsyncSlashHandleResourceWithRawResponse(self._client.slash_handle)

    @cached_property
    def pay(self) -> pay.AsyncPayResourceWithRawResponse:
        from .resources.pay import AsyncPayResourceWithRawResponse

        return AsyncPayResourceWithRawResponse(self._client.pay)

    @cached_property
    def webhook(self) -> webhook.AsyncWebhookResourceWithRawResponse:
        from .resources.webhook import AsyncWebhookResourceWithRawResponse

        return AsyncWebhookResourceWithRawResponse(self._client.webhook)

    @cached_property
    def merchant(self) -> merchant.AsyncMerchantResourceWithRawResponse:
        from .resources.merchant import AsyncMerchantResourceWithRawResponse

        return AsyncMerchantResourceWithRawResponse(self._client.merchant)

    @cached_property
    def merchant_category(self) -> merchant_category.AsyncMerchantCategoryResourceWithRawResponse:
        from .resources.merchant_category import AsyncMerchantCategoryResourceWithRawResponse

        return AsyncMerchantCategoryResourceWithRawResponse(self._client.merchant_category)

    @cached_property
    def developer_account(self) -> developer_account.AsyncDeveloperAccountResourceWithRawResponse:
        from .resources.developer_account import AsyncDeveloperAccountResourceWithRawResponse

        return AsyncDeveloperAccountResourceWithRawResponse(self._client.developer_account)

    @cached_property
    def developer_application(self) -> developer_application.AsyncDeveloperApplicationResourceWithRawResponse:
        from .resources.developer_application import AsyncDeveloperApplicationResourceWithRawResponse

        return AsyncDeveloperApplicationResourceWithRawResponse(self._client.developer_application)

    @cached_property
    def well_known(self) -> well_known.AsyncWellKnownResourceWithRawResponse:
        from .resources.well_known import AsyncWellKnownResourceWithRawResponse

        return AsyncWellKnownResourceWithRawResponse(self._client.well_known)

    @cached_property
    def oauth2(self) -> oauth2.AsyncOauth2ResourceWithRawResponse:
        from .resources.oauth2 import AsyncOauth2ResourceWithRawResponse

        return AsyncOauth2ResourceWithRawResponse(self._client.oauth2)

    @cached_property
    def fdx(self) -> fdx.AsyncFdxResourceWithRawResponse:
        from .resources.fdx import AsyncFdxResourceWithRawResponse

        return AsyncFdxResourceWithRawResponse(self._client.fdx)

    @cached_property
    def crypto(self) -> crypto.AsyncCryptoResourceWithRawResponse:
        from .resources.crypto import AsyncCryptoResourceWithRawResponse

        return AsyncCryptoResourceWithRawResponse(self._client.crypto)


class SlashSDKWithStreamedResponse:
    _client: SlashSDK

    def __init__(self, client: SlashSDK) -> None:
        self._client = client

    @cached_property
    def legal_entity(self) -> legal_entity.LegalEntityResourceWithStreamingResponse:
        from .resources.legal_entity import LegalEntityResourceWithStreamingResponse

        return LegalEntityResourceWithStreamingResponse(self._client.legal_entity)

    @cached_property
    def account(self) -> account.AccountResourceWithStreamingResponse:
        from .resources.account import AccountResourceWithStreamingResponse

        return AccountResourceWithStreamingResponse(self._client.account)

    @cached_property
    def virtual_account(self) -> virtual_account.VirtualAccountResourceWithStreamingResponse:
        from .resources.virtual_account import VirtualAccountResourceWithStreamingResponse

        return VirtualAccountResourceWithStreamingResponse(self._client.virtual_account)

    @cached_property
    def transaction(self) -> transaction.TransactionResourceWithStreamingResponse:
        from .resources.transaction import TransactionResourceWithStreamingResponse

        return TransactionResourceWithStreamingResponse(self._client.transaction)

    @cached_property
    def transfer(self) -> transfer.TransferResourceWithStreamingResponse:
        from .resources.transfer import TransferResourceWithStreamingResponse

        return TransferResourceWithStreamingResponse(self._client.transfer)

    @cached_property
    def card(self) -> card.CardResourceWithStreamingResponse:
        from .resources.card import CardResourceWithStreamingResponse

        return CardResourceWithStreamingResponse(self._client.card)

    @cached_property
    def card_group(self) -> card_group.CardGroupResourceWithStreamingResponse:
        from .resources.card_group import CardGroupResourceWithStreamingResponse

        return CardGroupResourceWithStreamingResponse(self._client.card_group)

    @cached_property
    def card_product(self) -> card_product.CardProductResourceWithStreamingResponse:
        from .resources.card_product import CardProductResourceWithStreamingResponse

        return CardProductResourceWithStreamingResponse(self._client.card_product)

    @cached_property
    def slash_handle(self) -> slash_handle.SlashHandleResourceWithStreamingResponse:
        from .resources.slash_handle import SlashHandleResourceWithStreamingResponse

        return SlashHandleResourceWithStreamingResponse(self._client.slash_handle)

    @cached_property
    def pay(self) -> pay.PayResourceWithStreamingResponse:
        from .resources.pay import PayResourceWithStreamingResponse

        return PayResourceWithStreamingResponse(self._client.pay)

    @cached_property
    def webhook(self) -> webhook.WebhookResourceWithStreamingResponse:
        from .resources.webhook import WebhookResourceWithStreamingResponse

        return WebhookResourceWithStreamingResponse(self._client.webhook)

    @cached_property
    def merchant(self) -> merchant.MerchantResourceWithStreamingResponse:
        from .resources.merchant import MerchantResourceWithStreamingResponse

        return MerchantResourceWithStreamingResponse(self._client.merchant)

    @cached_property
    def merchant_category(self) -> merchant_category.MerchantCategoryResourceWithStreamingResponse:
        from .resources.merchant_category import MerchantCategoryResourceWithStreamingResponse

        return MerchantCategoryResourceWithStreamingResponse(self._client.merchant_category)

    @cached_property
    def developer_account(self) -> developer_account.DeveloperAccountResourceWithStreamingResponse:
        from .resources.developer_account import DeveloperAccountResourceWithStreamingResponse

        return DeveloperAccountResourceWithStreamingResponse(self._client.developer_account)

    @cached_property
    def developer_application(self) -> developer_application.DeveloperApplicationResourceWithStreamingResponse:
        from .resources.developer_application import DeveloperApplicationResourceWithStreamingResponse

        return DeveloperApplicationResourceWithStreamingResponse(self._client.developer_application)

    @cached_property
    def well_known(self) -> well_known.WellKnownResourceWithStreamingResponse:
        from .resources.well_known import WellKnownResourceWithStreamingResponse

        return WellKnownResourceWithStreamingResponse(self._client.well_known)

    @cached_property
    def oauth2(self) -> oauth2.Oauth2ResourceWithStreamingResponse:
        from .resources.oauth2 import Oauth2ResourceWithStreamingResponse

        return Oauth2ResourceWithStreamingResponse(self._client.oauth2)

    @cached_property
    def fdx(self) -> fdx.FdxResourceWithStreamingResponse:
        from .resources.fdx import FdxResourceWithStreamingResponse

        return FdxResourceWithStreamingResponse(self._client.fdx)

    @cached_property
    def crypto(self) -> crypto.CryptoResourceWithStreamingResponse:
        from .resources.crypto import CryptoResourceWithStreamingResponse

        return CryptoResourceWithStreamingResponse(self._client.crypto)


class AsyncSlashSDKWithStreamedResponse:
    _client: AsyncSlashSDK

    def __init__(self, client: AsyncSlashSDK) -> None:
        self._client = client

    @cached_property
    def legal_entity(self) -> legal_entity.AsyncLegalEntityResourceWithStreamingResponse:
        from .resources.legal_entity import AsyncLegalEntityResourceWithStreamingResponse

        return AsyncLegalEntityResourceWithStreamingResponse(self._client.legal_entity)

    @cached_property
    def account(self) -> account.AsyncAccountResourceWithStreamingResponse:
        from .resources.account import AsyncAccountResourceWithStreamingResponse

        return AsyncAccountResourceWithStreamingResponse(self._client.account)

    @cached_property
    def virtual_account(self) -> virtual_account.AsyncVirtualAccountResourceWithStreamingResponse:
        from .resources.virtual_account import AsyncVirtualAccountResourceWithStreamingResponse

        return AsyncVirtualAccountResourceWithStreamingResponse(self._client.virtual_account)

    @cached_property
    def transaction(self) -> transaction.AsyncTransactionResourceWithStreamingResponse:
        from .resources.transaction import AsyncTransactionResourceWithStreamingResponse

        return AsyncTransactionResourceWithStreamingResponse(self._client.transaction)

    @cached_property
    def transfer(self) -> transfer.AsyncTransferResourceWithStreamingResponse:
        from .resources.transfer import AsyncTransferResourceWithStreamingResponse

        return AsyncTransferResourceWithStreamingResponse(self._client.transfer)

    @cached_property
    def card(self) -> card.AsyncCardResourceWithStreamingResponse:
        from .resources.card import AsyncCardResourceWithStreamingResponse

        return AsyncCardResourceWithStreamingResponse(self._client.card)

    @cached_property
    def card_group(self) -> card_group.AsyncCardGroupResourceWithStreamingResponse:
        from .resources.card_group import AsyncCardGroupResourceWithStreamingResponse

        return AsyncCardGroupResourceWithStreamingResponse(self._client.card_group)

    @cached_property
    def card_product(self) -> card_product.AsyncCardProductResourceWithStreamingResponse:
        from .resources.card_product import AsyncCardProductResourceWithStreamingResponse

        return AsyncCardProductResourceWithStreamingResponse(self._client.card_product)

    @cached_property
    def slash_handle(self) -> slash_handle.AsyncSlashHandleResourceWithStreamingResponse:
        from .resources.slash_handle import AsyncSlashHandleResourceWithStreamingResponse

        return AsyncSlashHandleResourceWithStreamingResponse(self._client.slash_handle)

    @cached_property
    def pay(self) -> pay.AsyncPayResourceWithStreamingResponse:
        from .resources.pay import AsyncPayResourceWithStreamingResponse

        return AsyncPayResourceWithStreamingResponse(self._client.pay)

    @cached_property
    def webhook(self) -> webhook.AsyncWebhookResourceWithStreamingResponse:
        from .resources.webhook import AsyncWebhookResourceWithStreamingResponse

        return AsyncWebhookResourceWithStreamingResponse(self._client.webhook)

    @cached_property
    def merchant(self) -> merchant.AsyncMerchantResourceWithStreamingResponse:
        from .resources.merchant import AsyncMerchantResourceWithStreamingResponse

        return AsyncMerchantResourceWithStreamingResponse(self._client.merchant)

    @cached_property
    def merchant_category(self) -> merchant_category.AsyncMerchantCategoryResourceWithStreamingResponse:
        from .resources.merchant_category import AsyncMerchantCategoryResourceWithStreamingResponse

        return AsyncMerchantCategoryResourceWithStreamingResponse(self._client.merchant_category)

    @cached_property
    def developer_account(self) -> developer_account.AsyncDeveloperAccountResourceWithStreamingResponse:
        from .resources.developer_account import AsyncDeveloperAccountResourceWithStreamingResponse

        return AsyncDeveloperAccountResourceWithStreamingResponse(self._client.developer_account)

    @cached_property
    def developer_application(self) -> developer_application.AsyncDeveloperApplicationResourceWithStreamingResponse:
        from .resources.developer_application import AsyncDeveloperApplicationResourceWithStreamingResponse

        return AsyncDeveloperApplicationResourceWithStreamingResponse(self._client.developer_application)

    @cached_property
    def well_known(self) -> well_known.AsyncWellKnownResourceWithStreamingResponse:
        from .resources.well_known import AsyncWellKnownResourceWithStreamingResponse

        return AsyncWellKnownResourceWithStreamingResponse(self._client.well_known)

    @cached_property
    def oauth2(self) -> oauth2.AsyncOauth2ResourceWithStreamingResponse:
        from .resources.oauth2 import AsyncOauth2ResourceWithStreamingResponse

        return AsyncOauth2ResourceWithStreamingResponse(self._client.oauth2)

    @cached_property
    def fdx(self) -> fdx.AsyncFdxResourceWithStreamingResponse:
        from .resources.fdx import AsyncFdxResourceWithStreamingResponse

        return AsyncFdxResourceWithStreamingResponse(self._client.fdx)

    @cached_property
    def crypto(self) -> crypto.AsyncCryptoResourceWithStreamingResponse:
        from .resources.crypto import AsyncCryptoResourceWithStreamingResponse

        return AsyncCryptoResourceWithStreamingResponse(self._client.crypto)


Client = SlashSDK

AsyncClient = AsyncSlashSDK
