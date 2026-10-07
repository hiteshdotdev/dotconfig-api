from flask import Blueprint, render_template, request

from dotconfig_api.db import get_db_connection

bp = Blueprint('api', __name__)


@bp.get('/health')
def health():
    return "Up & Running"


@bp.get('/create_table')
def create_table():
    connection = get_db_connection()
    cursor = connection.cursor()
    create_table_query = """
        CREATE TABLE IF NOT EXISTS example_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        )
    """
    cursor.execute(create_table_query)
    connection.commit()
    connection.close()
    return "Table created successfully"


@bp.post('/insert_record')
def insert_record():
    name = request.json['name']
    connection = get_db_connection()
    cursor = connection.cursor()
    insert_query = "INSERT INTO example_table (name) VALUES (%s)"
    cursor.execute(insert_query, (name,))
    connection.commit()
    connection.close()
    return "Record inserted successfully"


@bp.get('/data')
def data():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM example_table')
    result = cursor.fetchall()
    connection.close()
    return result


# UI route
@bp.get('/')
def index():
    return render_template('index.html')
