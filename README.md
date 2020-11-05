# Movie Casting App 

This is my final project for the [Udacity Full Stack Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004). It's an app allowing a casting agency to cast actors for upcoming projects. 

#### Who's it for?
The Fyyur Casting Agency is responsible for creating movies and managing and assigning actors to those movies. The agency wants a new system to streamline the casting process, store information about actors and movies, and limit who has access to data based on their role.

#### How does it work?
The app has a page where movies projects are listed and a page where actor profiles are listed. It also has forms allowing you to create and update movie projects and actor profiles, and it has a form to match actors with movies in development. Casting an actor to a movie using the app will automatically update the casting details of that movie record. Now, the agency can:
- Easily cast actors to movies using the app
- Keep track of upcoming movie projects, actor profiles, and casting information, all in one place
- Control who can view, create, update, or delete casting information based on their role at the agency

#### How can I access the app?
The casting app has been deployed to Heroku and is currently working at this link: 

[https://fsnd-capstone-cperacchio.herokuapp.com](https://fsnd-capstone-cperacchio.herokuapp.com/)

To log in, add /login to the url and enter one set of credentials. To log out, just go to /logout.

![homepage](https://github.com/cperacchio/fsnd-capstone/blob/main/static/img/new_landing_page.png?raw=true)

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
To access it locally, you need to activate a virtual environment and install the dependencies:
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

## Usage

### Casting app roles
Users can access the app's homepage anonymously and its functionality via two roles with specific access permissions:

1. <strong>Casting assistant</strong>: Can view upcoming movie projects and listed actors and see details about both
```
Casting assistant login credentials
User: fyyur.casting.assistant@gmail.com
Password: Auth0123!
```

2. <strong>Executive producer</strong>: Full access, with the ability to view, list, update, and delete both movie projects and actors
```
Executive producer login credentials
User: shanna.rhymes@gmail.com
Password: Auth0123! 
```

### API endpoints
This casting app API includes the following endpoints. Below is an overview of their expected behavior.

#### GET /login
- Redirects the user to the Auth0 login page, where the user can log in or sign up

#### GET /post-login
- Handles the response from the access token endpoint and stores the user's information in a Flask session

#### GET /logout
- Clears the user's session and logs them out

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

### Error handling
The error codes currently returned are:
- 400: Bad request  
- 401: Unauthorized
- 404: Resource not found
- 422: Unprocessable
- 500: Internal server error
- AuthError: Auth0 error status code and description