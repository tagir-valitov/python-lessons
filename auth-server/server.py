from flask import Flask, request, jsonify

# http://127.0.0.1:5000/static/index.html
app = Flask(__name__)
users = [
    {
        "name": "Tagir",
        "birthday": "2010-12-08",
        "gender": "male",
        "mail": "tagirvalitov614@gmail.com",
        "login": "valtag",
        "password": "12345"
    },
    {
        "name": "Rishat",
        "birthday": "1996-27-07",
        "gender": "male",
        "mail": "rishat@gmail.com",
        "login": "rishat",
        "password": "54321"
    }
]


@app.route("/login", methods=['POST'])
def login():
    # найти в списке user логин и пароль, которые прейдут к нам
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

@app.route("/update", methods=['POST'])
def update():
    data = request.json
    for user in users:
        if user['login'] == data['login']:
            user['name'] = data['name']
            user['birthday'] = data['birthday']
            user['gender'] = data['gender']
            user['mail'] = data['mail']
            user['password'] = data['password']

            return {"status": "Ok"}, 200
    return {"status": "NotFound"}, 404


@app.route("/delete", methods=['DELETE'])
def delete():
    data = request.json
    for user in users:
        if user['login'] == data['login'] and user['password'] == data['password']:
            users.remove(user)
            return {"status": "Ok"}, 200
    return {"status": "NotFound"}, 404


if __name__ == '__main__':
    app.run(debug=True)
