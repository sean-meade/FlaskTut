# Template inheretance
# Creates a base template that other templates are bases on
from flask import Flask, redirect, url_for, render_template

# base.html is the parent template. Other html pages (child)
# will inheret this base and maybe overwrite and fill in other 
# stuff.

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", content = "Testing")

if __name__ == "__main__":
    # debug=True means that the page will update automatically
    app.run(debug=True)