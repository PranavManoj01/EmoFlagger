import joblib
from flask import Flask, request, jsonify, render_template

# Updated paths
model = joblib.load("../models/emoflagger_model.pkl")
vectorizer = joblib.load("../models/tfidf_vectorizer.pkl")
# Label mapping
id2label = {0: "negative", 1: "neutral", 2: "positive"}

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if "text" not in data:
        return jsonify({"error": "Missing 'text' in request body"}), 400

    user_input = data["text"]
    transformed_input = vectorizer.transform([user_input])

        # Predict label and probability
    prediction = model.predict(transformed_input)[0]
    proba = model.predict_proba(transformed_input)[0]
    confidence = round(proba[prediction] * 100, 2)  # as percentage with 2 decimals

    sentiment = id2label[prediction]

    return jsonify({
    "sentiment": sentiment,
    "confidence": confidence
})


if __name__ == "__main__":
    app.run(debug=True)
