# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "Transaction",
    "ACHInfo",
    "CryptoInfo",
    "FeeInfo",
    "FeeInfoRelatedTransaction",
    "FpsInfo",
    "MerchantData",
    "MerchantDataLocation",
    "OriginalCurrency",
    "PixInfo",
    "RtpInfo",
    "SepaInfo",
    "SpeiInfo",
    "WireInfo",
]


class ACHInfo(BaseModel):
    """
    Information about the associated ACH transfer if the transaction is an ACH transfer.
    """

    company_discretionary_data: str = FieldInfo(alias="companyDiscretionaryData")
    """
    Optional data field that can be used by the originating company for internal
    purposes
    """

    company_id: str = FieldInfo(alias="companyId")
    """
    The company identification number assigned by the originating depository
    financial institution
    """

    entry_class_code: str = FieldInfo(alias="entryClassCode")
    """
    A three-character code that identifies the type of ACH entry (e.g., PPD for
    Prearranged Payment and Deposit, CCD for Corporate Credit or Debit)
    """

    payment_related_info: str = FieldInfo(alias="paymentRelatedInfo")
    """
    Additional information related to the payment, such as invoice numbers, payment
    references, or other payment-specific details
    """

    receiver_id: str = FieldInfo(alias="receiverId")
    """The unique identifier for the receiver of the ACH transfer"""

    trace_number: str = FieldInfo(alias="traceNumber")
    """
    A unique number assigned by the originating depository financial institution to
    identify the ACH entry
    """

    company_entry_description: Optional[str] = FieldInfo(alias="companyEntryDescription", default=None)
    """
    An optional description of the purpose of the ACH entry as provided by the
    originating company
    """

    counterparty_bank: Optional[str] = FieldInfo(alias="counterpartyBank", default=None)
    """
    The name of the bank or financial institution of the counterparty in the ACH
    transfer
    """


class CryptoInfo(BaseModel):
    """Information populated if this transaction is a crypto on/off-ramp transaction."""

    sender_address: Optional[str] = FieldInfo(alias="senderAddress", default=None)
    """The sender address of the crypto on/off-ramp transaction."""

    tx_hash: Optional[str] = FieldInfo(alias="txHash", default=None)
    """The transaction hash of the crypto on/off-ramp transaction."""


class FeeInfoRelatedTransaction(BaseModel):
    id: str

    amount: float


class FeeInfo(BaseModel):
    """Information populated if this transaction is a fee assessed by Slash."""

    related_transaction: Optional[FeeInfoRelatedTransaction] = FieldInfo(alias="relatedTransaction", default=None)


class FpsInfo(BaseModel):
    """
    Information about the associated Faster Payments transfer if the transaction is a Faster Payments deposit into a Global USD account.
    """

    account_number: Optional[str] = FieldInfo(alias="accountNumber", default=None)
    """The account number of the counterparty on the Faster Payments transfer."""

    last4: Optional[str] = None
    """
    The last 4 digits of the account number of the counterparty on the Faster
    Payments transfer.
    """

    recipient_name: Optional[str] = FieldInfo(alias="recipientName", default=None)
    """The name of the recipient of the Faster Payments transfer."""

    reference: Optional[str] = None
    """
    The free-form reference field set by the originator on the Faster Payments
    transfer.
    """

    sender_name: Optional[str] = FieldInfo(alias="senderName", default=None)
    """The name of the originator of the Faster Payments transfer."""

    sort_code: Optional[str] = FieldInfo(alias="sortCode", default=None)
    """The sort code of the counterparty bank on the Faster Payments transfer."""

    uetr: Optional[str] = None
    """
    The unique end-to-end transaction reference (UETR) for the Faster Payments
    transfer.
    """


class MerchantDataLocation(BaseModel):
    """Location details for the merchant/transaction."""

    city: str
    """The city of the merchant."""

    country: str
    """The country of the merchant."""

    state: str
    """The state/province of the merchant."""

    zip: str
    """The ZIP/postal code of the merchant."""


