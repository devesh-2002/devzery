import os
from flask import Flask, render_template, request, redirect, url_for
from models import db, User
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            new_user = User(username=username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('register'))

        except Exception as e:
            print(f"Error during registration: {e}")
            db.session.rollback()

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
