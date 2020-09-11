from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# With the html page (index.html in the folder templates)
# we can call this in the return by using render_template
# With {{}} in the html file you can use an input in html 
# page. So with {{content}} in the html file, using ", 
# content = name" allows the page to display the name.
@app.route("/<name>")
def home(name):
    return render_template("index.html", content = name, r = ["tim", "joe", "bill"])

if __name__ == "__main__":
    app.run()