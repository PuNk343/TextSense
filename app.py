from flask import Flask, request, jsonify, render_template
from collections import Counter
from textblob import TextBlob
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/analyze", methods=["POST"])
def analyze():
    text = request.json["text"]

    words = re.findall(r'\w+', text.lower())
    sentences = re.split(r'[.!?]+', text)

    word_count = len(words)
    sentence_count = len([s for s in sentences if s.strip() != ""])

    reading_time = round(word_count / 200, 2)
    common = Counter(words).most_common(5)

    sentiment_score = TextBlob(text).sentiment.polarity

    if sentiment_score > 0.3:
        tone = "Strongly Positive"
    elif sentiment_score > 0.1:
        tone = "Positive"
    elif sentiment_score < -0.3:
        tone = "Strongly Negative"
    elif sentiment_score < -0.1:
        tone = "Negative"
    else:
        tone = "Neutral"

    tone_score = round(sentiment_score, 2)

    if tone_score > 0.2:
        tone_message = "Your writing conveys a positive and confident tone."
    elif tone_score < -0.2:
        tone_message = "Your writing may come across as negative or critical."
    else:
        tone_message = "Your tone is fairly neutral. Consider adding more emotion or clarity."

    text_lower = text.lower()

    if "dear" in text_lower or "regards" in text_lower:
        format_type = "Letter"
        format_suggestion = "Dear [Name],\n\n[Opening]\n\n[Main Content]\n\n[Closing]\n\nRegards,\n[Your Name]"
    elif "hello" in text_lower or "hi" in text_lower:
        format_type = "Casual Message"
        format_suggestion = "Start with a greeting, keep it short, and clearly state your message."
    else:
        format_type = "General Writing"
        format_suggestion = "Structure your text with an introduction, body, and conclusion."

    return jsonify({
        "word_count": word_count,
        "sentence_count": sentence_count,
        "reading_time": reading_time,
        "common_words": common,
        "tone": tone,
        "tone_score": tone_score,
        "tone_message": tone_message,
        "format_type": format_type,
        "format_suggestion": format_suggestion
    })

if __name__ == "__main__":
    app.run(debug=True)
