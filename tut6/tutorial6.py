# Message Flashing
# Doing a login where the user goes to one page and the previous
# webpage is gone.
from flask import Flask, render_template, request, url_for, redirect, session, flash
# You can cause data to be saved for longer using datetime
from datetime import timedelta

app = Flask(__name__)
# All session data that is stored is encripted on the server
# we need to define a secret key in order to decrpt and encript this data
app.secret_key = "hello"
# This is how you set up for data to help for long or permenently
# can have days= as well
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
    return render_template("index.html")

# You can specify different methods that will be used in this page
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        # Set session to be kept for as long as set above
        session.permanent = True
        user = request.form["nm"]
        # A session stores data as a dictionary
        # To create a new piece of information in the session:
        # session["name dictionary key will be"] = value
        session["user"] = user
        flash("Login Successful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged in.")
            return redirect(url_for("user"))
        return render_template("login.html")


@app.route("/user")
def user():
    # Make sure someone has loged in and not just gone to
    # /user part of website
    # if "name of session key" in session
    # Make a dictionary key (which in this case is "user") put it 
    # inside a session (which is imported above and used in login).
    # Set this session to a value and the you can access it after 
    # you check it exists.
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
    else:
        flash("You are not logged in.")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    flash("You have been logged out!", "info")
    # remove data from session
    session.pop("user", None)
    # A message will flash notifying user they logged out,
    # then category (optional) in this case "info" (also have
    # "warning" and "error") that will show relavent icons
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)