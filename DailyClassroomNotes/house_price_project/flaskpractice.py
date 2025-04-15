from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to flask, I do not want to live"


app.run(host = "127.0.0.1", port = 5000)