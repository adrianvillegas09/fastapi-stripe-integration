from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware

from app.api.errors.error_handlers import (http422_error_handler,
                                           http_error_handler)
from app.api.routers.api import router
from app.core.config import ALLOWED_HOSTS

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(HTTPException, http_error_handler)
app.add_exception_handler(RequestValidationError, http422_error_handler)

app.include_router(router, prefix="/api")
