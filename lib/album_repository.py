"""Defines the AlbumRepository class."""

from lib.album import Album
from lib.artist import Artist


class AlbumRepository:
    """Controls the interaction between the Album class and the database."""

    def __init__(self, connection) -> None:
        """Init AlbumRepository class with connection to database."""
        self._connection = connection

    def all(self) -> list[Album] | None:
        """Get all rows from the albums table."""
        rows = self._connection.execute("SELECT * FROM albums;")
        if len(rows) > 0:
            return [
                Album(row["id"], row["title"], row["release_year"], row["artist_id"])
                for row in rows
            ]
        return None

    def find(self, id: int) -> Album | None:
        """Find a single album with a given ID."""
        row = self._connection.execute(
            "SELECT * FROM albums WHERE albums.id = %s;", [id]
        )
        if len(row) > 0:
            return Album(
                row[0]["id"],
                row[0]["title"],
                row[0]["release_year"],
                row[0]["artist_id"],
            )
        return None

    def get_album_artist(self, id: int) -> dict | None:
        """Get album and associated artist info from album id."""
        row = self._connection.execute(
            "SELECT albums.id AS album_id, albums.title, albums.release_year, \
                albums.artist_id, artists.id, artists.name AS artist_name, artists.genre \
                FROM albums JOIN artists ON albums.artist_id = artists.id \
                WHERE albums.id = %s ORDER BY albums.release_year;",
            [id],
        )
        if len(row) > 0:
            album = Album(
                row[0]["album_id"],
                row[0]["title"],
                row[0]["release_year"],
                row[0]["artist_id"],
            )
            artist = Artist(row[0]["artist_id"], row[0]["artist_name"], row[0]["genre"])
            return {"album":album, "artist": artist}
        return None

    def create(self, album: Album) -> object:
        """Create (add) an album to the albums table."""
        rows = self._connection.execute(
            "INSERT INTO albums (title, release_year, artist_id) \
                    VALUES (%s, %s, %s) RETURNING id",
            [album.title, album.release_year, album.artist_id],
        )
        row = rows[0]
        album.id = row["id"]
        return album

    def delete(self, id: int) -> None:
        """Delete a row from the albums table, reflecting the given ID."""
        self._connection.execute("DELETE FROM albums WHERE id = %s", [id])
