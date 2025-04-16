
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Witaj w moim API!"})

@app.route('/mojastrona')
def moja_strona():
    return jsonify({"message": "To jest moja strona!"})

@app.route('/hello')
def hello():
    name = request.args.get('name')
    if name:
        msg = f"Hello {name}!"
    else:
        msg = "Hello!"
    return msg 

@app.route('/api/v1.0/predict')
def predict():
    num1 = float(request.args.get('num1', 0))
    num2 = float(request.args.get('num2', 0))
    total = num1 + num2
    prediction = int(total > 5.8)

    return jsonify({
        "prediction": prediction,
        "features": {"num1": num1, "num2": num2}
    })

if __name__ == '__main__':
    app.run()
