import logging

from .base import BaseRepository, register_repository

logger = logging.getLogger(__name__)


@register_repository
class OrderRepository(BaseRepository):
    entity_name = "order"

    def get(self, item_id: int) -> dict:
        logger.info("Fetching %s %s", self.entity_name, item_id)
        return self._items[item_id]

    def list_all(self) -> list[dict]:
        logger.info("Listing all %s entities", self.entity_name)
        return list(self._items.values())

    def create(self, payload: dict) -> dict:
        item_id = payload["id"]
        self._items[item_id] = payload
        return payload
