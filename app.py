from flask import Flask, render_template, request, jsonify

import comment_analyser

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('legal.html')


@app.route('/get')
def get_bot_response():
    message = request.args.get('msg')
    response = ""
    if message:
        response = comment_analyser.generate_response(message)
        return str(response)
    else:
        return "Missing Data!"


if __name__ == "__main__":
    app.run()