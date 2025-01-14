from flask import Flask

app = Flask(__name__)

# Index route for web app
@app.route("/")
def index():
    return "hi :)"