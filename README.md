# TextSense — Real-Time Writing Clarity & Tone Analyzer

TextSense is a lightweight full-stack web application that analyzes written text in real time and provides structured feedback on clarity, tone, and writing format.

It goes beyond basic metrics by interpreting user input and offering actionable suggestions, making it a step toward intelligent writing assistance systems.

---

## Overview

TextSense captures user input dynamically and processes it through a backend NLP pipeline. The system evaluates textual structure, sentiment, and writing patterns, then returns both analytical insights and improvement suggestions instantly.

This project demonstrates how modern applications handle continuous user input with real-time feedback loops.

---

## Key Features

### Core Analysis

* Live word count
* Sentence count
* Estimated reading time
* Most frequent words detection

### Tone Analysis

* Multi-level sentiment classification:

  * Strongly Positive
  * Positive
  * Neutral
  * Negative
  * Strongly Negative
* Tone confidence score
* Contextual tone interpretation

### Writing Assistance

* Automatic format detection:

  * Letter
  * Casual message
  * General writing
* Suggested structure templates based on detected format

### User Experience

* Real-time updates on every keystroke
* Color-coded tone feedback
* Clean and minimal dark-themed interface

---

## System Architecture

The application follows a client–server architecture with a continuous feedback loop:

User Input
→ JavaScript Event Listener
→ HTTP POST Request
→ Flask Backend
→ NLP Processing (Regex + TextBlob)
→ JSON Response
→ Dynamic UI Update

---

## Tech Stack

* **Backend:** Python (Flask)
* **Frontend:** HTML, CSS, JavaScript
* **NLP:** TextBlob + regex-based processing
* **Communication:** REST API (JSON over HTTP)

---

## How It Works

1. The user types into a browser textarea
2. JavaScript captures input events in real time
3. Each input triggers an asynchronous POST request
4. The Flask backend processes the text:

   * tokenizes words using regex
   * splits sentences
   * computes frequency distributions
   * evaluates sentiment using TextBlob
   * classifies tone and generates interpretation
   * detects writing format and suggests structure
5. The server returns structured data as JSON
6. The frontend updates the interface instantly

---

## Running the Project

1. Install dependencies:

```id="run1"
pip install flask textblob
```

2. Start the server:

```id="run2"
python app.py
```

3. Open in browser:

```id="run3"
http://127.0.0.1:5000
```

---

## Example Output

* Words: 52
* Sentences: 4
* Reading Time: 0.26 min
* Tone: Strongly Negative
* Tone Insight: “Your writing may come across as negative or critical.”
* Detected Format: Letter
* Suggested Structure:

  ```
  Dear [Name],

  [Opening]

  [Main Content]

  [Closing]

  Regards,
  [Your Name]
  ```

---

## Design Philosophy

* Minimal dependencies, maximum clarity
* Combination of rule-based and model-based NLP
* Focus on real-time responsiveness
* Emphasis on interpretability over complexity

---

## Limitations

* Sentence segmentation is regex-based and may not handle edge cases
* High request frequency (per keystroke) can impact performance
* Format detection is rule-based and not context-aware
* No deep semantic understanding or rewriting capability

---

## Future Improvements

* Input debouncing to optimize performance
* Advanced sentence parsing and grammar checks
* Stopword filtering and keyword weighting
* Phrase-level analysis (n-grams)
* Clarity scoring system
* AI-based rewriting suggestions
* Deployment to cloud for public access

---

## Purpose

This project demonstrates the evolution from static scripts to interactive, intelligent systems.

It highlights how frontend interaction, backend processing, and NLP techniques can be combined to build real-time user-facing tools.

---
