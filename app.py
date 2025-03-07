"""'
Entry point to music library application.
"""

from flask import Flask, redirect, render_template, request

from lib.album import Album
from lib.album_repository import AlbumRepository
from lib.artist import Artist
from lib.artist_repository import ArtistRepository
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app: Flask = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    """Return 404 page on 404 error."""
    return render_template("404.html"), 404


@app.route("/seed", methods=["GET"])
def seed():
    """Seed database manually by calling this route"""
    connection = get_flask_database_connection(app)
    connection.seed("seeds/music_library.sql")
    return redirect( url_for("index"), code=200)


@app.route("/")
def index() -> str:
    """Return home template on index route"""
    return render_template("home.html")


@app.route("/albums", methods=["GET"])
def get_all_albums() -> str:
    """Return all albums to the browser."""
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    albums = album_repository.all()
    if len(albums) > 0:
        return render_template("albums.html", albums=albums)
    return render_template("404.html"), 404


@app.route("/albums/<int:id>", methods=["GET"])
def get_album(id):
    """Return one album to the browser, specified by id."""
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    album_info = album_repository.find(id)
    if album_info:
        return render_template("album.html", artist=album_info["artist"], album=album_info["album"])
    return render_template("404.html"), 404


@app.route("/albums/new", methods=["GET"])
def get_new_album() -> str:
    """Return HTML form to add new album."""
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    artists = artist_repository.all()
    return render_template("add_album.html", artists=artists)


@app.route("/albums/new", methods=["POST"])
def add_new_album() :
    """Add an album to the database via a POST request."""
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    album_title: str = request.form["album-title"]
    album_release_year: str = request.form["album-release-year"]
    album_artist_id: int = request.form["album-artist-id"]
    album: Album = Album(None, album_title, album_release_year, album_artist_id)
    if album.is_valid():
        album = album_repository.create(album)
        return redirect(f"/albums/{album.id}")
    return render_template("add_album.html", album=album, errors=album.generate_errors()), 400


@app.route("/albums/delete/<int:id>", methods=["POST"])
def delete_album(id):
    """Delete album of given ID"""
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    album = album_repository.delete(id)
    return render_template("delete_album.html", album=album), 202
    

@app.route("/artists", methods=["GET"])
def get_all_artists():
    """Returns all artists to the browser."""
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    artists = artist_repository.all()
    if len(artists) > 0:
        return render_template("artists.html", artists=artists)
    return render_template("404.html"), 404


@app.route("/artists/<int:id>", methods=["GET"])
def get_artist(id):
    """Returns one artist to the browser, specified by id."""
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    artist_info = artist_repository.get_artist_albums(id)
    if artist_info["artist"]:
        return render_template("artist.html", artist=artist_info["artist"], albums=artist_info["albums"])
    return render_template("404.html"), 404

@app.route("/artists/new", methods=["GET"])
def get_new_artist() -> str:
    """Return HTML form to add new artist"""
    return render_template("add_artist.html")

@app.route("/artists/new", methods=["POST"])
def add_new_artist() -> str:
    """Adds an artist to the database via a POST request."""
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    artist_name: str = request.form["artist-name"]
    artist_genre: str = request.form["artist-genre"]
    artist: Artist = Artist(None, artist_name, artist_genre)
    if artist.is_valid():
        new_artist = artist_repository.create(artist)
        return redirect(f"/artists/{new_artist.id}")
    return render_template("add_artist.html", errors=artist.generate_errors()), 400

@app.route("/artists/delete/<int:id>", methods=["POST"])
def delete_artist(id):
    """Delete artist of given ID"""
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    artist = artist_repository.delete(id)
    return render_template("delete_artist.html", artist=artist), 202
    

"""
Start app
"""

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
