from flask import Blueprint, render_template

# create variable and set it to Blueprint("name it", 
# import name, path to static folder, path to templates folder )
# __name__ represents the name of the file currently in
second = Blueprint("second", __name__, static_folder="static", template_folder="templates")

# route to this second.py app
@second.route("/home")
@second.route("/")
def home():
    # Access to templates by setting paths to templates folder
    # when creating "second" variable. 
    return render_template("home.html")

@second.route("/test")
def test():
    return "<h1>Testing</h1>"
