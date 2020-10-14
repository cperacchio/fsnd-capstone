from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, IntegerField
from wtforms.validators import DataRequired, AnyOf, URL

class MovieForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    director = StringField(
        'director'
    )
    genre = SelectField(
        'genre', validators=[DataRequired()],
        choices=[
            ('Action', 'Action'),
            ('Animated', 'Animated'),
            ('Comedy', 'Comedy'),
            ('Drama', 'Drama'),
            ('Fantasy', 'Fantasy'),
            ('Horror', 'Horror'),
            ('Indie', 'Indie'),
            ('Musical', 'Musical'),
            ('Romance', 'Romance'),
            ('Sci-Fi', 'Sci-Fi'),
            ('Thriller', 'Thriller')
        ]
    )
    release_year = StringField(
        'release_year'
    )
    rating = SelectField(
        'rating',
        choices=[
            ('G', 'G'),
            ('PG', 'PG'),
            ('PG-13', 'PG-13'),
            ('R', 'R')
        ]
    )

class ActorForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    age = IntegerField(
        'age', validators=[DataRequired()]
    )
    gender = SelectField(
        'gender', validators=[DataRequired()],
        choices=[
            ('Female', 'Female'),
            ('Male', 'Male'),
            ('Other', 'Other')
        ]
    )
    image_link = StringField(
        'image_link'
    )