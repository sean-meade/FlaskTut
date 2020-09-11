from flask import Flask, redirect, url_for

# Create an instence of flask web application
app = Flask(__name__)

# create pages of website
# Create homepage
# Need to define for flask how to access this page
# To tell flask where to look we give it a route:
# We decorate the function as follows 
# The "/" will send to homepage but can also put in "/about"
# or "/contact" for different pages.
@app.route("/")
def home():
    # Can add inline html when returning it from a function
    return "Hello this is the main page <h1>HELLO</h1>"

# A few more things on routing
# Create another page
# You can use the following to add a parameter to the pag 
# function
@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

# To redirect someone to a different page if they are not
# authurized
# Having /admin/ allows both /admin and /admin/ to be pages
# with
@app.route("/admin/")
def admin():
    # Using a redirect to redirect to home
    # return redirect(url_for("home"))
    # Using a redirect to redirect to a page with a paramiter
    return redirect(url_for("user", name = "Admin!"))

# run the app
if __name__ == "__main__":
    app.run()