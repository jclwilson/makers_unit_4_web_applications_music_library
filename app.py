''''
Entry point to music library application.
'''

import os

from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album

from flask import Flask, request, render_template

# Create a new Flask app
app: Flask = Flask(__name__)

@app.route('/')
def index():
    return "Music Library App"

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
    album = album_repository.find(id)
    if len(album) > 0:
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

'''
Start app
'''

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

