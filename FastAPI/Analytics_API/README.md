## Docker

- `docker build -t analytics-api -f Dockerfile .`
- `docker run analytics-api`

become

- `docker compose up --watch`
- `docker compose down` or `docker compose down -v` (to remove volumes)
- `docker compose run app /bin/bash` or `docker compose run app python`

