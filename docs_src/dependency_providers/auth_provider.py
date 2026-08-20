import logging

from fastapi import Depends, FastAPI

from .base import BaseProvider, register_provider

logger = logging.getLogger(__name__)


@register_provider
class AuthProvider(BaseProvider):
    resource_name = "auth"

    def provide(self) -> dict:
        return {"resource": self.resource_name, "status": "ready"}


app = FastAPI()


@app.get("/auth")
async def read_auth(resource: dict = Depends(AuthProvider())):
    return resource
