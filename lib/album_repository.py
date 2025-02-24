
'''
Defines the AlbumRepository class
'''
from lib.album import Album

class AlbumRepository:
    def __init__(self, connection):
        '''
        Inits AlbumRepository class with connection to database.
        '''
        self._connection = connection

    def all(self):
        '''
        Method to get all rows from the albums table.
        '''
        rows = self._connection.execute("SELECT * FROM albums;")
        return [Album(row["id"], row["title"], row["release_year"], row["artist_id"]) for row in rows]

    def find(self, id):
        '''
        Method to get a single row from the albums table, reflecting a given ID
        '''
        rows = self._connection.execute("SELECT * FROM albums WHERE id = %s;", [id])
        return [Album(row["id"], row["title"], row["release_year"], row["artist_id"]) for row in rows]

    def create(self, album):
        '''
        Method to create (add) an album to the albums table.
        '''
        self._connection.execute("INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)", [album.title, album.release_year, album.artist_id])
        return None

    def delete(self, id):
        '''
        Method to delete a row from the albums table, reflecting the given ID.
        '''
        self._connection.execute('DELETE FROM albums WHERE id = %s', [id])
        return None

