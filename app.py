from flask import Flask, request, jsonify

app = Flask(__name__)

# List to hold books data (since you are not using a database)
books = []

# Home route to check if the API is running
@app.route('/')
def home():
    return 'Library Management System API is running!'

# Route to handle POST requests to add a new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()  # Get the JSON data from the POST request
    if 'title' not in data or 'author' not in data:
        return jsonify({'error': 'Missing title or author'}), 400

    # Create a new book with an auto-incremented ID
    new_book = {
        'id': len(books) + 1,  # Auto-incrementing the ID
        'title': data['title'],
        'author': data['author']
    }

    # Add the new book to the list
    books.append(new_book)

    # Return the added book with HTTP status 201 (Created)
    return jsonify(new_book), 201

# Route to get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Route to get a book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book is None:
        return jsonify({'error': 'Book not found'}), 404
    return jsonify(book)

# Route to delete a book by ID
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify({'message': 'Book deleted'}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
