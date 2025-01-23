from flask import Flask
from flask import render_template

app = Flask(__name__)

# Index route for web app
@app.route("/")
def index():
    return render_template("index.html")

# New functions
@app.route("/about/")
def about():
     mood_current = "good" # declare variable 
     friends_list = ["Eliza", "Courtney", "Lucian", "Alex", "Abby", "Sohan", "Grace"]
     defintions = { "platypus": "a blue-green creature that is very good at solving mysteries", "ladybug": "an apex predator with magical properties", 'giraffe': 'long neck animal with purple tongue' }
     # pass variable into rendered template
     return render_template("about.html", mood = mood_current, friends = friends_list, my_dict=defintions)

@app.route("/contact/")
def contact():
     return render_template("contact.html")

# new route
@app.route("/hello/")
@app.route("/hello/<name_data>")
def hello_there(name_data = None):
    return render_template("hello_there.html", name = name_data)

@app.route("/api/data")
def get_data():
    # displays data file returned from an API call
    # can do more python work to format this later
    return app.send_static_file("data.json")

# Allows you to click "Run" button
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5421)
