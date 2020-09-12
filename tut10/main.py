# blueprints: http://exploreflask.com/en/latest/blueprints.html
from flask import Flask, render_template
# Import the other python file
from admin.second import second


app = Flask(__name__)
# the prefix means don't access any of this unless the url
# has the prefix specified
app.register_blueprint(second, url_prefix="/admin")

@app.route("/")
def test():
    return "<h1>Test</h1>"

if __name__ == "__main__":
    app.run(debug=True)