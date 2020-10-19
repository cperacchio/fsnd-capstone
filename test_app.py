import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Movie, Actor

class CapstoneTestCase(unittest.TestCase):
	"""This class represents the test case"""

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
			'name': 'The Pink Panther 3'
			'director': 'Bradley Cooper'
			'genre': 'Comedy'
			'release_year': '2023'
			'rating': 'PG-13'
		}
		
		self.test_actor = {
			'name': 'Steve Martin'
			'age': '75'
			'gender': 'Male'
			'image_link': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Steve_Martin%2C_2017-08-11.jpg/220px-Steve_Martin%2C_2017-08-11.jpg'
		}
	
	def tearDown(self):
		"""Executed after reach test"""
		pass

	"""
	TESTS
	Includes at least one test for each test for successful operation and for expected errors.
	"""
	
	"""
	Tests for movies endpoints
	"""

	def test_get_movies():
		res = self.client().get('/movies')
		data = json.loads(res.data)
		self.assertEqual(res.status_code, 200)
		self.assertEqual(data['success'], True)

	def test_get_movies():
		res = self.client().get('/movies')
		data = json.loads(res.data)
		self.assertEqual(res.status_code, 404)
		self.assertEqual(data['success'], False)
		self.assertEqual(data['message'], 'Not found')

	def test_create_movie_form():
		res = self.client().get('/movies/create')
		data = json.loads(res.data)
		self.assertEqual(res.status_code, 200)
		self.assertEqual(data['success'], True)

	def test_create_movie_form():
		res = self.client().get('/movies/create')
		data = json.loads(res.data)
		self.assertEqual(res.status_code, 404)
		self.assertEqual(data['success'], False)
		self.assertEqual(data['message'], 'Not found')

	def test_create_movie(self):
		new_movie = {
			'name': 'The Pink Panther 3',
			'director': 'Bradley Cooper',
			'genre': 'Comedy',
			'release_year': '2023',
			'rating': 'PG-13'
		}
		res = self.client().post('/movies/create', json=new_movie)
		data = json.loads(res.data)
		self.assertEqual(res.status_code, 200)
		self.assertEqual(data['success'], True)

	def test_create_movie(self):
		new_movie = {
			'name': 'The Pink Panther 3',
			'director': 'Bradley Cooper',
			'genre': 'Comedy',
			'release_year': '2023',
			'rating': 'PG-13'
		}
		res = self.client().post('/movies/create', json=new_movie)
		data = json.loads(res.data)
		self.assertEqual(res.status_code, 405)
		self.assertEqual(data['success'], False)
		self.assertEqual(data['message'], 'Method not allowed')

	def test_get_movie_details():
		res = self.client().get('/movies/{id}')
		data = json.loads(res.data)
		self.assertEqual(res.status_code, 200)
		self.assertEqual(data['success'], True)

	def test_get_movie_details():
		res = self.client().get('/movies/{id}')
		data = json.loads(res.data)
		self.assertEqual(res.status_code, 404)
		self.assertEqual(data['success'], False)
		self.assertEqual(data['message'], 'Not found')

	def test_update_movie_form():
		res = self.client().get('/movies/{id}/patch')
		data = json.loads(res.data)
		self.assertEqual(res.status_code, 200)
		self.assertEqual(data['success'], True)

	def test_update_movie_form():
		res = self.client().get('/movies/{id}/patch')
		data = json.loads(res.data)
		self.assertEqual(res.status_code, 404)
		self.assertEqual(data['success'], False)
		self.assertEqual(data['message'], 'Not found')

	def test_update_movie(self):
		updated_movie = {
			'name': 'The Pink Panther 4',
			'director': 'Bradley Cooper',
			'genre': 'Comedy',
			'release_year': '2023',
			'rating': 'PG-13'
		}
		res = self.client().post('/movies/{id}/patch', json=updated_movie)
		data = json.loads(res.data)
		self.assertEqual(res.status_code, 200)
		self.assertEqual(data['success'], True)

	def test_update_movie(self):
		updated_movie = {
			'name': 'The Pink Panther 4',
			'director': 'Bradley Cooper',
			'genre': 'Comedy',
			'release_year': '2023',
			'rating': 'PG-13'
		}
		res = self.client().post('/movies/{id}/patch', json=updated_movie)
		data = json.loads(res.data)
		self.assertEqual(res.status_code, 405)
		self.assertEqual(data['success'], False)
		self.assertEqual(data['message'], 'Method not allowed')

	def test_delete_movie(self):
		id = Movie.query.order_by(Movie.id.desc()).first().id
		res = self.client().delete(f'/movies/{id}/delete')
		data = json.loads(res.data)
		movie = Movie.query.filter(Movie.id==id).one_or_none()
		self.assertEqual(res.status_code, 200)
		self.assertEqual(data['success'], True)

	def test_delete_movie(self):
		id = Movie.query.order_by(Movie.id.desc()).first().id
		res = self.client().delete(f'/movies/{id}/delete')
		data = json.loads(res.data)
		movie = Movie.query.filter(Movie.id==id).one_or_none()
		self.assertEqual(res.status_code, 405)
		self.assertEqual(data['success'], False)
		self.assertEqual(data['message'], 'Method not allowed')

	"""
	Tests for actors endpoints
	"""
	def test_get_actors():
		res = self.client().get('/actors')
		data = json.loads(res.data)
		self.assertEqual(res.status_code, 200)
		self.assertEqual(data['success'], True)

	def test_get_actors():
		res = self.client().get('/actors')
		data = json.loads(res.data)
		self.assertEqual(res.status_code, 404)
		self.assertEqual(data['success'], False)
		self.assertEqual(data['message'], 'Not found')

	def test_create_actor_form():
		res = self.client().get('/actors/create')
		data = json.loads(res.data)
		self.assertEqual(res.status_code, 200)
		self.assertEqual(data['success'], True)

	def test_create_actor_form():
		res = self.client().get('/actors/create')
		data = json.loads(res.data)
		self.assertEqual(res.status_code, 404)
		self.assertEqual(data['success'], False)
		self.assertEqual(data['message'], 'Not found')

	def test_create_actor(self):
		new_actor = {
			'name': 'Steve Martin'
			'age': '75'
			'gender': 'Male'
			'image_link': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Steve_Martin%2C_2017-08-11.jpg/220px-Steve_Martin%2C_2017-08-11.jpg'
		}
		res = self.client().post('/actors/create', json=new_actor)
		data = json.loads(res.data)
		self.assertEqual(res.status_code, 200)
		self.assertEqual(data['success'], True)

	def test_create_actor(self):
		new_actor = {
			'name': 'Steve Martin'
			'age': '75'
			'gender': 'Male'
			'image_link': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Steve_Martin%2C_2017-08-11.jpg/220px-Steve_Martin%2C_2017-08-11.jpg'
		}
		res = self.client().post('/actors/create', json=new_actor)
		data = json.loads(res.data)
		self.assertEqual(res.status_code, 405)
		self.assertEqual(data['success'], False)
		self.assertEqual(data['message'], 'Method not allowed')

	def test_get_actor_details():
		res = self.client().get('/actors/{id}')
		data = json.loads(res.data)
		self.assertEqual(res.status_code, 200)
		self.assertEqual(data['success'], True)

	def test_get_actor_details():
		res = self.client().get('/actors/{id}')
		data = json.loads(res.data)
		self.assertEqual(res.status_code, 404)
		self.assertEqual(data['success'], False)
		self.assertEqual(data['message'], 'Not found')

	def test_update_actor_form():
		res = self.client().get('/actors/{id}/patch')
		data = json.loads(res.data)
		self.assertEqual(res.status_code, 200)
		self.assertEqual(data['success'], True)

	def test_update_actor_form():
		res = self.client().get('/actors/{id}/patch')
		data = json.loads(res.data)
		self.assertEqual(res.status_code, 404)
		self.assertEqual(data['success'], False)
		self.assertEqual(data['message'], 'Not found')

	def test_update_actor(self):
		updated_actor = {
			'name': 'Steve Martin'
			'age': '75'
			'gender': 'Male'
			'image_link': 'https://images.unsplash.com/photo-1596618813198-c1f7ae5827c8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1189&q=80'
		}
		res = self.client().post('/actors/{id}/patch', json=updated_actor)
		data = json.loads(res.data)
		self.assertEqual(res.status_code, 200)
		self.assertEqual(data['success'], True)

	def test_update_actor(self):
		updated_actor = {
			'name': 'Steve Martin'
			'age': '75'
			'gender': 'Male'
			'image_link': 'https://images.unsplash.com/photo-1596618813198-c1f7ae5827c8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1189&q=80'
		}
		res = self.client().post('/actors/{id}/patch', json=updated_actor)
		data = json.loads(res.data)
		self.assertEqual(res.status_code, 405)
		self.assertEqual(data['success'], False)
		self.assertEqual(data['message'], 'Method not allowed')

	def test_delete_actor(self):
		id = Actor.query.order_by(Actor.id.desc()).first().id
		res = self.client().delete(f'/actors/{id}/delete')
		data = json.loads(res.data)
		actor = Actor.query.filter(Actor.id==id).one_or_none()
		self.assertEqual(res.status_code, 200)
		self.assertEqual(data['success'], True)

	def test_delete_actor(self):
		id = Actor.query.order_by(Actor.id.desc()).first().id
		res = self.client().delete(f'/actors/{id}/delete')
		data = json.loads(res.data)
		actor = Actor.query.filter(Actor.id==id).one_or_none()
		self.assertEqual(res.status_code, 405)
		self.assertEqual(data['success'], False)
		self.assertEqual(data['message'], 'Method not allowed')

	"""
	Tests for cast endpoints
	"""
	def test_create_cast_form():
		res = self.client().get('/cast/create')
		data = json.loads(res.data)
		self.assertEqual(res.status_code, 200)
		self.assertEqual(data['success'], True)

	def test_create_cast_form():
		res = self.client().get('/cast/create')
		data = json.loads(res.data)
		self.assertEqual(res.status_code, 404)
		self.assertEqual(data['success'], False)
		self.assertEqual(data['message'], 'Not found')

	def test_create_cast():
		res = self.client().post('/cast/create')
		data = json.loads(res.data)
		self.assertEqual(res.status_code, 200)
		self.assertEqual(data['success'], True)

	def test_create_cast(self):
		res = self.client().post('/cast/create')
		data = json.loads(res.data)
		self.assertEqual(res.status_code, 405)
		self.assertEqual(data['success'], False)
		self.assertEqual(data['message'], 'Method not allowed')

# Make the tests conveniently executable
if __name__ == "__main__":
	unittest.main()
