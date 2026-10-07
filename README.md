# python-mysql-db-proj-1

## Setup

Requires [uv](https://docs.astral.sh/uv/).

```bash
cp .env.example .env   # then fill in your database details
uv run --with-requirements requirements.txt app.py
```

uv installs the dependencies into a cached environment on first run, so there is no virtualenv to create or activate.

Configuration is read from environment variables, loaded from `.env` if present:

| Variable | Required | Description |
| --- | --- | --- |
| `DB_HOST` | yes | MySQL / RDS endpoint |
| `DB_PORT` | no | MySQL port (default `3306`) |
| `DB_USER` | yes | Database username |
| `DB_PASSWORD` | yes | Database password |
| `DB_NAME` | yes | Database name |
| `FLASK_DEBUG` | no | `1` to enable debug mode (default off) |
