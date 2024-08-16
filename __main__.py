from repository.postgresql.pg_url_repository import PostgreSQLURLRepository
from services.business import URLShortener

def main():
    URL_repository = PostgreSQLURLRepository(conn_data)
    URLShortener(URL_repository)

if __name__ == '__main__':
    main()
