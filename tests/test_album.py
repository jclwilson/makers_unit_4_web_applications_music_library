'''
Constructs with id, title, release_year, and artist_id
'''
from lib.album import Album

def test_constructs_with_fields():
    '''
    Tests that Album objects are instantiated correctly.
    '''
    album = Album(1, 'Ok Computer', 1997, 2)
    assert album.id == 1
    assert album.title == 'Ok Computer'
    assert album.release_year == 1997
    assert album.artist_id == 2

def test_equality():
    '''
    Tests that Album objects with the same attributes are equal to other album objects.
    '''
    album_1 = Album(1, 'Ok Computer', 1997, 2)
    album_2 = Album(1, 'Ok Computer', 1997, 2)
    assert album_1 == album_2

def test_formatting():
    '''
    Tests that the string output of the object is formatted nicely :)
    '''
    album_1 = Album(1, 'Ok Computer', 1997, 2)
    assert str(album_1) == "Album(1, Ok Computer, 1997, 2)"
