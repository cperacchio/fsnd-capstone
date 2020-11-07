# Movie Casting App 

This is my final project for the [Udacity Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004). It's an app allowing a casting agency to cast actors for upcoming movie projects. 

#### Who's it for?
The Fyyur Casting Agency is responsible for creating movies and managing and assigning actors to those movies. The agency wants a new system to streamline the casting process, store information about actors and movies, and limit who has access to data based on their role.

#### How does it work?
The app has a page where movie projects are listed and a page where actor profiles are listed. It has pages allowing the agency to create and update both movie projects and actor profiles. And it has a page to match actors with movies in development. Casting an actor for a movie using the app will automatically update the casting details of that movie record. Now, the agency can:
- Easily cast actors for movies using the app
- Keep track of upcoming movie projects, actor profiles, and casting information, all in one place
- Control who can view, create, update, or delete casting information based on their role at the agency

#### How can I access the app?
The casting app has been deployed to Heroku and is currently working at this link: 
```
[https://fsnd-capstone-cperacchio.herokuapp.com](https://fsnd-capstone-cperacchio.herokuapp.com/)
```

To log in, add /login to the url and enter one set of credentials shown below. To log out, just go to /logout.

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
To access the app locally, you need a database, a virtual environment, dependencies installed, and environment variables set up. You also need an account with Auth0, the authentication service I used to secure this app and its API.

1. This app runs on a PostgreSQL database. You can download PostgreSQL at [postgresql.org](https://www.postgresql.org/download/).
2. Then head to [Auth0.com](https://auth0.com/) to create an account.
3. Next, activate a virtual environment:
```
$ cd project_directory_path/
$ virtualenv env
$ source env/bin/activate
```
4. Install the dependencies for this project and set up environment variables:
```
source setup.sh
```

## Setup
1. Create a PostgreSQL database locally and connect to it from setup.sh:
```
export DATABASE_URL='postgresql://your_user_name@localhost:XXXX/your_db_name'
```
2. In Auth0, configure a single page web application and its API, relying on the environment variables in setup.sh.
3. Start the development server:  
```
$ export FLASK_APP=app.py 
$ export FLASK_ENV=development # enables debug mode  
$ flask run --reload
```

## Usage

### Casting app roles
Users can access the app's homepage anonymously and its functionality via two roles with specific access permissions.

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
To access this app's API, a user needs to be authenticated. Logging in with approved credentials generates a JWT (JSON Web Token) that grants the user access based on their role's permissions.

The casting app API includes the following endpoints. Below is an overview of their expected behavior.

#### GET /login
- Redirects the user to the Auth0 login page, where the user can log in or sign up
- Roles authorized: all users
- Sample: ```curl http://127.0.0.1:5000/login```

#### GET /post-login
- Handles the response from the access token endpoint and stores the user's information in a Flask session
- Roles authorized: casting assistant, executive producer
- Sample: ```curl http://127.0.0.1:5000/post-login```

#### GET /logout
- Clears the user's session and logs them out
- Roles authorized: all users
- Sample: ```curl http://127.0.0.1:5000/logout```

#### GET /movies
- Returns a list of all the movie projects in the database
- Roles authorized: casting assistant, executive producer
- Sample: ```curl http://127.0.0.1:5000/movies```

#### GET /actors
- Returns a list of all the actors in the database
- Roles authorized: casting assistant, executive producer
- Sample: ```curl http://127.0.0.1:5000/actors```

#### GET /movies/{movie_id}
- Returns details about each individual movie project listed in the database
- Roles authorized: casting assistant, executive producer
- Sample: ```curl http://127.0.0.1:5000/movies/1```

#### GET /actors/{actor_id}
- Returns details about each individual actor listed in the database
- Roles authorized: casting assistant, executive producer
- Sample: ```curl http://127.0.0.1:5000/actors/1```

#### GET /movies/create
- Returns the form to list a movie project
- Roles authorized: executive producer
- Sample: ```curl http://127.0.0.1:5000/movies/create```

#### GET /actors/create
- Returns the form to list an actor profile
- Roles authorized: executive producer
- Sample: ```curl http://127.0.0.1:5000/actors/create```

#### POST /movies/create
- Adds a new movie project to the database, including the movie's name, genre, release year, and rating
- Roles authorized: executive producer
- Sample: ```curl http://127.0.0.1:5000/movies/create -X POST -H "Content-Type: application/json" -d '{ "name": "A Star is Born 2", "director": "Bradley Cooper", "genre": "Musical", "release_year": 2023, "rating": "R"}'```

#### POST /actors/create
- Adds a new actor profile to the database, including the actor's name, age, gender, and profile image
- Roles authorized: executive producer
- Sample: ```curl http://127.0.0.1:5000/actors -X POST -H "Content-Type: application/json" -d '{ "name": "Ana de Armas", "age": 32, "gender": "Female", "image_link": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Ana_de_Armas_by_Gage_Skidmore.jpg/220px-Ana_de_Armas_by_Gage_Skidmore.jpg"}'```

#### GET /movies/{movie_id}/patch
- Returns the form to update a movie project
- Roles authorized: executive producer
- Sample: ```curl http://127.0.0.1:5000/movies/1/patch```

#### GET /actors/{actor_id}/patch
- Returns the form to update an actor profile
- Roles authorized: executive producer
- Sample: ```curl http://127.0.0.1:5000/actors/1/patch```

#### GET /movies/{movie_id}/patch
- Updates an existing movie project, with revised details related to the movie's name, genre, release year, or rating
- Roles authorized: executive producer
- Sample: ```curl http://127.0.0.1:5000/movies/1 -X POST -H "Content-Type: application/json" -d '{ "name": "A Star is Born 2", "director": "Lady Gaga", "genre": "Comedy", "release_year": 2024, "rating": "R"}'```

#### GET /actors/{actor_id}/patch
- Updates an existing actor profile, with revised details related to the actor's name, age, gender, or profile image
- Roles authorized: executive producer
- Sample: ```curl http://127.0.0.1:5000/actors/1 -X POST -H "Content-Type: application/json" -d '{ "name": "Ana de Armas", "age": 32, "gender": "Female" , "image_link": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Ana_de_Armas_GQ_2018_2.png/165px-Ana_de_Armas_GQ_2018_2.png"}'```

#### GET /movies/{movie_id}/delete
- Deletes a movie project from the database
- Roles authorized: executive producer
- Sample: ```curl http://127.0.0.1:5000/movies/1/delete```

#### GET /actors/{actor_id}/delete
- Deletes an actor profile from the database
- Roles authorized: executive producer
- Sample: ```curl http://127.0.0.1:5000/actors/1/delete```

#### GET /cast/create
- Returns the form to cast an actor for a movie project
- Roles authorized: executive producer
- Sample: ```curl http://127.0.0.1:5000/cast/create```

#### POST /cast/create
- Casts an actor for an upcoming movie project by appending the actor to the movie's cast in the database
- Roles authorized: executive producer
- Sample: ```curl http://127.0.0.1:5000/cast/create -X POST -H "Content-Type: application/json" -d '{ "name": "The Pink Panther 2", "director": "Nancy Meyers", "genre": "Action", "release_year": 2022, "rating": "G", "cast": "Ana de Armas"}'```

### Error handling
The error codes currently returned are:
- 400: Bad request  
- 401: Unauthorized
- 404: Resource not found
- 422: Unprocessable
- 500: Internal server error
- AuthError: Auth0 error status code and description