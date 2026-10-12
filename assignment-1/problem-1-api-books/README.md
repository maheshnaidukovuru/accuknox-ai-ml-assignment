
# Problem 1: API Data Retrieval and SQLite Storage

## Objective
Fetch book records from an external REST API, store them in a local SQLite database, and display the saved records.

## Assumptions
- The problem statement does not specify a particular API, so the Open Library Search API is used.
- The API is queried for up to five books related to Python programming.
- Missing author names are represented as "Unknown author".
- Publication years may be unavailable for some books.

## Technologies
- Python
- Requests
- REST API
- JSON
- SQLite

## Workflow
1. Send an HTTP GET request to the Open Library Search API.
2. Parse the JSON response.
3. Extract the book title, author, and first publication year.
4. Create a SQLite database and books table if they do not exist.
5. Insert the retrieved records using parameterized SQL.
6. Retrieve the stored records using SELECT and display them.

## Database Schema

| Column | Type | Purpose |
|---|---|---|
| id | INTEGER | Primary key |
| title | TEXT | Book title |
| author | TEXT | Author name |
| publication_year | INTEGER | First publication year, when available |

## Setup

Install the required library:

```bash
python -m pip install -r requirements.txt
```

## Run

From the main project folder:

```bash
python assignment-1/problem-1-api-books/api_books_sqlite.py
```

## Output
The program displays the books retrieved from the SQLite database and the number of records displayed.

## Limitations
- An internet connection is required to retrieve books.
- Results depend on the API response.
- Repeated runs currently insert the returned books again.