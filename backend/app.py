import os
from flask import Flask, jsonify, render_template, request, redirect, url_for
from models import db, User
from dotenv import load_dotenv
from flask_cors import CORS
load_dotenv()

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        try:
            print(request.json['username'],request.json['email'],request.json['password'])
            username = request.json['username']
            email = request.json['email']
            password = request.json['password']
            new_user = User(username=username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('register'))

        except Exception as e:
            print(f"Error during registration: {e}")
            db.session.rollback()

    return jsonify({'message': 'User registered successfully'})

if __name__ == '__main__':
    app.run(debug=True)
