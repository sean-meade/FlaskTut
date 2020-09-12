from flask import Flask
from flask_restful import Api, Resource

# Initialize app
app = Flask(__name__)
# Wrap app in API - inializing the fact we're using a Restful API
api = Api(app)

# Creating our first resource
# We're going to make a class that is a resource
class HelloWorld(Resource):
    # Over ridden the get method, this is what will happen
    # when we send a specific get request to a url.
    def get(self):
        return {"data": "Hello World"}

# Register as a resource
# Add resource to the api
# The resource we want to add is the class HelloWorld
# and the url will have extension "/"
# Basicly makes a route for the resource
api.add_resource(HelloWorld, "/helloworld")

if __name__ == "__main__":
    # Only use debug for development not when hosting website
    app.run(debug=True)