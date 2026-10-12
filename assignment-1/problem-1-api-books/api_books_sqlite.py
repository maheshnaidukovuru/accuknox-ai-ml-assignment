
import sqlite3
import requests

# 1. External API configuration
API_URL = "https://openlibrary.org/search.json"

params = {
    "q": "python programming",
    "limit": 5
}


def fetch_books():
    """Fetch book records from the Open Library API."""
    response = requests.get(API_URL, params=params, timeout=20)
    response.raise_for_status()

    data = response.json()
    books = []

    for book in data.get("docs", []):
        title = book.get("title") or "Unknown title"

        authors = book.get("author_name") or []
        author = ", ".join(authors) if authors else "Unknown author"

        year = book.get("first_publish_year")

        books.append((title, author, year))

    return books


def create_database():
    """Create the SQLite database and books table."""
    connection = sqlite3.connect("books.db")

    connection.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            publication_year INTEGER
        )
    """)

    connection.commit()
    return connection


def save_books(connection, books):
    """Insert API records into SQLite."""
    connection.executemany("""
        INSERT INTO books (title, author, publication_year)
        VALUES (?, ?, ?)
    """, books)

    connection.commit()


def display_books(connection):
    """Retrieve and display records from SQLite."""
    rows = connection.execute("""
        SELECT id, title, author, publication_year
        FROM books
        ORDER BY id
    """).fetchall()

    print("\nBooks stored in SQLite")
    print("-" * 60)

    for book_id, title, author, year in rows:
        print(f"ID: {book_id}")
        print(f"Title: {title}")
        print(f"Author: {author}")
        print(f"Publication Year: {year if year is not None else 'Unknown'}")
        print("-" * 60)

    print(f"Total books displayed: {len(rows)}")


def main():
    connection = None

    try:
        books = fetch_books()
        print(f"Fetched {len(books)} books from the API.")

        connection = create_database()
        save_books(connection, books)
        display_books(connection)

    except requests.RequestException as error:
        print(f"API request failed: {error}")

    except sqlite3.Error as error:
        print(f"Database error: {error}")

    finally:
        if connection is not None:
            connection.close()


if __name__ == "__main__":
    main()