class MerchantData(BaseModel):
    """
    For card transactions, contains description of the transaction as reported by the merchant, merchant category code, and location of the merchant or origin of the transaction.
    For other transactions, this field is undefined.
    """

    category_code: str = FieldInfo(alias="categoryCode")
    """The merchant's category code (MCC)"""

    description: str
    """The raw description provided by the merchant for the transaction."""

    location: Optional[MerchantDataLocation] = None
    """Location details for the merchant/transaction."""


class OriginalCurrency(BaseModel):
    """The original currency of the transaction.

    This is only applicable to transactions. If this field is not sent, the original currency is in USD.
    """

    amount_cents: float = FieldInfo(alias="amountCents")
    """The amount of the transaction in its original currency in cents."""

    code: str
    """The original currency code of the transaction"""

    conversion_rate: float = FieldInfo(alias="conversionRate")
    """
    The conversion rate used to convert the transaction amount from its original
    currency to the account currency. The currency rate is computed at the time of
    the transaction.
    """


class PixInfo(BaseModel):
    """
    Information about the associated PIX (Brazilian instant-payment) transfer if the transaction is a PIX deposit into a Global USD account.
    """

    description: Optional[str] = None
    """A description of the PIX transfer provided by the originator."""

    reference: Optional[str] = None
    """The free-form reference field set by the originator on the PIX transfer."""

    sender_name: Optional[str] = FieldInfo(alias="senderName", default=None)
    """The name of the originator of the PIX transfer."""

    tracking_number: Optional[str] = FieldInfo(alias="trackingNumber", default=None)
    """The PIX network tracking number (`endToEndId`) for the transfer."""


class RtpInfo(BaseModel):
    """
    Information about the associated Real-Time Payment (RTP) transfer if the transaction is a real-time transfer.
    """

    counterparty_bank: Optional[str] = FieldInfo(alias="counterpartyBank", default=None)
    """
    The name of the bank or financial institution of the counterparty in the
    real-time transfer
    """

    description: Optional[str] = None
    """Additional description or purpose of the real-time payment"""

    end_to_end_id: Optional[str] = FieldInfo(alias="endToEndId", default=None)
    """
    A unique end-to-end identifier for the real-time payment transaction that
    remains with the payment throughout its lifecycle
    """

    originator_name: Optional[str] = FieldInfo(alias="originatorName", default=None)
    """The name of the originator of the real-time payment"""

    routing_number: Optional[str] = FieldInfo(alias="routingNumber", default=None)
    """The routing number of the counterparty's bank"""


class SepaInfo(BaseModel):
    """
    Information about the associated SEPA (Single Euro Payments Area) transfer if the transaction is a SEPA deposit into a Global USD account.
    """

    bic: Optional[str] = None
    """The BIC of the counterparty bank on the SEPA transfer."""

    iban: Optional[str] = None
    """The full IBAN of the counterparty on the SEPA transfer."""

    iban_last4: Optional[str] = FieldInfo(alias="ibanLast4", default=None)
    """The last 4 characters of the IBAN of the counterparty on the SEPA transfer."""

    payment_scheme: Optional[str] = FieldInfo(alias="paymentScheme", default=None)
    """The SEPA payment scheme used (e.g., `sepa_credit_transfer`, `sepa_instant`)."""

    recipient_name: Optional[str] = FieldInfo(alias="recipientName", default=None)
    """The name of the recipient of the SEPA transfer."""

    reference: Optional[str] = None
    """The free-form reference field set by the originator on the SEPA transfer."""

    sender_name: Optional[str] = FieldInfo(alias="senderName", default=None)
    """The name of the originator of the SEPA transfer."""

    uetr: Optional[str] = None
    """The unique end-to-end transaction reference (UETR) for the SEPA transfer."""


class SpeiInfo(BaseModel):
    """
    Information about the associated SPEI (Mexican real-time payment) transfer if the transaction is a SPEI deposit into a Global USD account.
    """

    clabe: Optional[str] = None
    """The CLABE of the counterparty on the SPEI transfer."""

    description: Optional[str] = None
    """A description of the SPEI transfer provided by the originator."""

    reference: Optional[str] = None
    """
    The free-form reference field (concepto de pago) set by the originator on the
    SPEI transfer.
    """

    sender_name: Optional[str] = FieldInfo(alias="senderName", default=None)
    """The name of the originator of the SPEI transfer."""

    tracking_number: Optional[str] = FieldInfo(alias="trackingNumber", default=None)
    """The SPEI network tracking number (clave de rastreo) for the transfer."""


