''''
Entry point to music library application.
'''

from os import system, name
import sys

from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
from lib.artist import Artist
from lib.album import Album

class Application:
    '''
    Runs the music library application
    '''
    def __init__(self) -> None:
        '''
        Initialises the connection to the database
        and seeds the database with data
        '''
        # Connect to the database
        self._connection = DatabaseConnection()
        self._connection.connect()
        # Seed with some seed data
        self._connection.seed("seeds/music_library.sql")

    def clear(self) -> None:
        '''
        Function to clear terminal screen.
        '''
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

    def continue_menu(self):
        '''
        Displays menu asking whether to continue / quit
        '''
        choice = ''
        while choice == '':
            print('\n\nWhat do you want to do?\n')
            print('\tm) Go to main menu')
            print('\n\tq) Quit')
            choice = input('\nChoose an option:\n\t')
            match choice:
                case 'q':
                    sys.exit()
                case 'm':
                    return ''
                case _:
                    choice = ''

    def print_artists(self, artist_repository) -> None:
        '''
        Prints all artists to the terminal
        :param artist_repository: The object holding the database connection.
        '''
        self.clear()
        artists = artist_repository.all()

        print('All artists:\n')
        for artist in artists:
            print(f"\t{artist.id}: {artist.name} ({artist.genre})")
        return None

    def print_albums(self, album_repository)-> None:
        '''
        Prints all albums to the terminal
        :param album_repository: The object holding the database connection.
        '''
        self.clear()
        albums = album_repository.all()

        print('All albums:\n')
        for album in albums:
            print(f"\t{album.id}: {album.title} ({album.release_year})")
        return None

    def add_artist(self, artist_repository) -> None:
        '''
        Interface to add an artist to the music library
        :param artist_repository: The object holding the database connection.
        '''
        valid = False
        while valid is False:
            self.clear()
            artist_id = None
            artist_name = input('Artist name:\t')
            artist_genre= input('Artist genre:\t')
            if artist_name != '' and artist_genre != '':
                valid = True
                artist = Artist(artist_id, artist_name, artist_genre)
                artist_repository.create(artist)
                print(f"\nAdded '{artist_name} ({artist_genre})' to music library database\n")
                return None

    def add_album(self, album_repository) -> None:
        '''
        Interface to add an artist to the music library
        :param album_repository: The object holding the database connection.
        '''
        valid = False
        while valid is False:
            self.clear()
            album_id = None
            album_title = input('Album title:\t')
            album_release_year= input('Album release year:\t')
            album_artist_id= input('Album artist:\t')
            if album_title != '' and not isinstance(album_release_year, int) and not isinstance(album_artist_id, int):
                valid = True
                album = Album(album_id, album_title, album_release_year, album_artist_id)
                album_repository.create(album)
                print(f"\nAdded '{album_title} ({album_release_year})' to music library database\n")
                return None

    def run(self) -> None:
        '''
        Runs application
        '''
        artist_repository = ArtistRepository(self._connection)
        album_repository = AlbumRepository(self._connection)
        choice = ''
        while choice == '':
            self.clear()
            print('Welcome to the music library manager\n\n')
            print('What would you like to do?')
            print('\t1) List all albums')
            print('\t2) List all artists')
            print('\t3) Add an artist')
            print('\t4) Add an album')
            print('\n\tq) Quit')
            choice = input('\nChoose an option:\n\t')
            match choice:
                case '1':
                    self.print_albums(album_repository)
                    choice = self.continue_menu()
                case '2':
                    self.print_artists(artist_repository)
                    choice = self.continue_menu()
                case '3':
                    self.add_artist(artist_repository)
                    choice = self.continue_menu()
                case '4':
                    self.add_album(album_repository)
                    choice = self.continue_menu()
                case 'q':
                    sys.exit()
                case _:
                    choice = ''


if __name__ == '__main__':
    app = Application()
    app.run()
