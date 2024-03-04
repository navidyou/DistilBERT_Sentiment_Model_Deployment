
from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load the model
nlp = pipeline("sentiment-analysis", model="distilbert-base-uncased")

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = request.get_json(force=True)
        prediction = nlp(data['text'])
        return jsonify(prediction)

if __name__ == '__main__':
    app.run(debug=True)
