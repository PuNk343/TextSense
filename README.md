# TextSense — Real-Time Writing Clarity Analyzer

A lightweight, full-stack web application that analyzes written text in real time.
It evaluates structure, tone, and lexical patterns to provide immediate feedback as the user types.

---

## Overview

TextSense is designed as a minimal yet complete demonstration of a real-time text processing system.

The application captures user input dynamically, processes it through a backend NLP pipeline, and updates the interface instantly. It reflects how modern systems handle continuous user-generated data with low latency.

---

## Key Features

* Live word and sentence count
* Estimated reading time
* Sentiment classification (Positive / Neutral / Negative)
* Frequency analysis of most common words
* Dynamic UI updates with tone-based visual feedback

---

## System Architecture

The application follows a simple client–server model:

User Input → JavaScript Event → HTTP Request → Flask Backend → NLP Processing → JSON Response → UI Update

---

## Tech Stack

* **Backend:** Python (Flask)
* **Frontend:** HTML, CSS, JavaScript
* **NLP:** TextBlob
* **Communication:** REST API (JSON over HTTP)

---

## How It Works

1. The user types into a textarea in the browser
2. JavaScript listens for input events
3. Each input triggers an asynchronous POST request to the backend
4. The Flask server processes the text:

   * tokenizes words using regex
   * splits sentences
   * computes frequency distributions
   * evaluates sentiment using TextBlob
5. The server returns structured data in JSON format
6. The frontend updates the interface in real time

---

## Running the Project

1. Install dependencies:

```
pip install flask textblob
```

2. Start the server:

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
* Common Words: i (5), way (4), no (3), hate (2)

---

## Design Notes

* The system is intentionally lightweight and avoids heavy NLP frameworks
* Combines rule-based text processing with a pretrained sentiment model
* Designed for clarity, responsiveness, and minimal latency

---

## Limitations

* Sentence segmentation is regex-based and may be imprecise
* Frequent API calls (one per keystroke) may impact performance
* Stopword filtering is minimal
* No phrase-level or contextual analysis

---

## Future Improvements

* Input debouncing to reduce request frequency
* Enhanced sentence parsing
* Stopword filtering and keyword weighting
* Phrase-level analysis (n-grams)
* Clarity scoring system
* Improved UI/UX and visualization

---

## Purpose

This project demonstrates the transition from static scripts to interactive systems.
It focuses on understanding how frontend interaction, backend processing, and real-time communication integrate into a cohesive application.

---
