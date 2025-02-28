from playwright.sync_api import expect


def test_get_albums_returns_html(page, test_web_address, db_connection) -> None:
    """When we call /albums with GET
    We see an HTML page of results.
    """
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    header_tag = page.locator("h1")
    expect(header_tag).to_have_text("Music Library App")
    subheader_tag = page.locator("h2")
    expect(subheader_tag).to_have_text("Albums")
    album_class = page.locator(".album")
    expect(album_class).to_have_count(12)


def test_get_albums_path_parameters_valid(
    page, test_web_address, db_connection
) -> None:
    """When we call /albums/1
    We are returned the album with the id of 1.
    """
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums/1")
    header_tag = page.locator("h1")
    expect(header_tag).to_have_text("Music Library App")
    subheader_tag = page.locator("h2")
    expect(subheader_tag).to_have_text("Album 1")
    album_title = page.locator("#album_title")
    expect(album_title).to_have_text("Title: Doolittle")
    album_title = page.locator("#album_release_year")
    expect(album_title).to_have_text("Release year: 1989")


def test_get_albums_path_parameters_invalid(
    page, test_web_address, db_connection
) -> None:
    """When we call /albums/100000000000
    The 404 page is returned.
    """
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums/1000000000")
    header_tag = page.locator("h1")
    expect(header_tag).to_have_text("Music Library App")
    subheader_tag = page.locator("h2")
    expect(subheader_tag).to_have_text("404 - File not found")


def test_get_artists_returns_html(page, test_web_address, db_connection) -> None:
    """When we call /artists with GET
    We see an HTML page of results.
    """
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    header_tag = page.locator("h1")
    expect(header_tag).to_have_text("Music Library App")
    subheader_tag = page.locator("h2")
    expect(subheader_tag).to_have_text("Artists")
    artist_class = page.locator(".artist")
    expect(artist_class).to_have_count(4)


def test_get_artists_path_parameters_valid(
    page, test_web_address, db_connection
) -> None:
    """When we call /artists/1
    We are returned the artist with the id of 1.
    """
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists/1")
    header_tag = page.locator("h1")
    expect(header_tag).to_have_text("Music Library App")
    subheader_tag = page.locator("#artist_id")
    expect(subheader_tag).to_have_text("Artist 1")
    artist_title = page.locator("#artist_name")
    expect(artist_title).to_have_text("Name: Pixies")
    artist_title = page.locator("#artist_genre")
    expect(artist_title).to_have_text("Genre: Rock")


def test_get_artists_path_parameters_invalid(
    page, test_web_address, db_connection
) -> None:
    """When we call /artists/100000000000
    The 404 page is returned.
    """
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists/1000000000")
    header_tag = page.locator("h1")
    expect(header_tag).to_have_text("Music Library App")
    subheader_tag = page.locator("h2")
    expect(subheader_tag).to_have_text("404 - File not found")

def test_add_album_path_parameters_valid(page, test_web_address, db_connection) -> None:
    """When we call /albums/new, return an html form."""
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums/new")
    header_tag = page.locator("h1")
    expect(header_tag).to_have_text("Music Library App")
    subheader_tag = page.locator("h2")
    expect(subheader_tag).to_have_text("Add album")
    input_form= page.locator("form")
    expect(input_form).to_have_id("add-new-album-form")


def test_add_invalid_album_returns_error(page, test_web_address, db_connection) -> None:
    """When an invalid album is submitted, app returns error"""
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums/new")
    page.fill("input[name=album-title]", " ")
    page.fill("input[name=album-release-year]", "1997")
    page.fill("input[name=album-artist-id]", "1")
    page.get_by_text("submit").click()
    expect(page.get_by_text("Whoops, there were some errors!")).to_be_visible()


def test_add_valid_album_returns_success(page, test_web_address, db_connection) -> None:
    """When a valid new album is submitted, it is added to the database"""
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums/new")
    page.fill("input[name=album-title]", "OK Computer")
    page.fill("input[name=album-release-year]", "1997")
    page.fill("input[name=album-artist-id]", "1")
    page.get_by_text("submit").click()
    subheader_tag = page.locator("h2")
    expect(subheader_tag).to_have_text("Album 13")
    album_title = page.locator("#album_title")
    expect(album_title).to_have_text("Title: OK Computer")
    album_title = page.locator("#album_release_year")
    expect(album_title).to_have_text("Release year: 1997")


def test_add_artist_path_parameters_valid(page, test_web_address, db_connection) -> None:
    """When we call /artists/new, return an html form."""
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists/new")
    header_tag = page.locator("h1")
    expect(header_tag).to_have_text("Music Library App")
    subheader_tag = page.locator("h2")
    expect(subheader_tag).to_have_text("Add artist")
    input_form= page.locator("form")
    expect(input_form).to_have_id("add-new-artist-form")


def test_add_invalid_artist_name_returns_error(page, test_web_address, db_connection) -> None:
    """When an invalid artist is submitted, app returns error."""
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists/new")
    page.fill("input[name=artist-name]", " ")
    page.fill("input[name=artist-genre]", "Alternative")
    page.get_by_text("submit").click()
    error_notification= page.locator("#errors")
    expect(error_notification).to_be_visible()


def test_add_invalid_artist_genre_returns_error(page, test_web_address, db_connection) -> None:
    """When an invalid artist is submitted, app returns error."""
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists/new")
    page.fill("input[name=artist-name]", "Jake")
    page.fill("input[name=artist-genre]", " ")
    page.get_by_text("submit").click()
    error_notification= page.locator("#errors")
    expect(error_notification).to_be_visible()


def test_add_valid_artist_returns_success(page, test_web_address, db_connection) -> None:
    """When a valid new artist is submitted, it is added to the database"""
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists/new")
    page.fill("input[name=artist-name]", "Jake")
    page.fill("input[name=artist-genre]", "Alternative")
    page.get_by_text("submit").click()
    subheader_tag = page.locator("#artist_id")
    expect(subheader_tag).to_have_text("Artist 5")
    artist_name= page.locator("#artist_name")
    expect(artist_name).to_have_text("Name: Jake")
    artist_genre= page.locator("#artist_genre")
    expect(artist_genre).to_have_text("Genre: Alternative")
