from website import create_app
from flask import Flask, render_template, request, jsonify
from chat import get_response

app = create_app()

@app.route("/bot_response", methods=["POST"])
def predict():
    text = request.get_json().get("sent_message")
    response_text = get_response(text)
    return jsonify(message=response_text)

if __name__ == '__main__':
    app.run(debug=True)