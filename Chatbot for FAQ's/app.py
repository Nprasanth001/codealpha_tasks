from flask import Flask, render_template, request, jsonify
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

with open("faq_data.json", "r") as file:
    faq_data = json.load(file)

questions = [item["question"] for item in faq_data]

vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    user_question = request.json["message"]

    user_vector = vectorizer.transform([user_question])

    similarity = cosine_similarity(
        user_vector,
        question_vectors
    )

    best_match = similarity.argmax()

    score = similarity[0][best_match]

    if score > 0.2:
        answer = faq_data[best_match]["answer"]
    else:
        answer = "Sorry, I couldn't find an answer."

    return jsonify({
        "answer": answer
    })

if __name__ == "__main__":
    app.run(debug=True)