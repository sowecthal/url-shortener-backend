from asyncpg import Pool

from url_shortener.models import URLAssoc
from ..url_repository import IURLRepository


class PostgreSQLURLRepository(IURLRepository):
    def __init__(self, pg_pool: Pool):
        self._pg_pool = pg_pool

    async def create(self, url_assoc: URLAssoc) -> None:
        pass

    async def delete(self, url_assoc: URLAssoc) -> None:
        pass