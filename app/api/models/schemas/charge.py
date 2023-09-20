from typing import Any, List, Optional

from pydantic import BaseModel


class Charge(BaseModel):
    charge_id: str


class Card(BaseModel):
    number: str
    exp_month: int
    exp_year: int
    cvc: str


class CreateCharge(BaseModel):
    amount: int
    currency: str
    card: Card
    description: Optional[str]


class ChargeList(BaseModel):
    data: List[Any]
    has_more: bool
