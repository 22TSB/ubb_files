from datetime import datetime

def validate_date(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def add_movie(movies, name, release_date, imdb_score, actors):
    # check for errors
    if not name.strip():
        raise ValueError("Movie name cannot be empty.")
    if not validate_date(release_date):
        raise ValueError("Invalid release date format. Use YYYY-MM-DD.")
    if not (0.0 <= imdb_score <= 10.0):
        raise ValueError("IMDb score must be between 0.0 and 10.0.")
    for movie in movies:
        if movie["name"].lower() == name.lower():
            raise ValueError("Movie already exists.")

    movies.append({
        "name": name,
        "release_date": release_date,
        "imdb_score": imdb_score,
        "actors": [actor.strip() for actor in actors if actor.strip()]
    })
    return movies

def delete_movie(movies, name):
    initial_length = len(movies)

    movies[:] = [movie for movie in movies if movie["name"].lower() != name.lower()]

    if len(movies) == initial_length:
        raise ValueError("Movie not found.")
    return movies

def update_imdb_score(movies, name, new_score):
    if not (0.0 <= new_score <= 10.0):
        raise ValueError("IMDb score must be between 0.0 and 10.0.")

    found = False
    for movie in movies:
        if movie["name"].lower() == name.lower():
            found = True
            movie["imdb_score"] = new_score

    if not found:
        raise ValueError("Movie not found.")
    return movies

def search_movies_by_actor(movies, actor_name):
    actor_lower = actor_name.lower()
    return [movie for movie in movies if any(actor_lower in a.lower() for a in movie["actors"])]

def search_movies_by_rating(movies, threshold):
    return [movie for movie in movies if movie["imdb_score"] > threshold]
