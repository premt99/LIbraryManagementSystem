# models.py
import sqlite3

def create_connection():
    """Create a connection to the SQLite database."""
    conn = sqlite3.connect('database.db')
    return conn

def create_tables():
    """Create the tables in the database."""
    conn = create_connection()
    c = conn.cursor()
    
    # Create the Books table
    c.execute('''CREATE TABLE IF NOT EXISTS Books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    year INTEGER,
                    available INTEGER)''')

    # Create the Members table
    c.execute('''CREATE TABLE IF NOT EXISTS Members (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL)''')

    conn.commit()
    conn.close()

create_tables()
