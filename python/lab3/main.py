from ui import user_menu, movie_menu, watchlist_menu
from repository import save_to_json, read_from_json, read_users, save_users, read_movies, save_movies, read_watchlists, save_watchlists

def main():
    # users_path = "./data/users.json"
    # movies_path = "./data/movies.json"
    # watchlists_path = "./data/watchlists.json"
    users_path = "./data/users.txt"
    movies_path = "./data/movies.txt"
    watchlists_path = "./data/watchlists.txt"

    while True:
        print("\n=== Movie Tracking Console Application ===")
        print("1. User Management")
        print("2. Movie Management")
        print("3. Watch List Management")
        print("0. Exit")
        choice = input("Choose an option: ").strip()
        
        # if (choice == "1"):
        #     users = read_from_json(users_path)
        #     watchlists = read_watchlists(watchlists_path)
        #     user_menu(users, watchlists, users_path)
        # elif (choice == "2"):
        #     movies = read_from_json(movies_path)
        #     movie_menu(movies, movies_path)
        # elif (choice == "3"):
        #     users = read_from_json(users_path)
        #     movies = read_from_json(movies_path)
        #     watchlists = read_from_json(watchlists_path)
        #     watchlist_menu(users, movies, watchlists, watchlists_path)
        if (choice == "1"):
            users = read_users(users_path)
            watchlists = read_watchlists(watchlists_path)
            user_menu(users, watchlists, users_path, watchlists_path)
        elif (choice == "2"):
            movies = read_movies(movies_path)
            movie_menu(movies, movies_path)
        elif (choice == "3"):
            users = read_users(users_path)
            movies = read_movies(movies_path)
            watchlists = read_watchlists(watchlists_path)
            watchlist_menu(users, movies, watchlists, watchlists_path)
        elif (choice == "0"):
            print("Exiting application. Goodbye!")
            break
        else: 
            print("Invalid option")

if __name__ == "__main__":
    main()
