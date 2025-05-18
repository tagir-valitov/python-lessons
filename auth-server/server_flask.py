from flask import Flask, request, jsonify

# http://127.0.0.1:5000/static/index.html
app = Flask(__name__)
users = []


@app.route("/login", methods=['POST'])
def login():
    # найти в списке user логин и пароль которые прийдут к нам
    data = request.json
    for user in users:
        if data['login'] == user['login'] and data['password'] == user['password']:
            return jsonify(user), 200

    return {"status": "NotFound"}, 404


@app.route("/signin", methods=['POST'])
def sign_in():
    data = request.json
    for user in users:
        if user['login'] == data['login']:
            return {"status": "User already exists"}, 400
    users.append(data)
    return {"status": "Ok"}, 200


@app.route("/logout", methods=['DELETE'])
def log_out():
    data = request.json
    for user in users:
        if user['login'] == data['login'] and user['password'] == data['password']:
            users.remove(user)
            return {"status": "Ok"}, 200
    return {"status": "NotFound"}, 404


if __name__ == '__main__':
    user = {
        "name": "Tagir",
        "birthday": "12.08.2010",
        "gender": "male",
        "mail": "tagirvalitov614@gmail.com",
        "login": "valtag",
        "password": "12345"
    }
    users.append(user)
    app.run(debug=True)
