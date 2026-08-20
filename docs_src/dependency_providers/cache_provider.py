import logging

from fastapi import Depends, FastAPI

from .base import BaseProvider, register_provider

logger = logging.getLogger(__name__)


@register_provider
class CacheProvider(BaseProvider):
    resource_name = "cache"

    def provide(self) -> dict:
        return {"resource": self.resource_name, "status": "ready"}


app = FastAPI()


@app.get("/cache")
async def read_cache(resource: dict = Depends(CacheProvider())):
    return resource
