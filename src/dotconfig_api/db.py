from flask import current_app
import pymysql


def get_db_connection():
    connection = pymysql.connect(host=current_app.config['DB_HOST'],
                                 port=current_app.config['DB_PORT'],
                                 user=current_app.config['DB_USER'],
                                 password=current_app.config['DB_PASSWORD'],
                                 database=current_app.config['DB_NAME'],
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection
