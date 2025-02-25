import pytest
from playwright.sync_api import Page, expect

def test_get_albums_returns_html(page, test_web_address, db_connection) -> None:
    '''
    When we call /albums with GET
    We see an HTML page of results
    '''
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/albums")
    header_tag = page.locator("h1")
    expect(header_tag).to_have_text("Music Library App")
    subheader_tag = page.locator("h2")
    expect(subheader_tag).to_have_text("Albums")
    album_class = page.locator(".album")
    expect(album_class).to_have_count(12)
