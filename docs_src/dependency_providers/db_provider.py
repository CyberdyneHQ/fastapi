import logging

from fastapi import Depends, FastAPI

from .base import BaseProvider, register_provider

logger = logging.getLogger(__name__)


@register_provider
class DbProvider(BaseProvider):
    resource_name = "db"

    def provide(self) -> dict:
        return {"resource": self.resource_name, "status": "ready"}


app = FastAPI()


@app.get("/db")
async def read_db(resource: dict = Depends(DbProvider())):
    return resource
