class Movie:
    def __init__(self):
        self.id_movie
        self.title
        self.director
        self.release_date
        self.banner
    
    def save(self):
        #logica para INSERT/UPDATE en base datos
        pass

    def delete(self):
        #logica para hacer un DELETE en la BASE
        pass

    def get_all(self):
        #logica para traer todas las peliculas
        pass
    
movies = [
    {
        'id_movie':1,
        'title':'Inception',
        'director':'Christopher Nolan',
        'release_date':'2010-07-16',
        'banner':'inception_banner.jpg'
    },
    {
        'id_movie':2,
        'title':'The Godfather',
        'director':'Francis Ford Coppola',
        'release_date':'1972-03-24',
        'banner':'godfather_banner.jpg'
    },
    {
        'id_movie':3,
        'title':'Forrest Gump',
        'director':'Robert Zemeckis',
        'release_date':'1994-07-06',
        'banner':'forrestgump_banner.jpg'
    },
    {
        'id_movie':4,
        'title':'Titanic',
        'director':'James Cameron',
        'release_date':'1997-12-19',
        'banner':'titanic_banner.jpg'
    },
    {
        'id_movie':5,
        'title':'Gladiator',
        'director':'Ridley Scott',
        'release_date':'2000-05-05',
        'banner':'gladiator_banner.jpg'
    }
]