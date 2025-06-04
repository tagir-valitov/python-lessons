@app.route("/login", methods=['POST'])
def login():
    data = request.json
    for user in users:
        if data['login'] == user['login'] and data['password'] == user['password']:
            return jsonify(user), 200
    abort(404, description="User not found or invalid credentials")


@app.route("/signin", methods=['POST'])
def sign_in():
    data = request.json
    for user in users:
        if user['login'] == data['login']:
            return {"status": "User already exists"}, 400
    users.append(data)
    return {"status": "Ok"}, 200 