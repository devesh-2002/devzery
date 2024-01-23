import os
from flask import Flask, jsonify, request, redirect, url_for
from sqlalchemy import desc
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
            username = request.json['username']
            email = request.json['email']
            password = request.json['password']
            new_user = User(username=username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('/dashboard/profile'))

        except Exception as e:
            print(f"Error during registration: {e}")
            db.session.rollback()

    return jsonify({'message': 'User registered successfully'})

@app.route('/dashboard/profile', methods=['GET', 'PUT'])
def user_dashboard():
    if request.method == 'GET':
        user = User.query.order_by(desc(User.id)).first()

        if user:
            return jsonify({'username': user.username, 'email': user.email})
        else:
            return jsonify({'message': 'User not found'}), 404

    elif request.method == 'PUT':
        user = User.query.order_by(desc(User.id)).first()

        if user:
            try:
                new_username = request.json.get('username')
                new_email = request.json.get('email')

                user.username = new_username if new_username else user.username
                user.email = new_email if new_email else user.email

                db.session.commit()

                return jsonify({'message': 'Profile updated successfully'})
            except Exception as e:
                print(f"Error updating profile: {e}")
                db.session.rollback()
                return jsonify({'error': 'Profile update failed'}), 500
        else:
            return jsonify({'message': 'User not found'}), 404

@app.route('/dashboard/profiles', methods=['GET'])
def all_profiles():
    profiles = User.query.all()
    profiles_data = [{'username': profile.username, 'email': profile.email} for profile in profiles]
    return jsonify({'profiles': profiles_data})

if __name__ == '__main__':
    app.run(debug=True)
