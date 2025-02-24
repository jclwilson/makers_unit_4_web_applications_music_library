''''
Entry point to music library application.
'''

import os

from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository

from flask import Flask, request

# Create a new Flask app
app: Flask = Flask(__name__)

@app.route('/albums', methods=['GET'])
def get_all_albums() -> str:
    '''
    Returns all albums to the browser.
    :param artist_repository: The object holding the database connection.
    '''
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    albums = album_repository.all()
    results = []
    for album in albums:
        results.append(f"{album.title} ({album.release_year})")
    return results

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
