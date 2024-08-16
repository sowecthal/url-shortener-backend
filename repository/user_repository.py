from abc import ABC, abstractmethod

class IUserRepository(ABC):
    @abstractmethod
    def create(self, URLAssoc: URLAssoc) -> int:
        pass

    @abstractmethod
    def get_by_id(self, URLAssoc_id: int) -> URLAssoc:
        pass

    @abstractmethod
    def update(self, dialogue: URLAssoc) -> None:
        pass

    @abstractmethod
    def update_name(self, URLAssoc: URLAssoc) -> None:
        pass

    @abstractmethod
    def update_model(self, URLAssoc: URLAssoc) -> None:
        pass

    @abstractmethod
    def delete(self, URLAssoc: URLAssoc) -> None:
        pass
