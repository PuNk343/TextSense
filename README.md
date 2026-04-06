# TextSense — Live Writing Clarity Analyzer

A lightweight NLP-powered web application that analyzes writing in real time.
It evaluates structure, tone, and word patterns to provide immediate feedback as the user types.

---

## Overview

This project demonstrates a simple end-to-end text analysis pipeline:

* Real-time frontend interaction
* Backend processing using Flask
* Basic NLP using TextBlob
* Instant feedback via API communication

The system is designed to reflect how modern applications process and interpret user-generated text dynamically.

---

## Features

* Live word and sentence count
* Estimated reading time
* Sentiment analysis (positive / neutral / negative)
* Most frequent words detection
* Real-time updates as the user types

---

## Tech Stack

* Python (Flask)
* JavaScript (Fetch API)
* HTML / CSS
* TextBlob (NLP)

---

## How It Works

1. User inputs text in the browser
2. JavaScript captures input events
3. Text is sent to the Flask backend via POST request
4. Backend processes:

   * Text cleaning
   * Word and sentence analysis
   * Sentiment scoring
5. Results are returned as JSON
6. Frontend updates the UI instantly

---

## How to Run

1. Install dependencies:

```
pip install flask textblob
```

2. Run the application:

```
python app.py
```

3. Open in browser:

```
http://127.0.0.1:5000
```

---

## Example Output

* Words: 43
* Sentences: 5
* Reading Time: 0.21 min
* Tone: Negative
* Most Common Words: ["i", "way", "no", "hate"]

---

## Purpose

This project is a simplified demonstration of how real-world systems analyze text input in real time.
It highlights core engineering concepts such as:

* Client-server communication
* Event-driven programming
* Text preprocessing
* Basic NLP pipelines

---

## Future Improvements

* Sentence clarity scoring
* Highlighting repeated words in UI
* Phrase-level analysis
* TF-IDF keyword importance
* UI enhancements and visualization

---
