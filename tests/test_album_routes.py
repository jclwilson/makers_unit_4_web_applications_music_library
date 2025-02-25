'''
Test file for album routes
'''

def test_get_albums_from_database(web_client, db_connection) -> None:
    '''
    Tests that when we call GET on /albums endpoint then all albums are returned
    '''
    db_connection.seed('seeds/music_library.sql')
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode("utf-8") == '''["Doolittle (1989)","Surfer Rosa (1988)","Waterloo (1974)","Super Trouper (1980)","Bossanova (1990)","Lover (2019)","Folklore (2020)","I Put a Spell on You (1965)","Baltimore (1978)","Here Comes the Sun (1971)","Fodder on My Wings (1982)","Ring Ring (1973)"]\n'''

def test_post_albums_from_database(web_client, db_connection) -> None:
    '''
    Test that we recieve a 400 BAD REQUEST on POST requests.
    '''
    db_connection.seed('seeds/music_library.sql')
    response = web_client.post('/albums')
    assert response.status_code == 400

def test_album_is_added_to_database(web_client, db_connection) -> None:
    '''
    Test that when we call POST on the albums endpoint, the information is added to the database.
    '''
    pass
