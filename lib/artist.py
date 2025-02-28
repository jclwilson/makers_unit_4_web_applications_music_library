class Artist:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, name, genre) -> None:
        self.id = id
        self.name = name
        self.genre = genre


    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self) -> str:
        return f"Artist({self.id}, {self.name}, {self.genre})"


    def is_valid(self) -> bool:
        """Check validity of submitted data."""
        name = self.name.strip()
        genre = self.genre.strip()
        if isinstance(name, str) \
                and len(name) > 0 \
                and isinstance(genre, str) \
                and len(genre) > 0:
            return True
        return False

    def generate_errors(self) -> list:
        """Return human-readable errors if data is invalid.""" 
        errors = []
        name = self.name.strip()
        genre = self.genre.strip()
        if isinstance(self.id, int) is False:
            errors.append("ID must be a number within range")
        if not isinstance(name, str) or len(name) == 0:
            errors.append("Artist name cannot be blank")
        if not isinstance(genre, str) or len(genre) == 0:
            errors.append("Artist genre cannot be blank")
        return errors
