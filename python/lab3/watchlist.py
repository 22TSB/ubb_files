def add_watchlist_entry(watchlists, users, movies, user_name, movie_name):
    user_exists = any(u["name"].lower() == user_name.lower() for u in users)
    movie_exists = any(m["name"].lower() == movie_name.lower() for m in movies)

    # check for errors
    if not user_exists:
        raise ValueError("User does not exist.")
    if not movie_exists:
        raise ValueError("Movie does not exist.")

    for entry in watchlists:
        if entry["user_name"].lower() == user_name.lower() and entry["movie_name"].lower() == movie_name.lower():
            raise ValueError("Watchlist entry already exists.")

    watchlists.append({"user_name": user_name, "movie_name": movie_name})
    return watchlists

def get_watched_movies_for_user(watchlists, movies, user_name):
    watched_movie_names = [e["movie_name"] for e in watchlists if e["user_name"].lower() == user_name.lower()]

    return [m for m in movies if m["name"] in watched_movie_names]
