from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField
from wtforms.validators import DataRequired, AnyOf, URL

class MovieForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    release_year = StringField(
        'release_year', validators=[DataRequired()]
    )
    rating = SelectField(
        'rating', validators=[DataRequired()],
        choices=[
            ('G', 'G'),
            ('PG', 'PG'),
            ('PG-13', 'PG-13'),
            ('R', 'R')
        ]
    )
    box_office = StringField(
        'box_office', validators=[DataRequired()]
    )
    image_link = StringField(
        'image_link'
    )
    director = StringField(
        'director'
    )

class ActorForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    age = StringField(
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