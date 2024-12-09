import sqlite3

# Initialize the database with tables for books and members
def init_db():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    # Create books table
    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        author TEXT NOT NULL)''')

    # Create members table
    cursor.execute('''CREATE TABLE IF NOT EXISTS members (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL)''')

    conn.commit()
    conn.close()

# Books functions
def get_books():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    conn.close()
    return [{"id": book[0], "title": book[1], "author": book[2]} for book in books]

def add_book(title, author):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books (title, author) VALUES (?, ?)', (title, author))
    conn.commit()
    conn.close()

def get_book(book_id):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books WHERE id = ?', (book_id,))
    book = cursor.fetchone()
    conn.close()
    if book:
        return {"id": book[0], "title": book[1], "author": book[2]}
    return None

def update_book(book_id, title, author):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE books SET title = ?, author = ? WHERE id = ?', (title, author, book_id))
    conn.commit()
    cursor.execute('SELECT * FROM books WHERE id = ?', (book_id,))
    updated_book = cursor.fetchone()
    conn.close()
    if updated_book:
        return {"id": updated_book[0], "title": updated_book[1], "author": updated_book[2]}
    return None

def delete_book(book_id):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
    conn.commit()
    conn.close()
    return True

# Members functions
def get_members():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM members')
    members = cursor.fetchall()
    conn.close()
    return [{"id": member[0], "name": member[1], "email": member[2]} for member in members]

def add_member(name, email):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO members (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    conn.close()

def get_member(member_id):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM members WHERE id = ?', (member_id,))
    member = cursor.fetchone()
    conn.close()
    if member:
        return {"id": member[0], "name": member[1], "email": member[2]}
    return None

def update_member(member_id, name, email):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE members SET name = ?, email = ? WHERE id = ?', (name, email, member_id))
    conn.commit()
    cursor.execute('SELECT * FROM members WHERE id = ?', (member_id,))
    updated_member = cursor.fetchone()
    conn.close()
    if updated_member:
        return {"id": updated_member[0], "name": updated_member[1], "email": updated_member[2]}
    return None

def delete_member(member_id):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM members WHERE id = ?', (member_id,))
    conn.commit()
    conn.close()
    return True
