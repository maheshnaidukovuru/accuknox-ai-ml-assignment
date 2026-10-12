# Problem 2: Student Scores and Visualization

## Objective
Fetch student test scores from an HTTP API, calculate the average score, and visualize individual scores using a bar chart.

## Assumption
The assignment does not specify a student-score API. Therefore, a local Flask API serves sample student records stored in `students.json`. These scores are illustrative test data, not real student results.

## Workflow
1. Flask exposes student records through the `GET /api/students` endpoint.
2. Python Requests fetches and parses the JSON response.
3. The program calculates the arithmetic mean of the student scores.
4. Matplotlib creates a bar chart with an average reference line.
5. The chart is saved as `student_scores.png`.

## Technologies
- Python
- Flask
- Requests
- Matplotlib
- JSON

## How to Run
Install dependencies:

`python -m pip install flask requests matplotlib`

Start the API in the first terminal:

`python assignment-1/problem-2-student-scores/student_api.py`

Keep that terminal running. Open a second terminal and execute:

`python assignment-1/problem-2-student-scores/student_scores.py`

## Sample Result
- Number of students: 5
- Average score: 81.00

The program displays the scores and generates a bar chart.

## Limitation
The API runs locally on the computer, and the dataset contains sample scores. No external student-score service was specified in the assignment.