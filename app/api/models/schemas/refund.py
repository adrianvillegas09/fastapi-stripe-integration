from typing import Any

from pydantic import BaseModel, Json


class Refund(BaseModel):
    id: str
    amount: float
    balance_transaction: str
    charge: str
    created: str
    currency: str
    metadata: Json
    payment_intent: str
    reason: Any
    receipt_number: Any
    source_transfer_reversal: Any
    status: str
    transfer_reversal: Any
