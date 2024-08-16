from typing import List 

from abc import ABC, abstractmethod
from models import User, URLAssoc

class IUserRepository(ABC):
    @abstractmethod
    def create(self, user: User) -> int:
        pass

    @abstractmethod
    def get_by_login(self, login: str) -> User:
        pass

    @abstractmethod
    def get_assoc_urls(self, user: User) -> List[URLAssoc]:
        pass

    @abstractmethod
    def delete(self, user: User) -> None:
        pass
