import json

# JSON handlers
def read_from_json(path):
    with open(path, 'r') as file:
        return json.load(file)

def save_to_json(data, path):
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)

# Text handlers
def read_users(path):
    users = []
    try:
        with open(path, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(',')
                if len(parts) >= 2:
                    name = parts[0].strip()
                    try:
                        age = int(parts[1].strip())
                        users.append({"name": name, "age": age})
                    except ValueError:
                        continue
    except FileNotFoundError:
        pass
    return users

def save_users(users, path):
    with open(path, 'w') as file:
        for user in users:
            file.write(f"{user['name']},{user['age']}\n")

def read_movies(path):
    movies = []
    try:
        with open(path, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split('|')
                if len(parts) >= 4:
                    name = parts[0].strip()
                    release_date = parts[1].strip()
                    try:
                        imdb_score = float(parts[2].strip())
                    except ValueError:
                        imdb_score = 0.0
                    actors = [a.strip() for a in parts[3].split(',') if a.strip()]
                    movies.append({
                        "name": name,
                        "release_date": release_date,
                        "imdb_score": imdb_score,
                        "actors": actors
                    })
    except FileNotFoundError:
        pass
    return movies

def save_movies(movies, path):
    with open(path, 'w') as file:
        for movie in movies:
            actors_str = ','.join(movie['actors'])
            file.write(f"{movie['name']}|{movie['release_date']}|{movie['imdb_score']}|{actors_str}\n")

def read_watchlists(path):
    watchlists = []
    try:
        with open(path, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split('|')
                if len(parts) >= 2:
                    user_name = parts[0].strip()
                    movie_name = parts[1].strip()
                    watchlists.append({
                        "user_name": user_name,
                        "movie_name": movie_name
                    })
    except FileNotFoundError:
        pass
    return watchlists

def save_watchlists(watchlists, path):
    with open(path, 'w') as file:
        for entry in watchlists:
            file.write(f"{entry['user_name']}|{entry['movie_name']}\n")
