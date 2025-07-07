from forms import BookForm
from werkzeug.datastructures import MultiDict

def test_valid_form(app):
    with app.app_context():
        form = BookForm(formdata=MultiDict({
            "title": "Test Book",
            "author": "Author Name",
            "genre": "Fiction",
            "description": "A test book.",
            "isbn": "1234567890123",
            "published_date": "2024-01-01"
        }))
        assert form.validate() is True

def test_missing_required_fields(app):
    with app.app_context():
        form = BookForm(formdata=MultiDict({
            "title": "",
            "author": "",
            "genre": "Fiction",
            "description": "Test",
            "isbn": "1234567890123",
            "published_date": "2024-01-01"
        }))
        assert form.validate() is False
        assert "This field is required." in form.title.errors
        assert "This field is required." in form.author.errors

def test_invalid_date_format(app):
    with app.app_context():
        form = BookForm(formdata=MultiDict({
            "title": "Test Book",
            "author": "Author",
            "published_date": "01-01-2024"  # Wrong format (should be YYYY-MM-DD)
        }))
        assert form.validate() is False
        assert "Not a valid date value" in form.published_date.errors[0]


