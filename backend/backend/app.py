from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

import comment_analyser

# flask app creation
app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
def index():
    return "Hello World"

# api end point ipc-check, takes comment, sends it to coment_analyzer and gets response
@app.route('/api/ipc-check')
def get_bot_response():
    message = request.args.get('comment')
    response = ""
    if message:
        response = comment_analyser.get_comment(message)
        print(response)
        return jsonify(response)
    else:
        return "Missing Data!"


if __name__ == "__main__":
    app.run()
