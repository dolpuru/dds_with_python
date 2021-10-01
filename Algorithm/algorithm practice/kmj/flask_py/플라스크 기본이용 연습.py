from flask import Flask
app = flask(__name__)
@app.route(__name__)
def hi():
    return"<h1>hi fucking world</h1>"

if __name__ == "__main__":
    app.run(host = "127.0.0.1", port = "8080")