class WireInfo(BaseModel):
    """
    Information about the associated wire transfer if the transaction is a wire transfer.
    """

    business_function_code: str = FieldInfo(alias="businessFunctionCode")
    """
    A code that identifies the business function or purpose of the wire transfer
    (e.g., customer transfer, bank transfer, etc.)
    """

    imad: str
    """
    Incoming Message Authentication Data - a unique identifier assigned by the
    receiving bank for the incoming wire transfer. If the other bank is an account
    with Column N.A., this field is empty.
    """

    omad: str
    """
    Outgoing Message Authentication Data - a unique identifier assigned by the
    originating bank for the outgoing wire transfer. If the other bank is an account
    with Column N.A., this field is empty.
    """

    sender_reference: str = FieldInfo(alias="senderReference")
    """
    A reference number or identifier provided by the sender of the wire transfer for
    tracking purposes
    """

    subtype_code: str = FieldInfo(alias="subtypeCode")
    """A code that identifies the specific type or subtype of the wire transfer"""

    type_code: str = FieldInfo(alias="typeCode")
    """
    A code that identifies the type of wire transfer (e.g., domestic, international)
    """

    counterparty_bank: Optional[str] = FieldInfo(alias="counterpartyBank", default=None)
    """
    The name of the bank or financial institution of the counterparty in the wire
    transfer
    """


