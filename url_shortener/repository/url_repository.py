from abc import ABC, abstractmethod

from url_shortener.models import URLAssoc


class IURLRepository(ABC):
    @abstractmethod
    def create(self, url_assoc: URLAssoc) -> None:
        pass

    @abstractmethod
    def delete(self, url_assoc: URLAssoc) -> None:
        pass
