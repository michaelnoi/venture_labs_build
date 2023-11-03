from flask import Flask
import requests

# Create a Flask application
app = Flask(__name__)

# Define a route and its associated function
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/<name>')
def hello_name(name):
    return f'Hello, {name}'


@app.route('/api')
def request():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        # Parse the JSON response into a Python dictionary.
        data = response.json()
        return data
    else:
        # If the request was not successful, print an error message with the status code.
        return f"API Request Failed with Status Code: {response.status_code}"


# Run the Flask application
if __name__ == '__main__':
    app.run()
