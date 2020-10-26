# Movie Casting App 

This is my final project for the [Udacity Full Stack Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004). It's an app allowing a casting agency to cast actors for upcoming projects. 

#### Who's it for?
The Fyyur Casting Agency is responsible for creating movies and managing and assigning actors to those movies. The agency wants to create a system to streamline the casting process, manage information about actors and movies, and limit who has access to data based on their role.

#### How does it work?
The app has a page where movies are listed, a page where actors are listed, and a form allowing you to match actors with movies in development. Casting an actor to a movie will update the details of that movie record, giving the agency an easy way to keep track of the casting process. Now, the agency can:
- Easily cast actors to movies using the app
- Keep track of upcoming movie projects, actor profiles, and casting information all in one place
- Control who can view, creat, update, or delete casting information, based on their role at the agency

## Skills covered
- Coding in Python 3
- Relational database architecture
- Modeling data objects with SQLAlchemy
- Internet protocols and communication
- Developing a Flask API
- Authentication and access
- Authentication with Auth0
- Authentication in Flask
- Role-based access control (RBAC)
- Testing Flask applications
- Deploying applications

## Dependencies
To access it, you need to activate a virtual environment and install the dependencies:
1. Activate a virtual environment:
```
$ cd PROJECT_DIRECTORY_PATH/
$ virtualenv env
$ source env/bin/activate
```
2. Install the dependencies for this project:
```
$ pip3 install -r requirements.txt
```

## Setup
Next, you need to start the development server:  
```
$ export FLASK_APP=app.py 
$ export FLASK_ENV=development # enables debug mode  
$ flask run --reload
```

## Link to app deployed on Heroku
```
...
```

## Usage

### Casting app roles
Users can access the app's functionality via two roles, each with specific access permissions:

1. <strong>Casting assistant</strong>: Can view upcoming movie projects and listed actors and see details about both
```
Sample casting assistant login credentials
User:
Password:
```

2. <strong>Executive producer</strong>: Full access, with the ability to view, list, and delete both movie projects and actors
```
Sample executive producer login credentials
User:
Password:
```

### API endpoints
This casting app API includes the following endpoints. Below is an overview of their expected behavior.

#### GET /login
- Redirects the user to the Auth0 login page, where the user can log in or sign up

#### GET /movies
- Returns a list of all the movie projects in the database

#### GET /actors
- Returns a list of all the actors in the database

#### GET /movies/{movie_id}
- Returns details about each individual movie project listed in the database

#### GET /actors/{actor_id}
- Returns details about each individual actor listed in the database

#### GET /movies/create
- Returns the form to list a movie project

#### GET /actors/create
- Returns the form to list an actor profile

#### POST /movies/create
- Adds a new movie project to the database, including the movie's name, genre, release year, and rating

#### POST /actors/create
- Adds a new actor profile to the database, including the actor's name, age, and gender

#### GET /movies/{movie_id}/patch
- Updates an existing movie project, with revised details related to the movie's name, genre, release year, or rating

#### GET /actors/{actor_id}/patch
- Updates an existing actor profile, with revised details related to the actor's name, age, or gender

#### GET /movies/{movie_id}/delete
- Deletes a movie project from the database

#### GET /actors/{actor_id}/delete
- Deletes an actor profile from the database

#### GET /cast/create
- Returns the form to cast an actor to a movie project

#### POST /cast/create
- Casts an actor to an upcoming movie project by appending the actor to the movie's cast in the database
