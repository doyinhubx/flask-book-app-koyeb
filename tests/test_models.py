# from models import Book

# def test_create_book(app):
#     with app.app_context():
#         book = Book(title="Test Book", author="Author")
#         assert book.title == "Test Book"
#         assert book.author == "Author"


from models import Book, db
from datetime import date
import pytest

def test_create_book(app):
    with app.app_context():
        # Clean up existing data
        Book.query.delete()
        db.session.commit()

        # Add a new test book
        book = Book(
            title="Test Book",
            author="Author",
            genre="Fiction",
            description="Test Description",
            isbn="1234567890123",
            published_date=date(2024, 1, 1)
        )
        db.session.add(book)
        db.session.commit()

        saved_book = Book.query.first()
        assert saved_book is not None
        assert saved_book.title == "Test Book"


def test_missing_required_fields(app):
    with app.app_context():
        # Title is required
        book = Book(author="Author Only")

        db.session.add(book)
        with pytest.raises(Exception):  # SQLAlchemy should raise IntegrityError
            db.session.commit()




