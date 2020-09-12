from flask import Flask, render_template, request, url_for, redirect

# GET is a way of getting information to a website.
# POST is a way of doing it securely.

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# You can specify different methods that will be used in this page
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")


@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    app.run(debug=True)