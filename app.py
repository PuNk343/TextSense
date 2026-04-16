from flask import Flask, request, jsonify, render_template
from collections import Counter
from textblob import TextBlob
from transformers import pipeline
import re

app = Flask(__name__)
sentiment_model = pipeline("sentiment-analysis")

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/analyze", methods=["POST"])
def analyze():
    text = request.json["text"]
    words = re.findall(r'\w+', text.lower())
    sentences = re.split(r'[.!?]+', text)
    word_count = len(words)
    sentence_count = len([s for s in sentences if s.strip()!=""])
    reading_time = round(word_count/200,2)
    common = Counter(words).most_common(5)
    basic_score = TextBlob(text).sentiment.polarity
    model_result = sentiment_model(text[:512])[0]
    model_label = model_result["label"]
    model_score = round(model_result["score"],2)
    if model_label=="POSITIVE":
        tone="Positive"
        tone_message=f"Neural model detects a positive tone with {int(model_score*100)}% confidence."
    else:
        tone="Negative"
        tone_message=f"Neural model detects a negative tone with {int(model_score*100)}% confidence."
    text_lower = text.lower()
    if "dear" in text_lower or "regards" in text_lower:
        format_type="Letter"
        format_suggestion="Dear [Name],\n\n[Opening]\n\n[Main Content]\n\n[Closing]\n\nRegards,\n[Your Name]"
    elif "hello" in text_lower or "hi" in text_lower:
        format_type="Casual Message"
        format_suggestion="Start with a greeting, keep it short, and clearly state your message."
    else:
        format_type="General Writing"
        format_suggestion="Structure your text with an introduction, body, and conclusion."
    return jsonify({
        "word_count":word_count,
        "sentence_count":sentence_count,
        "reading_time":reading_time,
        "common_words":common,
        "tone":tone,
        "tone_message":tone_message,
        "model_confidence":model_score,
        "format_type":format_type,
        "format_suggestion":format_suggestion
    })

if __name__=="__main__":
    app.run(debug=True)
