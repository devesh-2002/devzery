import os
import psycopg2
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
load_dotenv()

db = SQLAlchemy()

conn = psycopg2.connect(
        host="localhost",
        database=os.environ['DB_NAME'],
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])

cur = conn.cursor()
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
