from sqlalchemy import Column, String, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
import os

os.environ['DB_CONN'] = 'postgres://claireperacchio@localhost:5432/capstone'
database_path = os.environ['DB_CONN']

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
Classes
Have title and release year
'''
class Movie(db.Model):  
  __tablename__ = 'Movie'

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(120), nullable=False)
  release_year = db.Column(db.Integer, nullable=False)
  rating = db.Column(db.String(120), nullable=False)
  run_time = db.Column(db.Integer, nullable=False)
  box_office = db.Column(db.Integer, nullable=False)
  actors = db.relationship('Actor', backref='movie')
  director = db.relationship('Director', backref='movie')

  def __repr__(self):
    return f'<Movie {self.id} {self.title}>'

class Actor(db.Model):
  __tablename__ = 'Actor'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(120), nullable=False)
  age = db.Column(db.Integer, nullable=False)
  gender = db.Column(db.Char(1), nullable=False)
  movie_id = Column(Integer, ForeignKey('movie.id'))

  def __repr__(self):
    return f'<Actor {self.id} {self.name}>'

class Director(db.Model):
  __tablename__ = 'Director'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(120), nullable=False)
  age = db.Column(db.Integer, nullable=False)
  gender = db.Column(db.Char(1), nullable=False)
  movie_id = Column(Integer, ForeignKey('movie.id'))

  def __repr__(self):
    return f'<Director {self.id} {self.name}>'
