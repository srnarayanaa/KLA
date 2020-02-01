from flask import Flask, request, jsonify # Imports the flask library modules
from flask_restful import Resource, Api

app = Flask(__name__) # Single module that grabs all modules executing from this file
api=Api(app)

@app.route('/login', methods=['GET', 'POST']) # HTTP request methods namely "GET" or "POST"
def login():
    data = []
    if request.method == 'POST': # Checks if it's a POST request
        data = [dict(id='1', name='max', email='max@gmail.com')] # Data structure of JSON format
        response = jsonify(data) # Converts your data strcuture into JSON format
        response.status_code = 202 # Provides a response status code of 202 which is "Accepted" 

        return response # Returns the HTTP response
    else:
        data = [dict(id='none', name='none', email='none')] # Data structure of JSON format
        response = jsonify(data) # Converts your data strcuture into JSON format
        response.status_code = 406 # Provides a response status code of 406 which is "Not Acceptable"

        return response # Returns the HTTP response
app.run(debug=True)