#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db

#----------------------------------------------------------------------------#
# Initialize App 
#----------------------------------------------------------------------------#
def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
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
@app.route('/movies')
def movies():
	movies = Movie.query.all()

# route handler to create a movie record in db
@app.route('/movies/create', methods=['POST'])
def create_movie():

  # catch errors with try/except
  error = False
  try:
    # add user-submitted data and commit to db
    movie = Movie(
      title = request.form.get('title'),
      release_year = request.form.get('release_year'),
      director = request.form.get('director'),
      rating = request.form.get('rating'),
      run_time = request.form.get('run_time'),
      box_office = request.form.get('box_office'),
      actors = request.form.getlist('actors')
    )
    db.session.add(venue)
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
@app.route('/actors')
def movies():
	actors = Actor.query.all()

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

#  Directors
#  ----------------------------------------------------------------
@app.route('/directors')
def directors():
	directors = Director.query.all()

# route handler to delete directors
@app.route('/directors/<director_id>', methods=['DELETE'])
def delete_director(director_id):
  try:
    # get movie to delete
    director = Director.query.get(director_id) 
    db.session.delete(director)
    db.session.commit()

    # on successful db delete, flash success
    flash('Director ' + request.form['name'] + ' was successfully deleted!')

  except:
    db.session.rollback()
    flash('An error occurred. Director ' + request.form['name'] + ' could not be deleted.')
  finally:
    db.session.close()

  return render_template('pages/home.html')

#----------------------------------------------------------------------------#
# Launch App
#----------------------------------------------------------------------------#
if __name__ == '__main__':
    app.run(debug=True)
