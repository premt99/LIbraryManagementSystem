# routes.py
from flask import Flask, request, jsonify
from models import create_connection

app = Flask(__name__)

# CRUD operations for Books

@app.route('/books', methods=['GET'])
def get_books():
    conn = create_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM Books')
    books = c.fetchall()
    conn.close()
    return jsonify(books)

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    conn = create_connection()
    c = conn.cursor()
    c.execute("INSERT INTO Books (title, author, year, available) VALUES (?, ?, ?, ?)",
              (data['title'], data['author'], data['year'], data['available']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Book added successfully!"}), 201

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    conn = create_connection()
    c = conn.cursor()
    c.execute("UPDATE Books SET title = ?, author = ?, year = ?, available = ? WHERE id = ?",
              (data['title'], data['author'], data['year'], data['available'], id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Book updated successfully!"})

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    conn = create_connection()
    c = conn.cursor()
    c.execute("DELETE FROM Books WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Book deleted successfully!"})

# CRUD operations for Members

@app.route('/members', methods=['GET'])
def get_members():
    conn = create_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM Members')
    members = c.fetchall()
    conn.close()
    return jsonify(members)

@app.route('/members', methods=['POST'])
def add_member():
    data = request.get_json()
    conn = create_connection()
    c = conn.cursor()
    c.execute("INSERT INTO Members (name, email) VALUES (?, ?)",
              (data['name'], data['email']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Member added successfully!"}), 201

@app.route('/members/<int:id>', methods=['PUT'])
def update_member(id):
    data = request.get_json()
    conn = create_connection()
    c = conn.cursor()
    c.execute("UPDATE Members SET name = ?, email = ? WHERE id = ?",
              (data['name'], data['email'], id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Member updated successfully!"})

@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    conn = create_connection()
    c = conn.cursor()
    c.execute("DELETE FROM Members WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Member deleted successfully!"})

if __name__ == '__main__':
    app.run(debug=True)

# Search Books by title or author
@app.route('/books/search', methods=['GET'])
def search_books():
    query = request.args.get('query')
    conn = create_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM Books WHERE title LIKE ? OR author LIKE ?', ('%' + query + '%', '%' + query + '%'))
    books = c.fetchall()
    conn.close()
    return jsonify(books)

# Pagination for Books
@app.route('/books/page', methods=['GET'])
def paginate_books():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 5))
    offset = (page - 1) * per_page
    conn = create_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM Books LIMIT ? OFFSET ?', (per_page, offset))
    books = c.fetchall()
    conn.close()
    return jsonify(books)

# A simple authentication decorator for token-based protection
from functools import wraps
from flask import request, jsonify

def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('x-access-token')
        if not token or token != 'your-token-here':
            return jsonify({"message": "Token is missing or invalid!"}), 403
        return f(*args, **kwargs)
    return decorated_function

@app.route('/books', methods=['POST'])
@token_required
def add_book():
    # Function logic
    pass


