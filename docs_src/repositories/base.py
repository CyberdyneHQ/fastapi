import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)

# Module-level registry populated by the @register_repository decorator.
REPOSITORIES: list[type["BaseRepository"]] = []


def register_repository(cls: type["BaseRepository"]) -> type["BaseRepository"]:
    """Register a repository class in the global REPOSITORIES registry."""
    REPOSITORIES.append(cls)
    return cls


class BaseRepository(ABC):
    """Base class every repository must inherit from."""

    entity_name: str = ""

    def __init__(self) -> None:
        self._items: dict[int, dict] = {}

    @abstractmethod
    def get(self, item_id: int) -> dict:
        """Return a single entity by its identifier."""
        ...

    @abstractmethod
    def list_all(self) -> list[dict]:
        """Return every stored entity."""
        ...

    @abstractmethod
    def create(self, payload: dict) -> dict:
        """Persist a new entity and return it."""
        ...
