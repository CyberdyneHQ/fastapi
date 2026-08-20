import logging

from fastapi import Depends, FastAPI

from .base import BaseProvider, register_provider

logger = logging.getLogger(__name__)


@register_provider
class StorageProvider(BaseProvider):
    resource_name = "storage"

    def provide(self) -> dict:
        return {"resource": self.resource_name, "status": "ready"}


app = FastAPI()


@app.get("/storage")
async def read_storage(resource: dict = Depends(StorageProvider())):
    return resource
