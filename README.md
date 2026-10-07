# dotconfig-api

Flask REST API backed by MySQL.

## Setup

Requires [uv](https://docs.astral.sh/uv/).

```bash
cp .env.example .env   # then fill in your database details
uv run dotconfig-api
```

uv creates `.venv` and installs the locked dependencies on first run, so there is no virtualenv to create or activate.

Configuration is read from environment variables, loaded from `.env` if present:

| Variable | Required | Description |
| --- | --- | --- |
| `DB_HOST` | yes | MySQL / RDS endpoint |
| `DB_PORT` | no | MySQL port (default `3306`) |
| `DB_USER` | yes | Database username |
| `DB_PASSWORD` | yes | Database password |
| `DB_NAME` | yes | Database name |
| `FLASK_DEBUG` | no | `1` to enable debug mode (default off) |
| `APP_PORT` | no | Port the API listens on (default `8000`) |

## Layout

```
src/dotconfig_api/
├── __init__.py   # create_app() factory and the dotconfig-api entry point
├── db.py         # MySQL connection
├── routes.py     # API and UI routes
└── templates/    # UI served at /
```

Dependencies are declared in `pyproject.toml` and pinned in `uv.lock`.
