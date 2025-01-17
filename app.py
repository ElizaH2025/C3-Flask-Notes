from flask import Flask
from flask import render_template

app = Flask(__name__)

# Index route for web app
@app.route("/")
def index():
    return "hi :)"

# new route
@app.route("/hello/")
@app.route("/hello/<name_data>")
def hello_there(name_data = None):
    return render_template("hello_there.html", name = name_data)

# Allows you to click "Run" button
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)