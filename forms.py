from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SubmitField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    genre = StringField('Genre')
    description = TextAreaField('Description')
    isbn = StringField('ISBN')
    published_date = DateField('Published Date', format='%Y-%m-%d')
    submit = SubmitField('Submit')
