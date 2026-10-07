import os

from dotenv import load_dotenv
from flask import Flask, render_template, request
import pymysql

# Load variables from .env into the environment (real env vars take precedence)
load_dotenv()

app = Flask(__name__)
app.config.from_mapping(
    DB_HOST=os.environ['DB_HOST'],
    DB_PORT=int(os.environ.get('DB_PORT', 3306)),
    DB_USER=os.environ['DB_USER'],
    DB_PASSWORD=os.environ['DB_PASSWORD'],
    DB_NAME=os.environ['DB_NAME'],
)

def get_db_connection():
    connection = pymysql.connect(host=app.config['DB_HOST'],
                                 port=app.config['DB_PORT'],
                                 user=app.config['DB_USER'],
                                 password=app.config['DB_PASSWORD'],
                                 database=app.config['DB_NAME'],
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection

@app.get('/health')
def health():
    return "Up & Running"

@app.get('/create_table')
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

@app.post('/insert_record')
def insert_record():
    name = request.json['name']
    connection = get_db_connection()
    cursor = connection.cursor()
    insert_query = "INSERT INTO example_table (name) VALUES (%s)"
    cursor.execute(insert_query, (name,))
    connection.commit()
    connection.close()
    return "Record inserted successfully"

@app.get('/data')
def data():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM example_table')
    result = cursor.fetchall()
    connection.close()
    return result

# UI route
@app.get('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Debug mode is controlled by FLASK_DEBUG in .env
    app.run(host='0.0.0.0', port=int(os.environ.get('APP_PORT', 8000)) )
