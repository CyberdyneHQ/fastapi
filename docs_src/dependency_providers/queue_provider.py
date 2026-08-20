import logging

from fastapi import Depends, FastAPI

from .base import BaseProvider, register_provider

logger = logging.getLogger(__name__)


@register_provider
class QueueProvider(BaseProvider):
    resource_name = "queue"

    def provide(self) -> dict:
        return {"resource": self.resource_name, "status": "ready"}


app = FastAPI()


@app.get("/queue")
async def read_queue(resource: dict = Depends(QueueProvider())):
    return resource
