
'''
Defines the AlbumRepository class
'''
from lib.album import Album

class AlbumRepository:
    '''
    Controls the interaction between the Album class and the database
    '''
    def __init__(self, connection) -> None:
        '''
        Inits AlbumRepository class with connection to database.
        '''
        self._connection = connection

    def all(self) -> list[Album]:
        '''
        Method to get all rows from the albums table.
        '''
        rows = self._connection.execute("SELECT * FROM albums;")
        return [Album(row["id"], row["title"], row["release_year"], row["artist_id"]) for row in rows]

    def find(self, id) -> Album:
        '''
        Method to get album and associated artist info from album id.
        '''
        row = self._connection.execute("SELECT * FROM albums JOIN artists ON albums.artist_id=artists.id WHERE albums.id = %s;", [id])
        if row:
            album = Album(row[0]["id"], row[0]["title"], row[0]["release_year"], row[0]["artist_id"])
            album.artist_name = row[0]['name']
            return album

    def create(self, album) -> None:
        '''
        Method to create (add) an album to the albums table.
        '''
        self._connection.execute("INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)", [album.title, album.release_year, album.artist_id])

    def delete(self, id) -> None:
        '''
        Method to delete a row from the albums table, reflecting the given ID.
        '''
        self._connection.execute('DELETE FROM albums WHERE id = %s', [id])
