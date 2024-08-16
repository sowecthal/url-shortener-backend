from models.url_assoc import URLAssoc
from repository.url_repository import IURLRepository
from asyncpg import Pool


class PostgreSQLURLRepository(IURLRepository):
    def __init__(self, pg_pool: Pool):
        self._pg_pool = pg_pool

    async def create(self, urlAssoc: URLAssoc) -> None:
        pass

    async def get_by_login(self, urlAssoc_id: int) -> URLAssoc:
        pass

    async def delete(self, urlAssoc: URLAssoc) -> None:
        pass
