#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
import os
from flask import Flask, request, abort, jsonify, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from models import setup_db, Movie, Actor
import simplejson as json
#from auth.auth import AuthError, requires_auth
from forms import MovieForm, ActorForm

SECRET_KEY = os.urandom(32)

#----------------------------------------------------------------------------#
# Initialize App 
#----------------------------------------------------------------------------#
def create_app(test_config=None):
	# create and configure the app
  	app = Flask(__name__)
  	app.config['SECRET_KEY'] = SECRET_KEY
  	setup_db(app)
  	CORS(app)

  	return app

app = create_app()

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

# route handler for home page
@app.route('/')
def index():
	return render_template('pages/home.html')

#  Movies
#  ----------------------------------------------------------------
# route handler to get list of movies
@app.route('/movies', methods = ['GET'])
def get_movies():
	movies = Movie.query.all()

	movies_data = []
	for movie in movies:
		movies_data.append({
			"id": movie.id,
			"name": movie.name,
			"director": movie.director,
			"genre": movie.genre,
			"release_year": movie.release_year,
			"rating": movie.rating
			})

	return render_template('pages/movies.html', movies=movies_data), 200

# route handler to get to form to create a new movie
@app.route('/movies/create', methods=['GET'])
def create_movie_form():
	form = MovieForm()
	
	return render_template('forms/new_movie.html', form=form)

# route handler to create a movie record in db
@app.route('/movies/create', methods=['POST'])
def create_movie():
	# catch errors with try/except
	error = False
	# add user-submitted data and commit to db
	movie = Movie(
		name = request.form.get('name'),
		director = request.form.get('director'),
		genre = request.form.get('genre'),
		release_year = request.form.get('release_year'),
		rating = request.form.get('rating')
	)
	try:
		#db.session.add(movie)
		movie.insert()
		#db.session.commit()

	except:
		error = True
		#db.session.rollback()
		#print(sys.exc_info())
	
	# finally:
	# 	db.session.close()
	  
	if error:
		#On unsuccessful db insert, flash an error
		flash('Error: Movie ' + request.form['name'] + ' was not listed. Please check your inputs and try again :)')
	else:
		# On successful db insert, flash success
		flash(request.form['name'] + ' was successfully listed!')

	return render_template('pages/home.html')

# route handler to get individual movie records
@app.route('/movies/<int:movie_id>', methods=['GET'])
def get_movie_details():
	movie = Movie.query.get(movie_id)

	if movie is None:
		return json.dumps({
			'success': False,
			'error': 'Movie could not be found'
		}), 404

	cast = movie.cast
	cast_details = []

	for actor in cast:
		cast_details.append({
			"id": actor.id,
			"name": actor.name,
			"age": actor.age,
			"gender": actor.gender,
			"image_link": actor.image_link
			})

	movie_details = {
		"id": movie.id,
		"name": movie.name,
		"director": movie.director,
		"genre": movie.genre,
		"release_year": movie.release_year,
		"rating": movie.rating,
		"cast": cast_details	
	}

	return render_template('pages/show_movie.html', movie=movie_details)

# route handler to update movie records
@app.route('/movies/<int:movie_id>', methods=['PATCH'])
def update_movie(*args, **kwargs):
	# get movie based on id
	id = kwargs['id']
	movie = Movie.query.filter_by(id=id).one_or_none()

	if movie is None:
		return json.dumps({
			'success': False,
			'error': 'Movie could not be found to be updated',
		}), 404

	body = request.get_json()

	#if there is a movie name
	if 'name' in body:
		movie.name = body['name']

	# update movie
	try:
		movie.insert()

		return json.dumps({
			'success': True,
			'movie': movie.id
		}), 200
	# return error if movie can't be updated
	except:
		return json.dumps({
			'success': False,
			'error': 'An error occurred'
		}), 400


# route handler to delete movies
@app.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
	try:
		# get movie to delete
		movie = Movie.query.get(movie_id) 
		db.session.delete(movie)
		db.session.commit()

		# on successful db delete, flash success
		flash('Movie ' + request.form['title'] + ' was successfully deleted!')

	except:
		db.session.rollback()
		flash('An error occurred. This movie ' + request.form['title'] + ' could not be deleted.')
	finally:
		db.session.close()

	return render_template('pages/home.html')

