#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
import os
from flask import Flask, request, abort, jsonify, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from models import setup_db, Movie, Actor
import simplejson as json
from auth.auth import requires_auth, AuthError 
from forms import MovieForm, ActorForm
from authlib.integrations.flask_client import OAuth

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

@app.after_request
def after_request(response):
	response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
	response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
	return response


# route handler to log in
oauth = OAuth(app)
auth0 = oauth.register(
    'auth0',
    client_id='2FaJjQSAtsiLqHMEfNlS0ThYQ6Oyuh9c',
    client_secret='zyo8mHSRsJPhveP8t0k3ZhdapaQs5Dcl-uZBoy6fJGjnTK8jM5lq5ySIDbSC7wVo',
    api_base_url='https://fsnd79.auth0.com',
    access_token_url='https://fsnd79.auth0.com' + '/oauth/token',
    authorize_url='https://fsnd79.auth0.com' + '/authorize',
    client_kwargs={
        'scope': 'openid profile email',
    },
)

@app.route('/authorize')
@cross_origin()
def login():
    return auth0.authorize_redirect(redirect_uri='http://localhost:5000/post-authorize', audience=casting)

# route handler for home page once logged in
@app.route('/post-authorize')
@cross_origin()
def post_auth():
	response = make_response(render_template('pages/home.html'))
	return response

#  Movies
#  ----------------------------------------------------------------
# route handler to get list of movies
@app.route('/movies', methods = ['GET'])
@cross_origin()
@requires_auth('get:movies')
def get_movies(jwt):
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
@requires_auth('get:movieform')
def create_movie_form(jwt):
	form = MovieForm()
	
	return render_template('forms/new_movie.html', form=form)

# route handler to create a movie record in db
@app.route('/movies/create', methods=['POST'])
@requires_auth('post:movies')
def create_movie(jwt):
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
		movie.insert()

	except:
		error = True
	  
	if error:
		#On unsuccessful db insert, flash an error
		flash('Error: Movie ' + request.form['name'] + ' was not listed. Please check your inputs and try again :)')
	else:
		# On successful db insert, flash success
		flash(request.form['name'] + ' was successfully listed!')

	return render_template('pages/home.html')

# route handler to get individual movie records
@app.route('/movies/<int:movie_id>', methods=['GET'])
@requires_auth('get:movies')
def get_movie_details(movie_id, jwt):
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

# route handler to get to form to update a movie record
@app.route('/movies/<int:movie_id>/patch', methods=['GET'])
@requires_auth('get:movieform')
def update_movie_form(movie_id, jwt):
	form = MovieForm()
	movie = Movie.query.get(movie_id)

	if movie is None:
		return json.dumps({
			'success': False,
			'error': 'Movie could not be found to be updated',
		}), 404

	if movie:
		form.name.data = movie.name
		form.director.data = movie.director
		form.genre.data = movie.genre
		form.release_year.data = movie.release_year
		form.rating.data = movie.rating 

	return render_template('forms/edit_movie.html', form=form, movie=movie)

# route handler to update movie records
@app.route('/movies/<int:movie_id>/patch', methods=['POST'])
@requires_auth('post:movies')
def update_movie(movie_id, jwt):
	# get movie based on id
	movie = Movie.query.get(movie_id)
	error = False

	if movie is None:
		return json.dumps({
			'success': False,
			'error': 'Movie could not be found to be updated',
		}), 404

	
	try:
		new_name = request.form.get('name')
		movie.name = new_name
		new_director = request.form.get('director')
		movie.director = new_director
		new_genre = request.form.get('genre')
		movie.genre = new_genre
		new_release_year = request.form.get('release_year')
		movie.release_year = new_release_year
		new_rating = request.form.get('rating')
		movie.rating = new_rating

		movie.update()

	except:
		error = True

	if error:
		#On unsuccessful db insert, flash an error
		flash('Error: Movie ' + request.form['name'] + ' was not updated. Please check your inputs and try again :)')
	else:
		# On successful db insert, flash success
		flash(request.form['name'] + ' was successfully updated!')

	return render_template('pages/home.html')

# route handler to delete movies
@app.route('/movies/<int:movie_id>/delete', methods=['GET'])
@requires_auth('delete:movies')
def delete_movie(movie_id, jwt):
	# get movie to delete
	movie = Movie.query.get(movie_id) 
	error = False
	
	if movie is None:
		return json.dumps({
			'success': False,
			'error': 'Movie could not be found'
		}), 404

	try:
		movie.delete()

		# on successful db delete, flash success
		flash('Movie was successfully deleted!')

	except:
		error = True
		flash('An error occurred. This movie could not be deleted.')
	
	return render_template('pages/home.html')

