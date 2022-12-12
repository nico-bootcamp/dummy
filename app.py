# Import the Flask class from the flask module
from flask import Flask

# Create a new Flask app
app = Flask(__name__)

# Define a route for the default URL
@app.route('/')
def hello():
    # Return the string "Hello, World!" to the user
    return "Hello, World!"

# Run the app if it is the main module
if __name__ == '__main__':
    app.run()
    
