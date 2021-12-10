from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello():
    return"<h1>hello world</h1>"

#username을 인자로 받는다
@app.route("/profile/<username>")
def get_profile(username):
    return "profile:" + username

@app.route("/first/<username>")
def get_first(username):
    return "<h2>hello" + username + "!<h2>"

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = '8080')
    