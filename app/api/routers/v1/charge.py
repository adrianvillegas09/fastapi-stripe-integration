from typing import Optional

from fastapi import APIRouter, Body
from starlette.status import HTTP_200_OK, HTTP_201_CREATED

from app.api.dependencies.charge import (capture_charge_dependency,
                                         create_charge_dependency,
                                         get_charges_dependency)
from app.api.dependencies.refund import create_refund_dependency
from app.api.models.schemas.charge import ChargeList, CreateCharge
from app.api.models.schemas.refund import Refund

router = APIRouter()


@router.get(
    "/get_charges",
    status_code=HTTP_200_OK,
    response_model=ChargeList,
    name="GET:charges",
)
def get_charges(
    limit: Optional[int] = 10, starting_after: Optional[str] = None
) -> ChargeList:
    return get_charges_dependency(limit, starting_after)


@router.post(
    "/create_charge",
    status_code=HTTP_201_CREATED,
    name="POST:charge",
)
def create_charge(request_body: CreateCharge = Body(...)):
    return create_charge_dependency(
        request_body.amount,
        request_body.card,
        request_body.currency,
        request_body.description,
    )


@router.post(
    "/capture_charge/{charge_id}",
    status_code=HTTP_201_CREATED,
    name="POST:charge",
)
def create_refund(charge_id: str) -> Refund:
    return capture_charge_dependency(charge_id)


@router.post(
    "/create_refund/{charge_id}",
    status_code=HTTP_201_CREATED,
    name="POST:refund",
)
def create_refund(charge_id: str) -> Refund:
    return create_refund_dependency(charge_id)
