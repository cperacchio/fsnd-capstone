#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
import os
from flask import Flask, request, abort, jsonify, render_template, session
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from models import setup_db, Movie, Actor
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

	return render_template('pages/movies.html')

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
  try:
    # add user-submitted data and commit to db
    movie = Movie(
      name = request.form.get('name'),
      director = request.form.get('director'),
      genre = request.form.get('genre'),
      release_year = request.form.get('release_year'),
      rating = request.form.get('rating'),
      actors = request.form.getlist('actors')
    )
    db.session.add(movie)
    db.session.commit()

  except Exception as e:
    error = True
    db.session.rollback()
    print(f'Error ==> {e}')
  finally:
    db.session.close()
  
  if error:
    # On unsuccessful db insert, flash an error
    flash('Error: Movie ' + request.form['name'] + ' was not listed. Please check your inputs and try again :)')
  else:
    # on successful db insert, flash success
    flash(request.form['name'] + ' was successfully listed!')

  return render_template('pages/home.html')

# route handler to update movie records
@app.route('/movies/<id>', methods=['PATCH'])
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
@app.route('/movies/<movie_id>', methods=['DELETE'])
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

	return render_template('pages/actors.html')

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
  try:
    # add user-submitted data and commit to db
    actor = Actor(
      name = request.form.get('name'),
      age = request.form.get('release_year'),
      gender = request.form.get('rating'),
      image_link = request.form.get('image_link')
    )
    db.session.add(actor)
    db.session.commit()

  except Exception as e:
    error = True
    db.session.rollback()
    print(f'Error ==> {e}')
  finally:
    db.session.close()
  
  if error:
    # On unsuccessful db insert, flash an error
    flash('Error: Actor ' + request.form['name'] + ' was not listed. Please check your inputs and try again :)')
  else:
    # on successful db insert, flash success
    flash(request.form['name'] + ' was successfully listed!')

  return render_template('pages/home.html')

# route handler to update actor records
@app.route('/actors/<id>', methods=['PATCH'])
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
@app.route('/actors/<actor_id>', methods=['DELETE'])
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

	return render_template('forms/new_cast.html', movies=movies, actors=actors), 200

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
			abort(404)
			flash('Error: Please check your inputs')

		movie.cast.append(actor)
		movie.update()

		# success message upon succeesful casting
		flash(request.form['name'] + ' was successfully cast!')

	except:
		error = True
		flash('Error: Actor ' + request.form['name'] + ' was not cast. Please check your inputs and try again :)')

	return render_template('pages/home.html')

#----------------------------------------------------------------------------#
# Launch App
#----------------------------------------------------------------------------#
if __name__ == '__main__':
    app.run(debug=True)
