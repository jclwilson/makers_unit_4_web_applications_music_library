"""Module Album defines Album class."""

class Album:
    """Class: Album, representing albums table in database."""

    def __init__(self, id, title, release_year, artist_id) -> None:
        self.id: int | None = id
        self.title: str = title
        self.release_year: int = int(release_year)
        self.artist_id: int = int(artist_id)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self) -> str:
        return f"Album({self.id}, {self.title}, {self.release_year}, {self.artist_id})"

    def is_valid(self) -> bool:
        """Check validity of submitted data."""
        title = self.title.strip()
        if isinstance(title, str) \
                and len(title) > 0 \
                and isinstance(self.release_year, int):
            return True
        return False

    def generate_errors(self) -> list:
        """Return human-readable errors if data is invalid.""" 
        errors = []
        title = self.title.strip()
        if isinstance(self.id, int) is False:
            errors.append("ID must be a number within range")
        if title is None or title == "":
            errors.append("Album title cannot be blank")
        if self.release_year is None or isinstance(self.release_year, int) is False:
            errors.append("Release year must be a number")
        if isinstance(self.artist_id, int) is False:
            errors.append("Artist ID must be a number")
        return errors
