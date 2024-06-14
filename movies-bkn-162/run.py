from flask import Flask
from app.views import *

#Crear una instancia de Flask
app = Flask(__name__)

#asociacion de rutas con vistas
app.route('/',methods=['GET'])(index)
app.route('/api/movies/',methods=['GET'])(get_all_movies)

#Permite separa el codigo que se ejecuta cuando se corre el archivo
if __name__=='__main__':
    app.run(debug=True)