from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sum', methods=['POST'])
def sum_numbers():
    data = request.get_json()
    try:
        numbers = data['numbers']
        if not all(num.isnumeric() for num in numbers): #here I can use isnumeric because these are ints, otherwise would need to change the way I check
            raise ValueError('ERROR!! Please make sure values are integers.')
        return jsonify({'sum': sum(numbers)})
    except (KeyError, TypeError):
        return jsonify({'error': 'ERROR!! Please provide a JSON object containing a list of integers.'})

@app.route('/concatenate', methods=['POST'])
def concat_strings():
    data = request.get_json()
    try:
        first = data['first']
        second = data['second']
        return jsonify({'result': first + second})
    
    except (KeyError, TypeError):
        return jsonify({'error': 'ERROR!! Please provide a JSON object containing two strings called first and second.'})
