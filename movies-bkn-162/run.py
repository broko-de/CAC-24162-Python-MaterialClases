from flask import Flask
from app.database import init_app
from app.views import *
from flask_cors import CORS

#Crear una instancia de Flask
app = Flask(__name__)

init_app(app)
#permita solicitudes desde cualquier origen
CORS(app)

#asociacion de rutas con vistas
app.route('/', methods=['GET'])(index)
app.route('/api/movies/', methods=['GET'])(get_all_movies)
app.route('/api/movies/<int:movie_id>', methods=['GET'])(get_movie)
app.route('/api/movies/', methods=['POST'])(create_movie)
app.route('/api/movies/<int:movie_id>', methods=['PUT'])(update_movie)
app.route('/api/movies/<int:movie_id>', methods=['DELETE'])(delete_movie)

#Permite separa el codigo que se ejecuta cuando se corre el archivo
if __name__=='__main__':
    app.run(debug=True)