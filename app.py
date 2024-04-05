import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Ben Little in 3308'


@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://db_lab10_user:J15PdkxYRXa2je7IaXRDJDGTKH8pza3u@dpg-co7mocf79t8c73emj0cg-a/db_lab10")
    conn.close()
    return "Database Connection Successful!"

@app.route('/db_create')
def db_create():
    
    conn = psycopg2.connect("postgres://db_lab10_user:J15PdkxYRXa2je7IaXRDJDGTKH8pza3u@dpg-co7mocf79t8c73emj0cg-a/db_lab10")  
    cur = conn.cursor()  
    
    # create basketball table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
        );
        ''')
    
    conn.commit()
    conn.close()

    return "Basketball Table Successfully Created!"
