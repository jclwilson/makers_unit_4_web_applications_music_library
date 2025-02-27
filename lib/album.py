"""Module Album defines Album class."""

class Album:
    """Class: Album, representing albums table in database."""

    def __init__(self, id, title, release_year, artist_id) -> None:
        self.id: int = id
        self.title: str = title
        self.release_year: int = release_year
        self.artist_id: int = artist_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self) -> str:
        return f"Album({self.id}, {self.title}, {self.release_year}, {self.artist_id})"

    def is_valid(self) -> bool:
        """Check validity of submitted data."""
        if isinstance(self.title, str) \
                and len(self.title) > 0 \
                and isinstance(self.release_year, int) \
                and isinstance(self.artist_id, int):
            return True
        return False

    def generate_errors(self) -> list:
        """Return human-readable errors if data is invalid.""" 
        errors = []
        if self.title is None or self.title == "":
            errors.append("Album title cannot be blank")
        if self.release_year is None or isinstance(self.release_year, int) == False:
            errors.append("Release year must be a number")
        return errors
