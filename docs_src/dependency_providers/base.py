import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)

# Module-level registry populated by the @register_provider decorator.
PROVIDERS: list[type["BaseProvider"]] = []


def register_provider(cls: type["BaseProvider"]) -> type["BaseProvider"]:
    """Register a provider class in the global PROVIDERS registry."""
    PROVIDERS.append(cls)
    return cls


class BaseProvider(ABC):
    """Base class every dependency provider must inherit from."""

    resource_name: str = ""

    @abstractmethod
    def provide(self) -> dict:
        """Return the resource this provider supplies."""
        ...

    def __call__(self) -> dict:
        logger.info("Providing %s", self.resource_name)
        return self.provide()
