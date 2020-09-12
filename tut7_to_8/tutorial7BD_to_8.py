# Databases and updating users
from flask import Flask, render_template, request, url_for, redirect, session, flash
from datetime import timedelta
# SQLAlchemy allows you to write in python for the database querys
from flask_sqlalchemy import SQLAlchemy

# Need to install SQLAlchemy with "pip install flask-sqlalchemy"

app = Flask(__name__)
app.secret_key = "hello"
# users on this line is the name of the database you'll be using
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.permanent_session_lifetime = timedelta(minutes=5)

# Setup database object like an sql database
db = SQLAlchemy(app)

# Need to create a modal to store information in
class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    # dont need the "name" it will use the variable name
    name = db.Column("name", db.String(100))
    email = db.Column("email", db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/view")
def view():
    return render_template("view.html", values=users.query.all())

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        found_user = users.query.filter_by(name=user).first()
        # To delete something from the table:
        # found_user = users.query.filter_by(name=user).delete()
        # db.session.commit()
        # for multiple deletes:
        # for user in found_user:
        #       user.delete()
        
        
        # Check to see if user already exists
        if found_user:
            # Grab the users email
            session["email"] = found_user.email
        
        # If it doesnt create one
        else:
            # Use the class to create user and email is blank becasue
            # there is none yet
            usr = users(user, "")
            # add usr to database
            db.session.add(usr)
            # commit these changes
            db.session.commit()

        flash("Login Successful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged in.")
            return redirect(url_for("user"))
        return render_template("login.html")

# Adding a method to user
@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = users.query.filter_by(name=user).first()
            # change email
            found_user.email = email
            # save email
            db.session.commit()
            
            flash("Email was saved.")
        else:
            if "email" in session:
                email = session["email"]
        return render_template("user.html", email=email)
    else:
        flash("You are not logged in.")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    flash("You have been logged out!", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    # creates database if it's not already created
    db.create_all()
    app.run(debug=True)