import logging

from fastapi import Depends, FastAPI

from .base import BaseProvider, register_provider

logger = logging.getLogger(__name__)


@register_provider
class ConfigProvider(BaseProvider):
    resource_name = "config"

    def provide(self) -> dict:
        return {"resource": self.resource_name, "status": "ready"}


app = FastAPI()


@app.get("/config")
async def read_config(resource: dict = Depends(ConfigProvider())):
    return resource
