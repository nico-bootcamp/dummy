# Import the Flask class from the flask module
from flask import Flask
import pandas as pd

# Create a new Flask app
app = Flask(__name__)

# Define a route for the default URL
@app.route('/')
def orders():
    data = pd.read_csv('orderdata.csv')
    header = "<html><title>Flask App</title><h1>Orders Table:</h1><body>"
    footer = "</body></html>"
    return header + data.to_html(index=False, index_names=False) + footer

# Run the app if it is the main module
if __name__ == '__main__':
    app.run()
