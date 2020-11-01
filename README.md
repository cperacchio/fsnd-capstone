# Movie Casting App 

This is my final project for the [Udacity Full Stack Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004). It's an app allowing a casting agency to cast actors for upcoming projects. 

#### Who's it for?
The Fyyur Casting Agency is responsible for creating movies and managing and assigning actors to those movies. The agency wants a new system to streamline the casting process, store information about actors and movies, and limit who has access to data based on their role.

#### How does it work?
The app has a page where movies projects are listed and a page where actor profiles are listed. It also has forms allowing you to create and update movie projects and actor profiles, and it has a form to match actors with movies in development. Casting an actor to a movie using the app will automatically update the casting details of that movie record. Now, the agency can:
- Easily cast actors to movies using the app
- Keep track of upcoming movie projects, actor profiles, and casting information, all in one place
- Control who can view, create, update, or delete casting information based on their role at the agency

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
Coming soon!
```

## Usage

### Casting app roles
Users can access the app's homepage anonymously and its functionality via two roles with specific access permissions:

1. <strong>Casting assistant</strong>: Can view upcoming movie projects and listed actors and see details about both
```
Sample casting assistant login credentials
User: fyyur.casting.assistant@gmail.com
Password: Auth0123!
JWT access token: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjExc0I4dXRPc1Rod2FOZV8xN25LZyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQ3OS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY5ZTAyOGUyNGY4MGEwMDc5NjNjOTRjIiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTYwNDI1Nzk3NiwiZXhwIjoxNjA0MzQ0Mzc2LCJhenAiOiJ0UXRaSzQ5bFU0MkZENnNSVEZGbnhPdm43QnB2SU5BaSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.MtK95YNNlCiv9ZlwMSorC3Z3EQjZbtZYTJsChnP3zIBoRfs-cEYQyIphzfxvsUeNDlvoMfEAW_-bF1lwUhp8Gmvjn4CPWUDn0CLu05kJRcTE8sUCCdUAFvJAHghLUxf8XCsRff4oSPEnW12w9IQnU0VFZmrKZIhczjoJ7zMxAfHS3Z5v2rqGW0R-kUkpVr1vqaQow-cv3n4PBHdufg17G5J7Ry2QWY1ieJovAB3JArW0XnB7eeI5Bt1N53hcqoTk4QzPRCinxxJ9_xFCdHD6MFDs8q8q9ZZo0opHVC2rIZG5ju4KJ0kRc3LANEeA6ePrLVUOjjNBlifoNcHlgQY6Nw
```

2. <strong>Executive producer</strong>: Full access, with the ability to view, list, update, and delete both movie projects and actors
```
Sample executive producer login credentials
User: shanna.rhymes@gmail.com
Password: Auth0123!
JWT access token: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjExc0I4dXRPc1Rod2FOZV8xN25LZyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQ3OS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY5ZTEyMTM5ZmU1MDUwMDdiNWVmYmEyIiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTYwNDI1NzgwMSwiZXhwIjoxNjA0MzQ0MjAxLCJhenAiOiJ0UXRaSzQ5bFU0MkZENnNSVEZGbnhPdm43QnB2SU5BaSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3Jmb3JtIiwiZ2V0OmFjdG9ycyIsImdldDpjYXN0Zm9ybSIsImdldDptb3ZpZWZvcm0iLCJnZXQ6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0OmNhc3QiLCJwb3N0Om1vdmllcyJdfQ.Gan6e4JKvVkI8UH3WWlyiiZrI3-o_FLXcK67hO18nlY5Z0ms1HAPvtrwYrFm9Qni5e85IoyQzvzstargslw8wOczLT_zT3rQQ0C5DloCA-VxSLOuMzoj8qNfrEG77qO5Ojv85uTqHJ2IDYhYv5aZt5sV-Utf79KC83VGnioGD8JTnj8cbH4701RjMGHCatY-svOxe8GH0G8StIGMLq1bD7lszg8_hZzx9mpxnvgqnCws-QGFuCMmhRrYqq03p3O1_Bb8wfICwZfZpOcHqWP61C1NK5CanIRPRPwQxFjYPUPQGbb2g7mif0Exp26S3aPCLR3W0ShwCl9ost9fAZLpew 
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

### Error handling
