import os
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import relationship, sessionmaker
import json, sys

#os.environ['DB_CONN'] = 'postgres://claireperacchio@localhost:5432/capstone'
database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

'''
setup_db(app)
	binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
	app.config["SQLALCHEMY_DATABASE_URI"] = database_path
	app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
	db.app = app
	try:
		db.init_app(app)

		db.create_all()
		
	except:
		print("error setting up db")

'''
Models
'''

actor_movie = db.Table('actor_movie',
	Column('id', db.Integer, primary_key=True),
	Column('movie_id', db.Integer, db.ForeignKey('Movie.id')),
	Column('actor_id', db.Integer, db.ForeignKey('Actor.id'))
)

class Movie(db.Model):  
	__tablename__ = 'Movie'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(120), nullable=False)
	director = db.Column(db.String(120))
	genre = db.Column(db.String(120), nullable=False)
	release_year = db.Column(db.Integer)
	rating = db.Column(db.String(120))
	cast = relationship('Actor', secondary=actor_movie)

	def __init__(self, name, director, genre, release_year, rating):
		self.name = name
		self.director = director
		self.genre = genre
		self.release_year = release_year
		self.rating = rating

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
	  		'id': self.id,
		  	'name': self.name,
		  	'director': self.director,
		  	'genre': self.genre,
		  	'release_year': self.release_year,
		  	'rating': self.rating,
		  	'cast': [actor.format() for actor in self.cast]
	  	}

	def format_no_cast(self):
		return {
	  		'id': self.id,
		  	'name': self.name,
		  	'director': self.director,
			'genre': self.genre,
		  	'release_year': self.release_year,
		  	'rating': self.rating
	  	}

class Actor(db.Model):
	__tablename__ = 'Actor'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(120), nullable=False)
	age = db.Column(db.Integer(), nullable=False)
	gender = db.Column(db.String(120), nullable=False)
	image_link = db.Column(db.String(500))
	movies = db.relationship('Movie', secondary=actor_movie)

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
			'movies': [movie.format() for movie in self.movies]
		}

	def format_no_movies(self):
	  	return {
		  	'name': self.name,
		  	'id': self.id,
		  	'age': self.age,
		  	'gender': self.gender
	  	}
