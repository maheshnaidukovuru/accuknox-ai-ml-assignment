import csv
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).parent
CSV_FILE = BASE_DIR / "users.csv"
DB_FILE = BASE_DIR / "users.db"


def create_database(connection):
    connection.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    """)
    connection.commit()


def import_users(connection):
    with CSV_FILE.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames or not {"name", "email"}.issubset(
            reader.fieldnames
        ):
            raise ValueError("CSV must contain name and email columns.")

        imported = 0

        for row in reader:
            name = (row.get("name") or "").strip()
            email = (row.get("email") or "").strip()

            if not name or not email:
                print("Skipping a row with missing name or email.")
                continue

            cursor = connection.execute(
                "INSERT OR IGNORE INTO users (name, email) VALUES (?, ?)",
                (name, email)
            )

            if cursor.rowcount == 1:
                imported += 1

        connection.commit()
        return imported


def display_users(connection):
    rows = connection.execute(
        "SELECT id, name, email FROM users ORDER BY id"
    ).fetchall()

    print("\nUsers stored in SQLite")
    print("-" * 50)

    for user_id, name, email in rows:
        print(f"ID: {user_id} | Name: {name} | Email: {email}")

    print("-" * 50)
    print(f"Total users in database: {len(rows)}")


def main():
    try:
        with sqlite3.connect(DB_FILE) as connection:
            create_database(connection)
            imported = import_users(connection)
            print(f"New users imported: {imported}")
            display_users(connection)

    except (OSError, sqlite3.Error, ValueError, csv.Error) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()