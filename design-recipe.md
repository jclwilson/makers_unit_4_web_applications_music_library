# Music library web app

## 1. Extract nouns from the user stories or specification

```
As a user
I want a web application
That can add albums to my music library

As a user
I want to list album titles, release years, and artist ids
```

## Music Library Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

### 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# Request:
POST /albums

# With body parameters:
title=Voyage
release_year=2022
artist_id=2

# Expected response (200 OK)
(No content)

```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# EXAMPLE

# POST /albums
#  Parameters:
#    title: National Anthem
#    release_year: 2000 
#    artist_id: 5
#  Expected response (200 OK):

# GET /albums
#  Parameters: none
#  Expected response (405 Method not allowed):
"""
"""
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
'''
POST /albums
- title: test title
- release_year: 2025
- artist_id: 19
'''
def test_post_albums(web_client):
    response = web_client.post('/albums', data={'title':'test title', 'release_year':2000, 'artist_id':19})
    assert response.status_code == 200
```