#  Actors
#  ----------------------------------------------------------------
# route handler to get list of actors
@app.route('/actors', methods = ['GET'])
def get_actors():
	actors = Actor.query.all()

	actors_data = []
	for actor in actors:
		actors_data.append({
			"id": actor.id,
			"name": actor.name,
			"age": actor.age,
			"gender": actor.gender,
			"image_link": actor.image_link
			})

	return render_template('pages/actors.html', actors=actors_data)

# route handler to get to form to create a new actor
@app.route('/actors/create', methods=['GET'])
def create_actor_form():
	form = ActorForm()
	return render_template('forms/new_actor.html', form=form)

# route handler to create an actor profile in db
@app.route('/actors/create', methods=['POST'])
def create_actor():
	# catch errors with try/except
	error = False
	# add user-submitted data and commit to db
	actor = Actor(
		name = request.form.get('name'),
		age = request.form.get('age'),
		gender = request.form.get('gender'),
		image_link = request.form.get('image_link')
	)
	try:
		actor.insert()
		# db.session.add(self)
		# db.session.commit()

	except Exception as e:
		error = True
		# db.session.rollback()
		# print(f'Error ==> {e}')

	# finally:
	# 	db.session.close()

	if error:
		# On unsuccessful db insert, flash an error
		flash('Error: Actor ' + request.form['name'] + ' was not listed. Please check your inputs and try again :)')

	else:
		# on successful db insert, flash success
		flash(request.form['name'] + ' was successfully listed!')

	return render_template('pages/home.html')

# route handler to update actor records
@app.route('/actors/<int:actor_id>', methods=['PATCH'])
def update_actor(*args, **kwargs):
	# get movie based on id
	id = kwargs['id']
	movie = Actor.query.filter_by(id=id).one_or_none()

	if movie is None:
		return json.dumps({
			'success': False,
			'error': 'Actor could not be found to be updated',
		}), 404

	body = request.get_json()

	#if there is an actor name
	if 'name' in body:
		actor.name = body['name']

	# update actor 
	try:
		actor.insert()

		return json.dumps({
			'success': True,
			'actor': actor.id
		}), 200
	# return error if actor can't be updated
	except:
		return json.dumps({
			'success': False,
			'error': 'An error occurred'
		}), 400

# route handler to delete actors
@app.route('/actors/<int:actor_id>', methods=['DELETE'])
def delete_actor(actor_id):
	try:
		# get movie to delete
		actor = Actor.query.get(actor_id) 
		db.session.delete(actor)
		db.session.commit()

		# on successful db delete, flash success
		flash('Actor ' + request.form['name'] + ' was successfully deleted!')

	except:
		db.session.rollback()
		flash('An error occurred. Actor ' + request.form['name'] + ' could not be deleted.')

	finally:
		db.session.close()

	return render_template('pages/home.html')

#  Cast a Movie
#  ----------------------------------------------------------------
# route handler to get to form to cast a movie
@app.route('/cast/create', methods=['GET'])
def create_cast_form():				
	movies = Movie.query.all()
	actors = Actor.query.all()		

	return render_template('forms/new_cast.html', movies=movies, actors=actors)

# route handler to cast a movie in db
@app.route('/cast/create', methods=['POST'])
def create_cast():
	error = False
	actor_id = request.form.get('actor_id')
	movie_id = request.form.get('movie_id')

	try:
		movie = Movie.query.get(movie_id)
		actor = Movie.query.get(actor_id)

		if movie is None or actor is None:
			return json.dumps({
				'success': False,
			}), 400

		movie.cast.append(actor)
		movie.update()

	except:
		error = True
	
	if error:
		flash('Error: This actor was not cast. Please check your inputs and try again :)')

	else: 
		# success message upon succeesful casting
		flash('This actor was successfully cast!')

	return render_template('pages/home.html')

#----------------------------------------------------------------------------#
# Launch App
#----------------------------------------------------------------------------#
if __name__ == '__main__':
	app.run(debug=True)
