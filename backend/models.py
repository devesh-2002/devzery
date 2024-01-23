import os
import psycopg2
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
load_dotenv()

db = SQLAlchemy()

try:
    conn = psycopg2.connect(
        host="localhost",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'],
        database=os.environ['DB_NAME']
    )
    conn.close()
except psycopg2.OperationalError:
    conn = psycopg2.connect(
        host="localhost",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD']
    )
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(f"CREATE DATABASE {os.environ['DB_NAME']}")
    conn.close()

conn = psycopg2.connect(
    host="localhost",
    user=os.environ['DB_USERNAME'],
    password=os.environ['DB_PASSWORD'],
    database=os.environ['DB_NAME']
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
