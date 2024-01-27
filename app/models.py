from app import db

authors_books = db.Table('authors_books',
                db.Column('author_id', db.Integer, db.ForeignKey('author.id')),
                db.Column('book_id', db.Integer, db.ForeignKey('book.id'))
                        )

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Boolean, default=True)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    books = db.relationship('Book', secondary=authors_books, backref=db.backref('authors', lazy='dynamic'))