class Transaction(BaseModel):
    id: str

    account_id: object = FieldInfo(alias="accountId")
    """The account ID associated with the transaction"""

    account_subtype: Literal["cash", "credit"] = FieldInfo(alias="accountSubtype")
    """
    For charge cards, specifies if the transaction belongs to the cash or credit
    account. For debit accounts, this field is always cash.
    """

    amount_cents: float = FieldInfo(alias="amountCents")
    """The amount of the transaction in cents in USD.

    If the transaction amount is negative, the transaction is a debit. If the
    transaction amount is positive, the transaction is a credit.
    """

    date: str
    """The date in UTC time when the transaction was posted.

    If the transaction is pending or failed, this is the date the transaction was
    created.
    """

    description: str

    detailed_status: Literal[
        "pending",
        "pending_approval",
        "in_review",
        "canceled",
        "failed",
        "settled",
        "declined",
        "refund",
        "reversed",
        "returned",
        "dispute",
    ] = FieldInfo(alias="detailedStatus")
    """- `pending_approval`: Used for any transaction type that is pending approval.

    This does not affect the account's available or posted balances.

    - `pending`: Used for any transaction type that has not posted to the account
      yet, but is affecting the account's available balance.
    - `canceled`: Used for any transaction that was canceled.
    - `failed`: Used for any transaction that failed to post to the account.
    - `settled`: Used for any transaction that has posted to the account, except for
      card refunds, which use the `refund` status, and ACH returns, which use the
      `returned` status.
    - `declined`: Used for card transactions that were declined.
    - `refund`: Used for card transactions that were refunded, increasing the
      account's available and posted balances.
    - `reversed`: Used for card transactions that were authorized, but reversed by
      the merchant.
    - `returned`: Used for ACH returns. In the case of an ACH return, there are two
      possibilities: (1) if the ACH settled and then returned, then there will be
      one transaction with status `settled` for the ACH settling, and one
      transaction with status `returned` for the ACH return. Both of these are
      posted transactions. (2) if the ACH returned before settling, then there will
      only be one transaction with status `canceled`.
    - `dispute`: Used for disputed card transactions.
    """

    status: Literal["pending", "posted", "failed"]
    """
    - `pending`: The transaction is pending and has not been posted to the account
      yet (the account's posted balance doesn't reflect the transaction yet, but the
      account's available balance does).
    - `posted`: The transaction has been posted to the account and the account's
      posted balance and available balances both reflect the transaction.
    - `failed`: The transaction failed to post to the account and no longer affects
      the account's available or posted balances.
    """

    ach_info: Optional[ACHInfo] = FieldInfo(alias="achInfo", default=None)
    """
    Information about the associated ACH transfer if the transaction is an ACH
    transfer.
    """

    approval_reason: Optional[str] = FieldInfo(alias="approvalReason", default=None)
    """The reason for the approval.

    Only exists for card transactions with `detailedStatus` = `pending` or
    `settled`.
    """

    authorized_at: Optional[str] = FieldInfo(alias="authorizedAt", default=None)
    """The UTC timestamp of when the transaction was authorized.

    Only exists for card transactions.
    """

    card_id: Optional[str] = FieldInfo(alias="cardId", default=None)
    """The card ID associated with the transaction.

    If the transaction is not associated with a card, this field is not sent.
    """

    crypto_info: Optional[CryptoInfo] = FieldInfo(alias="cryptoInfo", default=None)
    """Information populated if this transaction is a crypto on/off-ramp transaction."""

    decline_reason: Optional[str] = FieldInfo(alias="declineReason", default=None)
    """The reason for the decline.

    Only exists for card transactions with `detailedStatus` = `declined`.
    """

    fee_info: Optional[FeeInfo] = FieldInfo(alias="feeInfo", default=None)
    """Information populated if this transaction is a fee assessed by Slash."""

    fps_info: Optional[FpsInfo] = FieldInfo(alias="fpsInfo", default=None)
    """
    Information about the associated Faster Payments transfer if the transaction is
    a Faster Payments deposit into a Global USD account.
    """

    memo: Optional[str] = None
    """The memo associated with the transaction.

    For virtual account transfers, this is the memo provided when creating the
    transfer. For ACH transactions, this is the company entry description. For wire
    transactions, this is the sender reference.
    """

    merchant_data: Optional[MerchantData] = FieldInfo(alias="merchantData", default=None)
    """
    For card transactions, contains description of the transaction as reported by
    the merchant, merchant category code, and location of the merchant or origin of
    the transaction. For other transactions, this field is undefined.
    """

    merchant_description: Optional[str] = FieldInfo(alias="merchantDescription", default=None)
    """DEPRECATED.

    Use `merchantData.description` instead. For card transactions, the description
    of the transaction as reported by the merchant. For other transactions, this
    field is undefined.
    """

    order_id: Optional[str] = FieldInfo(alias="orderId", default=None)
    """
    The order ID, as reported by the merchant, associated with the specific
    transaction.
    """

    original_currency: Optional[OriginalCurrency] = FieldInfo(alias="originalCurrency", default=None)
    """The original currency of the transaction.

    This is only applicable to transactions. If this field is not sent, the original
    currency is in USD.
    """

    pix_info: Optional[PixInfo] = FieldInfo(alias="pixInfo", default=None)
    """
    Information about the associated PIX (Brazilian instant-payment) transfer if the
    transaction is a PIX deposit into a Global USD account.
    """

    provider_authorization_id: Optional[str] = FieldInfo(alias="providerAuthorizationId", default=None)
    """The provider authorization ID for the transaction.

    Only exists for card transactions.
    """

    reference_number: Optional[str] = FieldInfo(alias="referenceNumber", default=None)
    """The reference number provided by Visa for this transaction."""

    rtp_info: Optional[RtpInfo] = FieldInfo(alias="rtpInfo", default=None)
    """
    Information about the associated Real-Time Payment (RTP) transfer if the
    transaction is a real-time transfer.
    """

    sepa_info: Optional[SepaInfo] = FieldInfo(alias="sepaInfo", default=None)
    """
    Information about the associated SEPA (Single Euro Payments Area) transfer if
    the transaction is a SEPA deposit into a Global USD account.
    """

    spei_info: Optional[SpeiInfo] = FieldInfo(alias="speiInfo", default=None)
    """
    Information about the associated SPEI (Mexican real-time payment) transfer if
    the transaction is a SPEI deposit into a Global USD account.
    """

    virtual_account_id: Optional[str] = FieldInfo(alias="virtualAccountId", default=None)
    """The virtual account ID where the transaction occurred"""

    wire_info: Optional[WireInfo] = FieldInfo(alias="wireInfo", default=None)
    """
    Information about the associated wire transfer if the transaction is a wire
    transfer.
    """
