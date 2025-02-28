from lib.album import Album
from lib.artist import Artist


class ArtistRepository:
    # We initialise with a database connection
    def __init__(self, connection) -> None:
        self._connection = connection

    # Retrieve all artists
    def all(self):
        rows = self._connection.execute("SELECT * from artists")
        artists = []
        for row in rows:
            item = Artist(row["id"], row["name"], row["genre"])
            artists.append(item)
        return artists

    # Find a single artist by their id
    def find(self, artist_id):
        rows = self._connection.execute(
            "SELECT * from artists WHERE id = %s", [artist_id]
        )
        row = rows[0]
        return Artist(row["id"], row["name"], row["genre"])

    def get_artist_albums(self, artist_id):
        # Find a single artist by their id
        rows = self._connection.execute(
            "SELECT albums.id AS album_id, albums.title, albums.release_year, albums.artist_id, artists.id, artists.name, artists.genre from albums JOIN artists ON artists.id = albums.artist_id WHERE artists.id = %s ORDER BY albums.release_year",
            [artist_id],
        )
        if rows:
            artist = Artist(rows[0]["id"], rows[0]["name"], rows[0]["genre"])
            albums = []
            for row in rows:
                albums.append(
                    Album(
                        row["album_id"],
                        row["title"],
                        row["release_year"],
                        row["artist_id"],
                    )
                )
            return {'artist': artist, 'albums': albums}
        return None

    # Create a new artist
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, artist) -> None:
        self._connection.execute(
            "INSERT INTO artists (name, genre) VALUES (%s, %s)",
            [artist.name, artist.genre],
        )
        return

    # Delete an artist by their id
    def delete(self, artist_id) -> None:
        self._connection.execute("DELETE FROM artists WHERE id = %s", [artist_id])
        return
