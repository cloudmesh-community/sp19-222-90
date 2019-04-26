"""
Main module of the server file
"""

from flask import jsonify
import connexion
import pandas as pd

# Create the application instance
app = connexion.App(__name__, specification_dir="./")

# Read the yaml file to configure the endpoints
app.add_api("nfl-analysis.yaml")

# create a URL route in our application for "/"
@app.route("/")
def home():
    msg = "This service provides a prediction of an NFL rookie's performance in 
       Fantasy Football league based upon their performance at the NFL Combine."
    
    return jsonify(msg)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

