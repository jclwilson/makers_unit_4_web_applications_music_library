"""Constructs with id, title, release_year, and artist_id."""

from lib.album import Album


def test_constructs_with_fields() -> None:
    """Tests that Album objects are instantiated correctly."""
    album = Album(1, "Ok Computer", 1997, 2)
    assert album.id == 1
    assert album.title == "Ok Computer"
    assert album.release_year == 1997
    assert album.artist_id == 2


def test_equality() -> None:
    """Tests that Album objects with the same attributes are equal to other album objects."""
    album_1 = Album(1, "Ok Computer", 1997, 2)
    album_2 = Album(1, "Ok Computer", 1997, 2)
    assert album_1 == album_2


def test_formatting() -> None:
    """Tests that the string output of the object is formatted nicely :)."""
    album_1 = Album(1, "Ok Computer", 1997, 2)
    assert str(album_1) == "Album(1, Ok Computer, 1997, 2)"


def test_validation_valid_data() -> None:
    """Test valid data returns true.

    When data is submitted via the HTML form, ensure that valid data is accepted
    """
    album = Album(13, "OK Computer", 1997, 5)
    assert album.is_valid() is True


def test_validation_invalid_data() -> None:
    """Test invalid data returns false.

    When data is submitted via the HTML form, ensure that invalid data is rejected.
    """
    album_invalid_title = Album(13, "", 1997, 5)
    assert album_invalid_title.is_valid() is False

def test_album_generates_errors() -> None:
    """Test invalid data generates errors."""
    album_invalid_title = Album(13, "", 1997, 5)
    assert album_invalid_title.is_valid() is False
    assert album_invalid_title.generate_errors() == ["Album title cannot be blank"]
