from lib.artist import Artist

"""
Artist constructs with an id, name and genre
"""


def test_artist_constructs() -> None:
    artist = Artist(1, "Test Artist", "Test Genre")
    assert artist.id == 1
    assert artist.name == "Test Artist"
    assert artist.genre == "Test Genre"


"""
We can format artists to strings nicely
"""


def test_artists_format_nicely() -> None:
    artist = Artist(1, "Test Artist", "Test Genre")
    assert str(artist) == "Artist(1, Test Artist, Test Genre)"
    # Try commenting out the `__repr__` method in lib/artist.py
    # And see what happens when you run this test again.


"""
We can compare two identical artists
And have them be equal
"""


def test_artists_are_equal() -> None:
    artist1 = Artist(1, "Test Artist", "Test Genre")
    artist2 = Artist(1, "Test Artist", "Test Genre")
    assert artist1 == artist2
    # Try commenting out the `__eq__` method in lib/artist.py
    # And see what happens when you run this test again.


def test_validation_valid_data() -> None:
    """Test valid data returns true.

    When data is submitted via the HTML form, ensure that valid data is accepted
    """
    artist = Artist(5, "Jake", "Alternative")
    assert artist.is_valid() is True


def test_validation_invalid_data_no_genre() -> None:
    """Test invalid data returns false.

    When data is submitted via the HTML form, ensure that invalid data is rejected.
    """
    artist = Artist(5, "Jake", "")
    assert artist.is_valid() is False

def test_validation_invalid_data_no_name() -> None:
    """Test invalid data returns false.

    When data is submitted via the HTML form, ensure that invalid data is rejected.
    """
    artist = Artist(5, "", "Alternative")
    assert artist.is_valid() is False

def test_artist_generates_errors() -> None:
    """Test invalid data generates errors."""
    artist_invalid_name = Artist(5, "", "Alternative")
    assert artist_invalid_name.is_valid() is False
    assert artist_invalid_name.generate_errors() == ["Artist name cannot be blank"]
