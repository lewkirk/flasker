from flask import Flask, render_template

# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')

# FILTERS
#safe
#capitalize
#lower
#upper
#title
#trim
#striptags


def index():
    the_name = "Sir Pedro"
    text = "This is Bold text   "
    grocery_list = ["apples", "juice", 10]
    return render_template("index.html",
        first_name = the_name,
        text = text,
        grocery_list = grocery_list)
# example: localhost:5000/user/John
@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name = name)

# Create Custom Error Pages

# Invalid URL
@app.errorhandler(404)

def page_not_found(e):
    return render_template("404.html"), 404 

# Internal Server Error
@app.errorhandler(500)

def page_not_found(e):
    return render_template("500.html"), 500 
