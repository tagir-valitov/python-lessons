from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
from http import HTTPStatus
import os

# http://127.0.0.1:5000/static/index.html


app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['POSTGRESQL']
db = SQLAlchemy(app)


# users = [
#     {
#         "name": "Tagir",
#         "birthday": "2010-12-08",
#         "gender": "male",
#         "mail": "tagirvalitov614@gmail.com",
#         "login": "valtag",
#         "password": "12345"
#     },
#     {
#         "name": "Rishat",
#         "birthday": "1996-27-07",
#         "gender": "male",
#         "mail": "rishat@gmail.com",
#         "login": "rishat",
#         "password": "54321"
#     }
# ]

class User(db.Model):
    __tablename_ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    birthday = db.Column(db.String(10), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    mail = db.Column(db.String(120), unique=True, nullable=False)
    login = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "birthday": self.birthday,
            "gender": self.gender,
            "mail": self.mail,
            "login": self.login,
            "password": self.password
        }
with app.app_context():
    db.create_all()

@app.route("/login", methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(login=data['login']).first()
    if user and check_password_hash(user.password, data['password']):
        return jsonify(user.to_dict()), 200
    return {"status": "NotFound"}, 404

@app.route("/signin", methods=['POST'])
def sign_in():
    data = request.json
    if User.query.filter_by(login=data['login']).first():
        return {"status": "User already exists"}, 400

    hashed_password = generate_password_hash(data['password'])
    new_user = User(
        name=data['name'],
        birthday=data['birthday'],
        gender=data['gender'],
        mail=data['mail'],
        login=data['login'],
        password=hashed_password
    )

    db.session.add(new_user)
    db.session.commit()
    return {"status": "Ok"}, 200

@app.route("/update", methods=['POST'])
def update():
    data = request.json
    user = User.query.filter_by(login=data['login']).first()
    if user:
        user.name = data['name']
        user.birthday = data['birthday']
        user.gender = data['gender']
        user.mail = data['mail']
        user.password = generate_password_hash(data['password'])

        db.session.commit()
        return {"status": "Ok"}, 200
    return {"status": "NotFound"}, 404

@app.route("/delete", methods=['DELETE'])
def delete():
    data = request.json
    user = User.query.filter_by(login=data['login']).first()

    if user and check_password_hash(user.password, data['password']):
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted"}), HTTPStatus.OK

    return jsonify({"message": "Failed"}), HTTPStatus.UNAUTHORIZED

if __name__ == '__main__':
    app.run(debug=True)