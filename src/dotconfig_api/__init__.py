import os

from dotenv import find_dotenv, load_dotenv
from flask import Flask

from dotconfig_api.routes import bp


def create_app():
    # Load variables from .env into the environment (real env vars take precedence).
    # The file is looked up from the working directory upwards.
    load_dotenv(find_dotenv(usecwd=True))

    app = Flask(__name__)
    app.config.from_mapping(
        DB_HOST=os.environ['DB_HOST'],
        DB_PORT=int(os.environ.get('DB_PORT', 3306)),
        DB_USER=os.environ['DB_USER'],
        DB_PASSWORD=os.environ['DB_PASSWORD'],
        DB_NAME=os.environ['DB_NAME'],
    )
    app.register_blueprint(bp)
    return app


def main() -> None:
    # Debug mode is controlled by FLASK_DEBUG in .env
    create_app().run(host='0.0.0.0', port=int(os.environ.get('APP_PORT', 8000)))