#  Actors
#  ----------------------------------------------------------------
# route handler to get list of actors
@app.route('/actors', methods = ['GET'])
@cross_origin()
@requires_auth('get:actors')
def get_actors(jwt):
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
@requires_auth('get:actorform')
def create_actor_form(jwt):
	form = ActorForm()
	return render_template('forms/new_actor.html', form=form)

# route handler to create an actor profile in db
@app.route('/actors/create', methods=['POST'])
@requires_auth('post:actors')
def create_actor(jwt):
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

	except Exception as e:
		error = True

	if error:
		# On unsuccessful db insert, flash an error
		flash('Error: Actor ' + request.form['name'] + ' was not listed. Please check your inputs and try again :)')

	else:
		# on successful db insert, flash success
		flash(request.form['name'] + ' was successfully listed!')

	return render_template('pages/home.html')

# route handler to get individual actor records
@app.route('/actors/<int:actor_id>', methods=['GET'])
@requires_auth('get:actors')
def get_actor_details(actor_id, jwt):
	actor = Actor.query.get(actor_id)

	if actor is None:
		return json.dumps({
			'success': False,
			'error': 'Actor could not be found'
		}), 404

	actor_details = ({
		"id": actor.id,
		"name": actor.name,
		"age": actor.age,
		"gender": actor.gender,
		"image_link": actor.image_link
	})

	return render_template('pages/show_actor.html', actor=actor_details)

# route handler to get to form to update an actor record
@app.route('/actors/<int:actor_id>/patch', methods=['GET'])
@requires_auth('get:actorform')
def update_actor_form(actor_id, jwt):
	form = ActorForm()
	actor = Actor.query.get(actor_id)

	if actor is None:
		return json.dumps({
			'success': False,
			'error': 'Actor could not be found to be updated',
		}), 404

	if actor:
		form.name.data = actor.name
		form.age.data = actor.age
		form.gender.data = actor.gender
		form.image_link.data = actor.image_link 

	return render_template('forms/edit_actor.html', form=form, actor=actor)

# route handler to update actor records
@app.route('/actors/<int:actor_id>/patch', methods=['POST'])
@requires_auth('post:actors')
def update_actor(actor_id, jwt):
	# get movie based on id
	actor = Actor.query.get(actor_id)
	error = False

	if actor is None:
		return json.dumps({
			'success': False,
			'error': 'Actor could not be found to be updated',
		}), 404
	
	try:
		new_name = request.form.get('name')
		actor.name = new_name
		new_age = request.form.get('age')
		actor.age = new_age
		new_gender = request.form.get('gender')
		actor.gender = new_gender
		new_image_link = request.form.get('image_link')
		actor.image_link = new_image_link

		actor.update()

	except:
		error = True

	if error:
		#On unsuccessful db insert, flash an error
		flash('Error: Actor ' + request.form['name'] + ' was not updated. Please check your inputs and try again :)')
	else:
		# On successful db insert, flash success
		flash(request.form['name'] + ' was successfully updated!')

	return render_template('pages/home.html')

# route handler to delete actors
@app.route('/actors/<int:actor_id>/delete', methods=['GET'])
@requires_auth('delete:actors')
def delete_actor(actor_id, jwt):
	# get actor to delete
	actor = Actor.query.get(actor_id) 
	error = False
	
	if actor is None:
		return json.dumps({
			'success': False,
			'error': 'Actor could not be found'
		}), 404

	try:
		actor.delete()

		# on successful db delete, flash success
		flash('Actor was successfully deleted!')

	except:
		error = True
		flash('An error occurred. This actor could not be deleted.')
	
	return render_template('pages/home.html')

#  Cast a Movie
#  ----------------------------------------------------------------
# route handler to get to form to cast a movie
@app.route('/cast/create', methods=['GET'])
@requires_auth('get:castform')
def create_cast_form(jwt):				
	movies = Movie.query.all()
	actors = Actor.query.all()		

	return render_template('forms/new_cast.html', movies=movies, actors=actors)

# route handler to cast a movie in db
@app.route('/cast/create', methods=['POST'])
@requires_auth('post:cast')
def create_cast(jwt):
	error = False
	actor_id = request.form.get('actor_id')
	movie_id = request.form.get('movie_id')

	try:
		actor = Actor.query.get(actor_id)
		movie = Movie.query.get(movie_id)

		if actor is None:
			return json.dumps({
			'success': False,
			'error': 'Actor could not be found'
			}), 404

		if movie is None:
			return json.dumps({
			'success': False,
			'error': 'Movie could not be found'
			}), 404

		movie.cast.append(actor)
		movie.update()

	except:
		error = True
	
	if error:
		flash('Error: This actor was not cast. Please check your inputs and try again :)')

	else: 
		# success message upon succeesful casting
		flash('This actor was successfully booked!')

	return render_template('pages/home.html')

#----------------------------------------------------------------------------#
# Launch App
#----------------------------------------------------------------------------#
if __name__ == '__main__':
	app.run(debug=True)
