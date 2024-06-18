from flask import jsonify
from app.models import Movie

def index():
    response = {'message':'Hola mundo API FLASK 🐍'}
    return jsonify(response)

#funcion que busca todo el listado de las peliculas
def get_all_movies():
    movies = Movie.get_all()
    list_movies = [movie.serialize() for movie in movies]
    return jsonify(list_movies)

#funcion que busca una pelicula
def get_movie():
    pass

def create_movie():
    pass

def update_movie():
    pass

def delete_movie():
    pass