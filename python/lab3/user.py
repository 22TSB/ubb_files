from repository import save_to_json

def add_user(users, name, age):
    # check for errors
    if not name.strip():
        raise ValueError("user name cannot be empty")

    if age < 0 or age > 150:
        raise ValueError("invalid age")

    # check for dupes
    for user in users:
        if (user["name"].lower() == name.lower() and user["age"] == age):
            raise ValueError("user already exists")

    users.append({"name": name, "age": age,})
    return users

def delete_user(users, watchlists, name):
    initital_length = len(users) 

    # filter dupes
    users[:] = [user for user in users if user["name"].lower() != name.lower()]

    if len(users) == initital_length: 
        raise ValueError("user not found")

    watchlists[:] = [w for w in watchlists if w["user_name"].lower() != name.lower()]

    return users, watchlists

def update_user(users, watchlists, name, new_name=None, new_age=None):
    found = False

    for user in users:
        if user["name"].lower() == name.lower():
            found = True

            old_name = user["name"]

            if new_name and new_name.strip():
                user["name"] = new_name

            if new_age is not None:
                if new_age < 0 or new_age > 150:
                    raise ValueError("invalid age")
                user["age"] = new_age

            if new_name and new_name.strip() and new_name.strip().lower() != old_name.lower():
                    for entry in watchlists:
                        if entry["user_name"].lower() == old_name.lower():
                            entry["user_name"] = user["name"]

    if not found:
        raise ValueError("user not found")

    return users, watchlists
