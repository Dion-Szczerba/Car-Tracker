import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "data" / "car.db"

def get_connection():
    #Open a connection to the SQLite database
    DB_PATH.parent.mkdir(exist_ok=True) # create data/ if it is missing
    connection = sqlite3.connect(DB_PATH)

    #Dictionary Cursor
    connection.row_factory = sqlite3.Row

    connection.execute("PRAGMA foreign_keys = ON") # Switch on foreign keys
    return connection

def init_db():
    #Building the tables by running schema.sql
    schema = Path(__file__).parent / "schema.sql"
    connection = get_connection()
    connection.executescript(schema.read_text())
    connection.commit()
    connection.close()
    print("Database initialised")

if __name__ == "__main__":
    init_db()