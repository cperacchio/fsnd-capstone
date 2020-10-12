import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movie, Actor

class MovieCastingTestCase(unittest.TestCase):
	"""This class represents the trivia test case"""

	def setUp(self):
		"""Define test variables and initialize app."""
		self.app = create_app()
		self.client = self.app.test_client
		self.database_name = "capstone"
		self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
		setup_db(self.app, self.database_path)

		# binds the app to the current context
		with self.app.app_context():
			self.db = SQLAlchemy()
			self.db.init_app(self.app)
			# create all tables
			self.db.create_all()

		self.test_movie = {
			'name': 'The Pink Panther 2'
			'director': 'Bradley Cooper'
			'genre': 'Comedy'
			'release_year': '2022'
			'rating': 'PG-13'
		}
		
		self.test_actor = {
			'name': 'Steve Martin'
			'age': '75'
			'gender': 'Male'
			'image_link': 'https://en.wikipedia.org/wiki/File:Steve_Martin,_2017-08-11.jpg'
		}
	
	def tearDown(self):
		"""Executed after reach test"""
		pass

	"""
	TESTS
	Includes at least one test for each test for successful operation and for expected errors.
	"""
	
	# tests for get requests
	def test_get_movies():
		res = self.client().get('/movies')
		data = json.loads(res.data)

		self.assertEqual(res.status_code, 200)

	def test_get_movies():
		res = self.client().get('/movies')
		data = json.loads(res.data)

		self.assertEqual(res.status_code, 401)

	def test_get_actors():
		res = self.client().get('/actors')
		data = json.loads(res.data)

		self.assertEqual(res.status_code, 200)

	def test_get_actors():
		res = self.client().get('/actors')
		data = json.loads(res.data)

		self.assertEqual(res.status_code, 401)

	# tests for post requests
	def test_create_movie():
		res = self.client().post('/movies/create')
		data = json.loads(res.data)

		self.assertEqual(res.status_code, 200)

	def test_create_movie():
		res = self.client().post('/movies/create')
		data = json.loads(res.data)

		self.assertEqual(res.status_code, 401)

	def test_create_actor():
		res = self.client().post('/actors/create')
		data = json.loads(res.data)

		self.assertEqual(res.status_code, 200)

	def test_create_actor():
		res = self.client().post('/actors/create')
		data = json.loads(res.data)

		self.assertEqual(res.status_code, 401)

	# tests for patch requests
	def test_update_movie():
		res = self.client().patch('/movies/<id>')
		data = json.loads(res.data)

		self.assertEqual(res.status_code, 200)

	def test_update_movie():
		res = self.client().patch('/movies/<id>')
		data = json.loads(res.data)

		self.assertEqual(res.status_code, 401)

	def test_update_actor():
		res = self.client().patch('/actors/<id>')
		data = json.loads(res.data)

		self.assertEqual(res.status_code, 200)
	
	def test_update_actor():
		res = self.client().patch('/actors/<id>')
		data = json.loads(res.data)

		self.assertEqual(res.status_code, 401)

	# tests for delete requests
	def test_delete_movie():
		res = self.client().delete('/movies/<id>')
		data = json.loads(res.data)

		self.assertEqual(res.status_code, 200)

	def test_delete_movie():
		res = self.client().delete('/movies/<id>')
		data = json.loads(res.data)

		self.assertEqual(res.status_code, 401)

	def test_delete_actor():
		res = self.client().delete('/actors/<id>')
		data = json.loads(res.data)

		self.assertEqual(res.status_code, 200)
	
	def test_delete_actor():
		res = self.client().delete('/actors/<id>')
		data = json.loads(res.data)

		self.assertEqual(res.status_code, 401)

# Make the tests conveniently executable
if __name__ == "__main__":
	unittest.main()
