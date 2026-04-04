from flask import flash, request, jsonify, render_template, Flask
from collections import Counter
from textblob import TextBlob
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/analyze", methods=["POST"])
def analyze():
    print("REQUEST RECEIVED")
    text = request.json["text"]
    words = re.findall(r'\w+', text.lower())
    sentences = re.split(r'\[.!?]',text)

    word_count = len(words)
    sentence_count = len([s for s in sentences if s.strip()!= ""])

    reading_time = round(word_count/200,2)
    common = Counter(words).most_common(5)
    sentiment_score = TextBlob(text).sentiment.polarity

    if sentiment_score > 0.1:
        tone = "postiive"
    elif sentiment_score < -0.1:
        tone = "negative"
    else:
        tone = "neutral"
    return jsonify({
        "word_count": word_count,
        "sentence_count": sentence_count,
        "reading_time": reading_time,
        "common_words": common,
        "tone": tone
    })
if __name__ == "__main__":
    app.run(debug=True)