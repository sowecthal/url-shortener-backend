import asyncpg

class Database:
    def __init__(self, config):
        self.config = config
        self.pool = None

    async def createPool(self):
        self.pool = await asyncpg.create_pool(**self.config['DATABASE'])

    async def insert_new_user(self, login, pass_hash):
        query = "INSERT INTO users (login, pass_hash) VALUES ($1, $2)"
        async with self.pool.acquire() as conn:
                await conn.execute(query, login, pass_hash)
    
    async def fetch_user_by_login(self, login):
        query = "SELECT id, login, pass_hash, role FROM users WHERE login = $1"
        async with self.pool.acquire() as conn:
            return await conn.fetchrow(query, login)

    async def delete_user(self, login):
        delete_urls_query = "DELETE FROM urls WHERE user_id = (SELECT id FROM users WHERE login = $1)"
        delete_user_query = "DELETE FROM users WHERE login = $1"
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                await conn.execute(delete_urls_query, login)
                return await conn.execute(delete_user_query, login)

    async def insert_new_url(self, user_id, original_url, short_url):
        query = "INSERT INTO urls (user_id, original_url, short_url) VALUES ($1, $2, $3)"
        async with self.pool.acquire() as conn:
            await conn.execute(query, user_id, original_url, short_url)

    async def fetch_urls_by_user(self, login):
        query = "SELECT urls.short_url FROM urls JOIN users ON urls.user_id = users.id WHERE users.login = $1"
        async with self.pool.acquire() as conn:
            return await conn.fetchrow(query, login)

    async def delete_url(self, short_url):
        query = "DELETE FROM urls WHERE short_url = $1"
        async with self.pool.acquire() as conn:
            return await conn.execute(query, short_url)