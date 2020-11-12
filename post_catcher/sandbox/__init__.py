from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def do_it():
    request.get_data()
    print('received the thing', request.data)
    return 'Hello, World'
