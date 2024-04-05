import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://db_lab10_user:J15PdkxYRXa2je7IaXRDJDGTKH8pza3u@dpg-co7mocf79t8c73emj0cg-a/db_lab10")
    conn.close()
    return "Database Connection Successful!"