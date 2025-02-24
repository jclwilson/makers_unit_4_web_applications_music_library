# Music Library Database Integration App

## 3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name.

```python
# Table name: albums

# Model class
# (in lib/album.py)
class Album:
    

# Repository class
# (in lib/album_repository.py)
class AlbumRepository:

```

## 4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python
class Album:
    def __init__(self, id, title, release_year, artist_id):
        self._id = id
        self._title = title
        self._release_year = release_year
        self._artist_id = artist_id

    def __eq__(self):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f'Album(self, {self._id}, {self._title}, {self._release_year}, {self._artist_id})
    
```

## 5. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

```python
# Table name: albums

# Repository class
# (in lib/album_repository.py)

class AlbumRepository():

    def __init__(self):
        pass

    def all(self):
        '''
        Selects all records
        Parameters: None
        Returns: List of dictionaries
        SELECT id, name, cohort_name FROM students;
        Side effects: None
        '''

```

## 6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

```python
# Get all albums

repo = AlbumRepository()

albums = repo.all()

len(albums) # =>  13

albums[0].id # =>  1
albums[0].title# =>  'David'
albums[0].release_year # =>  ''
albums[0].artist_id => 1

```
