from flask import Flask, request,jsonify

app = Flask(__name__)
users = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    try:
        username = data['username']
        password = data['password']
        if username in users:
            raise ValueError("Username already taken, please try again")
        users[username] = password
        return {'message': 'Registration successful!'}
    except (KeyError, TypeError):
        return jsonify({'error': 'ERROR!! Please provide a JSON object containing a username and password.'})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    try:
        username = data['username']
        password = data['password']
        if username in users and users[username] == password:
            return {'message': 'Access granted!'}
            #of course normally here I would also return a token of access
        else:
            return {'message': 'Access denied!'}
            #and here a simple check for number of logins trials in the last 24 hours
    except (KeyError, TypeError):
        return jsonify({'error': 'ERROR!! Please provide a JSON object containing a username and password.'})