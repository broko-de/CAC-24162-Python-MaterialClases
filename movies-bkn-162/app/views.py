from flask import jsonify
from app.models import movies

def index():
    response = {'message':'Hola mundo API FLASK 🐍'}
    return jsonify(response)

#funcion que busca una pelicula
def get_movie():
    pass

#funcion que busca todo el listado de las peliculas
def get_all_movies():
    return jsonify(movies)

def create_movie():
    pass

def update_movie():
    pass

def delete_movie():
    pass