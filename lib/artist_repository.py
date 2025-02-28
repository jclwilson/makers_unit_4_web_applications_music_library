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

    def find(self, artist_id):
        rows = self._connection.execute(
            "SELECT * from artists WHERE id = %s", [artist_id]
        )
        row = rows[0]
        return Artist(row["id"], row["name"], row["genre"])

    def get_artist_albums(self, artist_id):
        artist = self.find(artist_id)
        albums = self.get_all_albums_by_artist(artist_id)
        return {"artist": artist, "albums": albums}

    def get_all_albums_by_artist(self, artist_id: int) -> list | None:
        """Returns all albums by given artist."""
        rows = self._connection.execute("SELECT * FROM albums WHERE artist_id = %s", [artist_id])
        albums = []
        for row in rows:
            album = Album(
                row["id"],
                row["title"],
                row["release_year"],
                row["artist_id"],
            )
            albums.append(album)
        return albums

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
