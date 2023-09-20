from typing import Union

from fastapi import HTTPException
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY


async def http_error_handler(_: Request, exc: HTTPException) -> JSONResponse:
    return JSONResponse({"errors": [exc.detail]}, status_code=exc.status_code)


async def http422_error_handler(
    _: Request, exc: Union[RequestValidationError, ValidationError]
) -> JSONResponse:
    return JSONResponse(
        {"errors": exc.errors()}, status_code=HTTP_422_UNPROCESSABLE_ENTITY
    )
