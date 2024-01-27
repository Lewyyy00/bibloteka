from flask import render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.models import Book, Author
from app import app, db

@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.form.get('title')
    new_book = Book(title=title)
    db.session.add(new_book)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/add_author', methods=['POST'])
def add_author():
    author_name = request.form.get('author_name')
    book_id = request.form.get('book_id')
    
    book = Book.query.get(book_id)
    if book:
        author = Author.query.filter_by(name=author_name).first()
        if not author:
            author = Author(name=author_name)
        book.authors.append(author)
        db.session.commit()
    
    return redirect(url_for('index'))