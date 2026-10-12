# Problem 3: CSV Users Import into SQLite

## Objective
Read user names and email addresses from a CSV file, store them in a local SQLite database, and display the stored records.

## Technologies
- Python
- CSV module
- SQLite3

## Project Files
- `users.csv` — Sample user records containing names and email addresses.
- `import_users.py` — Reads the CSV, creates the database table, imports records, and displays the saved users.
- `users.db` — SQLite database created by the program.

## Database Schema
The `users` table contains:
- `id` — Integer primary key, automatically generated.
- `name` — User's name, required.
- `email` — User's email address, required and unique.

## How to Run
Open a terminal at the project root and run:

`python assignment-1/problem-3-csv-users/import_users.py`

## Expected Result
The program imports four sample user records and displays their IDs, names, and email addresses.

Repeated runs skip existing email addresses to prevent duplicate records.

## Error Handling
The program handles file errors, invalid CSV data, and SQLite database errors.