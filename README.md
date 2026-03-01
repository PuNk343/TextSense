# Resume Keyword Scanner

A lightweight text-processing tool that compares a job description with a resume to identify missing technical keywords.

This project demonstrates structured problem decomposition, basic natural language preprocessing, and set-based comparison logic — applied to a real internship use case.

---

## Overview

Modern Applicant Tracking Systems (ATS) rely heavily on keyword matching.
This tool simulates a simplified version of that logic.

Given:

* A job description
* A resume

It extracts meaningful words from both, removes common filler terms, and highlights keywords present in the job description but absent from the resume.

---

## Core Concepts Demonstrated

* Text preprocessing (lowercasing, punctuation removal)
* Stopword filtering
* Basic keyword extraction
* Set operations for comparison
* Debugging and file handling
* Practical application of string processing

---

## Project Structure

```
ResumeKeywordScanner/
│
├── scanner.ipynb
├── sample_job.txt
├── sample_resume.txt
└── README.md
```

---

## How It Works

1. Load job description and resume text files
2. Normalize and clean text
3. Remove common stopwords
4. Extract candidate keywords
5. Compute set difference
6. Display missing keywords and total count

---

## How to Run

1. Place job description text in `job.txt`
2. Place resume text in `resume.txt`
3. Run `scanner.ipynb`
4. Review the missing keyword output

---

## Why This Project Matters

This project transforms an abstract internship struggle into a measurable process.

Instead of guessing why a resume fails to get shortlisted, it provides a structured way to analyze keyword alignment — bridging the gap between application and optimization.
