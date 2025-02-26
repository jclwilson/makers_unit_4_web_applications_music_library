''''
Entry point to music library application.
'''

import os

from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist

from flask import Flask, request, render_template

# Create a new Flask app
app: Flask = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/albums', methods=['GET'])
def get_all_albums():
    '''
    Returns all albums to the browser.
    '''
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    albums = album_repository.all()
    if len(albums) > 0:
        return render_template('albums.html', albums=albums)
    else:
        return render_template('404.html')

@app.route('/albums/<id>', methods=['GET'])
def get_album(id):
    '''
    Returns one album to the browser, specified by id
    '''
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    album = album_repository.get_album_artist(id)
    if album:
        return render_template('album.html', album=album)
    else:
        return render_template('404.html')

@app.route('/albums', methods=['POST'])
def add_album():
    '''
    Adds an album to the database via a POST request
    '''
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    album_title: str = request.form['title']
    album_release_year: str = request.form['release_year']
    album_artist_id: str = request.form['artist_id']
    new_album: Album = Album(None, album_title, album_release_year, album_artist_id)
    album_repository.create(new_album)
    return ''

@app.route('/artists', methods=['GET'])
def get_all_artists():
    '''
    Returns all artists to the browser.
    '''
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    artists = artist_repository.all()
    if len(artists) > 0:
        return render_template('artists.html', artists=artists)
    else:
        return render_template('404.html')

@app.route('/artists/<id>', methods=['GET'])
def get_artist(id):
    '''
    Returns one artist to the browser, specified by id
    '''
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    artist = artist_repository.get_artist_albums(id)
    if artist:
        return render_template('artist.html', artist=artist)
    else:
        return render_template('404.html')

@app.route('/artists', methods=['POST'])
def add_artist():
    '''
    Adds an artist to the database via a POST request
    '''
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    artist_name: str = request.form['name']
    artist_genre: str = request.form['artist_genre']
    new_artist: Artist = Artist(None, artist_name, artist_genre)
    artist_repository.create(new_artist)
    return ''

'''
Start app
'''

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

