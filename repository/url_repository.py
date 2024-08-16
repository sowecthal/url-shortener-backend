from abc import ABC, abstractmethod
from models.url_assoc import URLAssoc

class IURLRepository(ABC):
    @abstractmethod
    def create(self, urlAssoc: URLAssoc) -> None:
        pass

    @abstractmethod
    def get_by_login(self, urlAssoc_id: int) -> URLAssoc:
        pass

    @abstractmethod
    def delete(self, urlAssoc: URLAssoc) -> None:
        pass
