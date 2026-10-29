# tests.py
import os

from user import add_user, delete_user, update_user
from movie import validate_date, add_movie, delete_movie, update_imdb_score, search_movies_by_actor, search_movies_by_rating
from watchlist import add_watchlist_entry, get_watched_movies_for_user

from repository import read_from_json, save_to_json, read_users, save_users, read_movies, save_movies, read_watchlists, save_watchlists

def test_user_logic():
    users = [{"name": "Alice", "age": 30}]
    movies = [{"name": "Matrix", "release_date": "1999-03-31", "imdb_score": 8.7, "actors": ["Keanu Reeves"]}]
    watchlists = [{"user_name": "Alice", "movie_name": "Matrix"}]
    
    # 1. watchlist update
    users, watchlists = update_user(users, watchlists, "Alice", new_name="Alicia", new_age=31)
    assert users[0]["name"] == "Alicia"
    assert users[0]["age"] == 31
    assert watchlists[0]["user_name"] == "Alicia"
    
    # 2. watchlist delete
    users, watchlists = delete_user(users, watchlists, "Alicia")
    assert len(users) == 0
    assert len(watchlists) == 0

def test_movie_logic():
    assert validate_date("2026-10-29") == True
    assert validate_date("29-10-2026") == False
    
    movies = []
    movies = add_movie(movies, "Inception", "2010-07-16", 8.8, ["Leonardo DiCaprio", "Elliot Page"])
    assert len(movies) == 1
    
    movies = update_imdb_score(movies, "Inception", 9.0)
    assert movies[0]["imdb_score"] == 9.0
    
    found_actor = search_movies_by_actor(movies, "Leonardo")
    assert len(found_actor) == 1
    
    found_rating = search_movies_by_rating(movies, 8.5)
    assert len(found_rating) == 1
    
    movies = delete_movie(movies, "Inception")
    assert len(movies) == 0

def test_watchlist_logic():
    users = [{"name": "Bob", "age": 30}]
    movies = [{"name": "Matrix", "release_date": "1999-03-31", "imdb_score": 8.7, "actors": ["Keanu Reeves"]}]
    watchlists = []
    
    watchlists = add_watchlist_entry(watchlists, users, movies, "Bob", "Matrix")
    assert len(watchlists) == 1
    
    watched = get_watched_movies_for_user(watchlists, movies, "Bob")
    assert len(watched) == 1
    assert watched[0]["name"] == "Matrix"

def test_save_and_read_json():
    items = ["milk", "bread", "eggs"]
    save_to_json(items, "test_shopping.json")
    assert read_from_json("test_shopping.json") == items
    os.remove("test_shopping.json")

def test_save_and_read_text():
    # users
    path = "test_users_repo.txt"
    users = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]
    
    # Test saving and reading
    save_users(users, path)
    loaded_users = read_users(path)
    
    assert len(loaded_users) == 2
    assert loaded_users[0]["name"] == "Alice"
    assert loaded_users[0]["age"] == 25
    assert loaded_users[1]["name"] == "Bob"
    assert loaded_users[1]["age"] == 30
    
    # Cleanup
    if os.path.exists(path):
        os.remove(path)

    # movies
    path = "test_movies_repo.txt"
    movies = [
        {
            "name": "Inception",
            "release_date": "2010-07-16",
            "imdb_score": 8.8,
            "actors": ["Leonardo DiCaprio", "Elliot Page"]
        }
    ]
    
    # Test saving and reading
    save_movies(movies, path)
    loaded_movies = read_movies(path)
    
    assert len(loaded_movies) == 1
    assert loaded_movies[0]["name"] == "Inception"
    assert loaded_movies[0]["release_date"] == "2010-07-16"
    assert loaded_movies[0]["imdb_score"] == 8.8
    assert loaded_movies[0]["actors"] == ["Leonardo DiCaprio", "Elliot Page"]
    
    # Cleanup
    if os.path.exists(path):
        os.remove(path)

    # watchlists
    path = "test_watchlists_repo.txt"
    watchlists = [
        {"user_name": "Alice", "movie_name": "Inception"}
    ]
    
    # Test saving and reading
    save_watchlists(watchlists, path)
    loaded_watchlists = read_watchlists(path)
    
    assert len(loaded_watchlists) == 1
    assert loaded_watchlists[0]["user_name"] == "Alice"
    assert loaded_watchlists[0]["movie_name"] == "Inception"
    
    # Cleanup
    if os.path.exists(path):
        os.remove(path)

def run_all_tests():
    test_user_logic()
    test_movie_logic()
    test_watchlist_logic()
    test_save_and_read_json()
    test_save_and_read_text()
    print("All tests passed successfully! ✅")

if __name__ == "__main__":
    run_all_tests()
