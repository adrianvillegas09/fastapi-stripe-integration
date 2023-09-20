from typing import List

from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

config = Config(".env")

UNIT_TEST = config("UNIT_TEST", cast=bool, default=False)
DEBUG: bool = config("DEBUG", cast=bool, default=False)
ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS", cast=CommaSeparatedStrings, default="*"
)

## STRIP Config
STRIPE_PUBLISHABLE_KEY = config("STRIPE_PUBLISHABLE_KEY", cast=str)
STRIPE_SECRET_KEY = config("STRIPE_SECRET_KEY", cast=str)
