import os
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, create_engine
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, sessionmaker
import json, sys

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
Models
'''

actor_movie = db.Table('actor_movie',
    Column('id', db.Integer, primary_key=True),
    Column('movie_id', db.Integer, db.ForeignKey('movie.id')),
    Column('actor_id', db.Integer, db.ForeignKey('actor.id'))
)

director_movie = db.Table('director_movie',
    Column('id', db.Integer, primary_key=True),
    Column('movie_id', db.Integer, db.ForeignKey('movie.id')),
    Column('director_id', db.Integer, db.ForeignKey('director.id'))
)

class Movie(db.Model):  
  __tablename__ = 'Movie'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(120), nullable=False)
  release_year = db.Column(db.Integer, nullable=False)
  rating = db.Column(db.String(120), nullable=False)
  box_office = db.Column(db.Integer, nullable=False)
  image_link = db.Column(db.String(500))
  cast = db.relationship('Actor', secondary=actor_movie, back_populates='movies', cascade='save-update, merge', lazy='dynamic')
  director = db.relationship('Director', secondary=director_movie, back_populates='movies', cascade='save-update, merge', lazy='dynamic')

  def __init__(self, name, release_year, rating, box_office, image_link, director):
        self.name = name
        self.release_year = release_year
        self.rating = rating
        self.box_office = box_office
        self.image_link = image_link
        self.director = director

  def insert(self):
    try:
      db.session.add(self)
      db.session.commit()
    except: 
      db.session.rollback()
    print(sys.exc_info())
  
  def update(self):
    try:
      db.session.commit()
    except: 
      db.session.rollback()
      print(sys.exc_info())

  def delete(self):
    try:
      db.session.delete(self)
      db.session.commit()
    except: 
      db.session.rollback()
      print(sys.exc_info())


  def format(self):
      return {
          'name': self.name,
          'id': self.id,
          'release_year': self.release_year,
          'cast': [actor.format_no_movies() for actor in self.cast],
          'director': self.director
      }

  def format_with_no_cast(self):
      return {
          'name': self.name,
          'release_year': self.release_year,
          'director': self.director
      }

class Actor(db.Model):
  __tablename__ = 'Actor'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(120), nullable=False)
  age = db.Column(db.Integer, nullable=False)
  gender = db.Column(db.String(1), nullable=False)
  image_link = db.Column(db.String(500))
  movies = db.relationship('Movie', secondary=actor_movie, lazy='joined')

  def __init__(self, name, age, gender, image_link):
        self.name = name
        self.age = age
        self.gender = gender
        self.image_link = image_link
        
  def insert(self):
    try:
      db.session.add(self)
      db.session.commit()
    except: 
      db.session.rollback()
      print(sys.exc_info())
  
  def update(self):
    try:
      db.session.commit()
    except: 
      db.session.rollback()
      print(sys.exc_info())

  def delete(self):
    try:
      db.session.delete(self)
      db.session.commit()
    except: 
      db.session.rollback()
      print(sys.exc_info())

  def format(self):
      return {
          'name': self.name,
          'id': self.id,
          'age': self.age,
          'gender': self.gender,
          'movies': [movie.format_with_no_cast() for movie in self.movies]
      }

  def format_no_movies(self):
      return {
          'name': self.name,
          'age': self.age,
          'gender': self.gender,
      }

class Director(db.Model):
  __tablename__ = 'Director'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(120), nullable=False)
  age = db.Column(db.Integer, nullable=False)
  gender = db.Column(db.String(1), nullable=False)
  image_link = db.Column(db.String(500))
  movies = db.relationship('Movie', secondary=director_movie, lazy='joined')

  def __init__(self, name, age, gender, image_link):
        self.name = name
        self.age = age
        self.gender = gender
        self.image_link = image_link
        
  def insert(self):
    try:
      db.session.add(self)
      db.session.commit()
    except: 
      db.session.rollback()
      print(sys.exc_info())
  
  def update(self):
    try:
      db.session.commit()
    except: 
      db.session.rollback()
      print(sys.exc_info())

  def delete(self):
    try:
      db.session.delete(self)
      db.session.commit()
    except: 
      db.session.rollback()
      print(sys.exc_info())

  def format(self):
      return {
          'name': self.name,
          'id': self.id,
          'age': self.age,
          'gender': self.gender,
          'movies': [movie.format_with_no_cast() for movie in self.movies]
      }

  def format_no_movies(self):
      return {
          'name': self.name,
          'age': self.age,
          'gender': self.gender,
      }
