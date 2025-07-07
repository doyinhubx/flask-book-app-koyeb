import pytest
import tempfile
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app as flask_app
from models import db


@pytest.fixture
def app():
    # Setup temporary SQLite DB for testing
    db_fd, db_path = tempfile.mkstemp()
    flask_app.config['TESTING'] = True
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
    flask_app.config['WTF_CSRF_ENABLED'] = False

    with flask_app.app_context():
        db.create_all()
        yield flask_app

    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def client(app):
    return app.test_client()



