from repository.url_repository import IURLRepository
from dataclasses import dataclass
import datetime 

@dataclass
class URL:
    original_url: str
    short_url: str
    clicks: int
    reg_date: datetime.datetime
    user_id: int


class URLShortener:
    def __init__(self, URL_repository: IURLRepository) -> None:
        self.URL_repository = URL_repository

    def shorten_URL(self, user_id: int, original_url: str) -> str:
        pass