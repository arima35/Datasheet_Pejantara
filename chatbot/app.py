from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Inisialisasi Flask
app = Flask(__name__)
CORS(app)

# Load intents
with open('intents_indo.json', 'r') as f:
    intents = json.load(f)

# Preprocessing intents
patterns = [pattern.lower() for intent in intents['intents'] for pattern in intent['patterns']]
responses = [intent['responses'] for intent in intents['intents'] for _ in intent['patterns']]

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(patterns)

# Fungsi untuk mencocokkan pertanyaan
def get_response(user_input):
    user_input_vector = vectorizer.transform([user_input.lower()])
    similarities = cosine_similarity(user_input_vector, tfidf_matrix)
    max_similarity_index = similarities.argmax()
    max_similarity_score = similarities[0, max_similarity_index]
    
    if max_similarity_score > 0.5:  # Threshold untuk relevansi
        return responses[max_similarity_index][0]
    else:
        return "Maaf, saya belum memahami pertanyaan Anda."

# Endpoint Flask
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    response = get_response(user_message)
    return jsonify({"response": response})

# Jalankan Flask
if __name__ == '__main__':
    app.run(debug=True)
