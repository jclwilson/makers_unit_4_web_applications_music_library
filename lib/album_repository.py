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

    def find(self, id: int) -> dict | None:
        """Find a single album with a given ID."""
        rows = self._connection.execute(
                "SELECT albums.*, artists.id AS artist_id, artists.name, artists.genre FROM albums LEFT JOIN artists ON artists.id = albums.artist_id WHERE albums.id = %s;", [id]
        )
        if rows:
            album = Album(
                rows[0]["id"],
                rows[0]["title"],
                rows[0]["release_year"],
                rows[0]["artist_id"],
            )
            artist = Artist(rows[0]["artist_id"], rows[0]["name"], rows[0]["genre"])
            return {"artist": artist, "album": album}
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

    def delete(self, id: int) -> object:
        """Delete a row from the albums table, reflecting the given ID."""
        rows = self._connection.execute("DELETE FROM albums WHERE id = %s RETURNING *", [id])
        return rows[0]
