
'''
Test file for album repository
'''
from lib.album_repository import AlbumRepository
from lib.album import Album

def test_get_all_albums_from_database(db_connection):
    '''
    When we call #all, we get all the albums in the database as instances.
    '''
    db_connection.seed('seeds/music_library.sql')
    repo = AlbumRepository(db_connection)
    result = repo.all()
    assert result == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2)
    ]

def test_find_single_album_by_id(db_connection):
    '''
    When we call #find, we get a signle album instance returned to us.
    '''
    db_connection.seed('seeds/music_library.sql')
    repo = AlbumRepository(db_connection)
    result = repo.find(1)
    assert result == [Album(1, 'Doolittle', 1989, 1)]


def test_add_one_album_to_database(db_connection):
    '''
    When I add an album to the library
    It is added to the database.
    '''
    db_connection.seed('seeds/music_library.sql')
    repo = AlbumRepository(db_connection)
    album = Album(13, 'OK Computer', 1997, 5)
    repo.create(album)
    added_album = repo.find(13)
    assert added_album[0] == album

def test_add_multiple_albums_to_database(db_connection):
    '''
    When I add multiple albums to the library
    They are added to the database
    '''
    db_connection.seed('seeds/music_library.sql')
    repo = AlbumRepository(db_connection)
    album_1 = Album(13, 'OK Computer', 1997, 5)
    album_2 = Album(14, 'National Anthem', 2000, 5)
    repo.create(album_1)
    repo.create(album_2)
    added_album_1 = repo.find(13)
    added_album_2 = repo.find(14)
    assert added_album_1[0] == album_1
    assert added_album_2[0] == album_2

def test_delete_album_in_database(db_connection):
    '''
    When an album is deleted from the library
    It is deleted from the database
    '''
    db_connection.seed('seeds/music_library.sql')
    repo = AlbumRepository(db_connection)
    album = Album(13, 'OK Computer', 1997, 5)
    repo.create(album)
    found_album_1 = repo.find(13)
    assert found_album_1[0] == album
    repo.delete(13)
    found_album_2 = repo.find(13)
    assert found_album_2 == []
