# AccuKnox AI/ML Trainee Assignment

This repository contains my solutions for the AccuKnox AI/ML Trainee assessment.

## Assignment 1: Python Programming

### Problem 1: API Data Retrieval and SQLite Storage
- Fetch book information from the Open Library REST API.
- Store book records in a local SQLite database.
- Retrieve and display stored book records.
- Technologies: Python, Requests, SQLite.

### Problem 2: Student Scores and Visualization
- Fetch student scores from a local Flask HTTP API.
- Calculate the average score.
- Visualize individual scores and the average using Matplotlib.
- Technologies: Python, Flask, Requests, Matplotlib, JSON.

**Note:** The student scores are illustrative sample data served by a local API because the assignment did not specify a student-score API.

### Problem 3: CSV Import into SQLite
- Read names and email addresses from a CSV file.
- Store records in a SQLite database.
- Skip duplicate email addresses and display the saved records.
- Technologies: Python, CSV, SQLite.

## Assignment 2: AI and LLM Fundamentals

The `assignment-2/assignment_2_answers.md` file contains:
1. Self-assessment of LLMs, Deep Learning, AI, and Machine Learning.
2. High-level architecture of an LLM chatbot, including an optional RAG extension.
3. Vector databases and the selection of Qdrant for a hypothetical cybersecurity knowledge assistant.

## Project Structure

```text
accuknox-ai-ml-assignment/
├── assignment-1/
│   ├── problem-1-api-books/
│   ├── problem-2-student-scores/
│   └── problem-3-csv-users/
├── assignment-2/
│   └── assignment_2_answers.md
└── README.md
```

## Setup

Use Python 3.10 or later.

Install the required packages:

```bash
python -m pip install requests flask matplotlib
```

SQLite is included with Python's standard library in typical Python installations.

## Running the Programs

### Problem 1

```bash
python assignment-1/problem-1-api-books/api_books_sqlite.py
```

### Problem 2

Start the API in one terminal:

```bash
python assignment-1/problem-2-student-scores/student_api.py
```

Keep it running. In a second terminal, run:

```bash
python assignment-1/problem-2-student-scores/student_scores.py
```

### Problem 3

```bash
python assignment-1/problem-3-csv-users/import_users.py
```

## Notes

- The book program requires an internet connection to access the Open Library API.
- The student API runs locally and serves illustrative sample scores.
- The programs create local SQLite databases and, for Problem 2, a chart image when executed.
- These solutions are intended for the AccuKnox AI/ML Trainee assessment.