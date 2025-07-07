from flask import Flask, render_template, redirect, url_for, request, abort
from models import db, Book
from forms import BookForm
from config import Config
from flask_migrate import Migrate  

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)  

@app.route('/')
def index():
    books = Book.query.order_by(Book.created_at.desc()).all()
    return render_template('index.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    form = BookForm()
    if form.validate_on_submit():
        book = Book(
            title=form.title.data,
            author=form.author.data,
            genre=form.genre.data,
            description=form.description.data,
            isbn=form.isbn.data,
            published_date=form.published_date.data
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_book.html', form=form)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_book(id):
    book = db.session.get(Book, id)
    if not book:
        abort(404)
    form = BookForm(obj=book)
    if form.validate_on_submit():
        form.populate_obj(book)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_book.html', form=form)

@app.route('/delete/<int:id>')
def delete_book(id):
    book = db.session.get(Book, id)
    if not book:
        abort(404)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
