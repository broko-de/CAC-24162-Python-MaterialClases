from app.database import get_db

class Movie:
    #CONSTRUCTOR
    def __init__(self,id_movie=None,title=None,director=None,release_date=None,banner=None):
        self.id_movie = id_movie
        self.title = title
        self.director = director
        self.release_date = release_date
        self.banner = banner

    @staticmethod    
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM movies")
        rows = cursor.fetchall()
        movies = [Movie(id_movie=row[0], title=row[1], director=row[2], release_date=row[3], banner=row[4]) for row in rows]
        # movies = []
        # for row in rows:
        #     new_movie =  Movie(row[0],row[1],row[2],row[3],row[4])
        #     movies.append(new_movie)
        cursor.close()
        return movies

    def save(self):
        #logica para INSERT/UPDATE en base datos
        pass

    def delete(self):
        #logica para hacer un DELETE en la BASE
        pass
    
    def serialize(self):
        return {
            'id_movie': self.id_movie,
            'title': self.title,
            'director': self.director,
            'release_date': self.release_date,
            'banner': self.banner,
        }
    
    