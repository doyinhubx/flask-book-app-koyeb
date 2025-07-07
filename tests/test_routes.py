from models import Book, db
from datetime import date

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Book" in response.data

def test_add_book(client):
    response = client.post('/add', data={
        'title': 'Test Book',
        'author': 'Test Author',
        'genre': 'Fiction',
        'description': 'Test Description',
        'isbn': '1234567890123',
        'published_date': '2024-01-01'
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'Test Book' in response.data


def test_edit_book(client, app):
    with app.app_context():
        book = Book(title='Old Title', author='Author', published_date=date.today())
        db.session.add(book)
        db.session.commit()
        book_id = book.id

    response = client.post(f'/edit/{book_id}', data={
        'title': 'Updated Title',
        'author': 'Author',
        'genre': '',
        'description': '',
        'isbn': '',
        'published_date': '2024-01-01'
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'Updated Title' in response.data


def test_delete_book(client, app):
    with app.app_context():
        book = Book(title='Delete Me', author='Author')
        db.session.add(book)
        db.session.commit()
        book_id = book.id

    response = client.get(f'/delete/{book_id}', follow_redirects=True)

    assert response.status_code == 200
    assert b'Delete Me' not in response.data


# Handling Edge Cases in Real-World Applications
#----------------------------------------------------
def test_add_invalid_book(client):
    response = client.post('/add', data={
        'title': '',  # Required field missing
        'author': ''
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'This field is required' in response.data or b'Add Book' in response.data


def test_add_book_missing_fields(client):
    """POST /add with missing required fields"""
    response = client.post('/add', data={
        'title': '',  # Required
        'author': ''  # Required
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'This field is required' in response.data or b'Add Book' in response.data


def test_add_book_invalid_isbn(client):
    """POST /add with invalid ISBN (too short or non-numeric)"""
    response = client.post('/add', data={
        'title': 'Invalid ISBN Book',
        'author': 'Test Author',
        'isbn': 'abc123',
        'published_date': '2024-01-01'
    }, follow_redirects=True)

    # This assumes you validate ISBN format in the form
    assert response.status_code == 200
    assert b'invalid' in response.data.lower() or b'Add Book' in response.data


def test_edit_nonexistent_book(client):
    """Try to edit a book that doesn't exist"""
    response = client.get('/edit/9999', follow_redirects=True)
    assert response.status_code == 404


def test_delete_nonexistent_book(client):
    """Try to delete a book that doesn't exist"""
    response = client.get('/delete/9999', follow_redirects=True)
    assert response.status_code == 404


def test_empty_form_submission(client):
    """Submit form with all fields empty"""
    response = client.post('/add', data={}, follow_redirects=True)
    assert response.status_code == 200
    assert b'This field is required' in response.data or b'Add Book' in response.data


def test_invalid_method_on_add(client):
    """Send GET where POST is expected"""
    response = client.put('/add')  # PUT is not allowed on this route
    assert response.status_code in [405, 400]  # Method not allowed
