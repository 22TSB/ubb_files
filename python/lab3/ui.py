from user import add_user, delete_user, update_user
from movie import validate_date, add_movie, delete_movie, update_imdb_score, search_movies_by_actor, search_movies_by_rating
from watchlist import add_watchlist_entry, get_watched_movies_for_user
from repository import save_to_json, read_from_json, save_users, save_movies, save_watchlists

# print
def display_user_menu(): 
    print("\n--- User Management Menu ---")
    print("1. Add user")
    print("2. Delete user")
    print("3. Update user")
    print("4. Display all users")
    print("0. Back")

def display_movie_menu(): 
    print("\n--- Movie Management Menu ---")
    print("1. Add movie")
    print("2. Delete movie")
    print("3. Update IMDb rating")
    print("4. Display all movies")
    print("0. Back")

def display_watchlist_menu(): 
    print("\n--- Watch List Menu ---")
    print("1. Add watch list entry")
    print("2. Show watched movies for a user")
    print("3. Search movies by actor")
    print("4. Show movies above rating threshold")
    print("5. Display all watch lists")
    print("0. Back")

# menu
def user_menu(users, watchlists, user_path, watchlist_path):
    while True:
        display_user_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Enter name: ")

            try:
                age = int(input("Enter age: "))
                users = add_user(users, name, age)
                # save_to_json(users, user_path)
                save_users(users, user_path)
                print("User added successfully.")

            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            name = input("Enter name of user to delete: ")

            try:
                users, watchlists = delete_user(users, watchlists, name)
                # save_to_json(users, user_path)
                save_users(users, user_path)
                # save_to_json(watchlists, watchlist_path)
                save_watchlists(watchlists, watchlist_path)
                print("User deleted successfully")
                
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "3":
            name = input("Enter name of user to update:")
            new_name_str = input("Enter new name (leave blank to keep):").strip()
            new_age_str = input("Enter new age (leave blank to keep):").strip()
            new_name = None
            new_age = None

            if (new_name_str != ''):
                new_name = new_name_str

            if (new_age_str != ''):
                new_age = int(new_age_str)

            try:
                users, watchlists = update_user(users, watchlists, name, new_name, new_age)
                # save_to_json(users, user_path)
                save_users(users, user_path)
                # save_to_json(watchlists, watchlist_path)
                save_watchlists(watchlists, watchlist_path)
                print("User updated successfully")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "4":
            print("\nUsers List:")
            for user in users:
                print(f"- Name: {user["name"]}, Age: {user["age"]}")

        elif choice == "0":
            break
        else:
            print("Invalid option.")

def movie_menu(movies, path):
    while True:
        display_movie_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Enter movie name: ")
            release_date = input("Enter release date (yyyy-mm-dd): ")

            try:
                imdb_score = float(input("Enter imdb score (0.0 - 10.0): "))
                actors_input = input("Enter actors separated by comma ',': ")
                actors = [a.strip() for a in actors_input.split(",")]
                movies = add_movie(movies, name, release_date, imdb_score, actors)
                # save_to_json(movies, path)
                save_movies(movies, path)
                print("Movie added successfully.")

            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            name = input("Enter movie name to delete: ")
            
            try:
                movies = delete_movie(movies, name)
                # save_to_json(movies, path)
                save_movies(movies, path)
                print("Movie deleted successfully.")

            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "3":
            name = input("Enter movie name to update: ")

            try:
                new_score = float(input("Enter new IMDb score: "))
                movies = update_imdb_score(movies, name, new_score)
                # save_to_json(movies, path)
                save_movies(movies, path)
                print("IMDb score updated successfully.")

            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "4":
            print("\nMovies List:")
            for m in movies:
                print(f"- {m['name']} | Released: {m['release_date']} | IMDb: {m['imdb_score']} | Actors: {', '.join(m['actors'])}")

        elif choice == "0":
            break
        else:
            print("Invalid option.")

def watchlist_menu(users, movies, watchlists, path):
    while True:
        display_watchlist_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            user_name = input("Enter user name: ")
            movie_name = input("Enter movie name: ")
            try:
                watchlists = add_watchlist_entry(watchlists, users, movies, user_name, movie_name)
                # save_to_json(watchlists, path)
                save_watchlists(watchlists, path)
                print("Watch list entry added successfully.")

            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            user_name = input("Enter user name: ")
            watched = get_watched_movies_for_user(watchlists, movies, user_name)

            print(f"\nMovies watched by {user_name}:")
            for m in watched:
                print(f"- {m['name']} (IMDb: {m['imdb_score']})")

        elif choice == "3":
            actor = input("Enter actor name to search: ")
            found = search_movies_by_actor(movies, actor)

            print(f"\nMovies featuring {actor}:")
            for m in found:
                print(f"- {m['name']}")

        elif choice == "4":
            try:
                threshold = float(input("Enter rating threshold: "))
                found = search_movies_by_rating(movies, threshold)

                print(f"\nMovies with IMDb rating > {threshold}:")
                for m in found:
                    print(f"- {m['name']} ({m['imdb_score']})")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "5":
            print("\nAll Watch Lists:")
            for w in watchlists:
                print(f"- User: {w['user_name']} watched Movie: {w['movie_name']}")

        elif choice == "0":
            break
        else:
            print("Invalid option.")
