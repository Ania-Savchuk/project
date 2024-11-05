from abc import ABC, abstractmethod
from typing import List, Optional

class AbstractRepository(ABC):
    @abstractmethod
    def get_all(self) -> List:
        pass

    @abstractmethod
    def get_by_id(self, entity_id: int) -> Optional:
        pass

    @abstractmethod
    def create(self, **kwargs) -> None:
        pass

    @abstractmethod
    def update(self, entity_id: int, **kwargs) -> Optional:
        pass

    @abstractmethod
    def delete(self, entity_id: int) -> bool:
        pass
