from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # recebe JSON
    inputs = data.get('inputs', [])

    # Exemplo de perceptron simples
    weights = [0.5, -0.6, 0.3]
    bias = 0.1

    result = sum(w * x for w, x in zip(weights, inputs)) + bias
    output = 1 if result > 0 else 0

    return jsonify({"result": output, "raw": result})

if __name__ == '__main__':
  app.run(port=5000, debug=True)