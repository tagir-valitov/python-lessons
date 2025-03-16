# Смотри у тебя 4 страницы, если пользователь не зарегистрирован то показываешь страничку с логином,
# там есть кнопка зарегистрироваться которая ведет на страницу регистрации. Если пользователь залогинен то показываешь
# страницу его профиля
# и там есть кнопка редактировать которая ведет на страницу редактирования профил
# я и есть кнопка выйти которая разлогинивает

from flask import Flask, request, jsonify

app = Flask(__name__)
users = []



@app.route("/login")
def login():
    data = request.json
    return jsonify(data)

@app.route("/signin")
def sign_in():
    data = request.json
    users.append(data)
    print(users)
    return {"status":"Ok"}, 200




if __name__ == '__main__':
    app.run(debug=True)