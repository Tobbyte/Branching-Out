"""Module to read files"""
import json

def filter_users_by_name(name, users):
    """Filters by name"""
    filtered_users = [user for user in users
                      if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)

def filter_users_by_age(age, users):
    """Filters by age"""
    ## TODO: sanitize input
    filtered_users = [user for user in users
                      if user.get("age") == int(age)]

    for user in filtered_users:
        print(user)

def filter_users_by_email(email, users):
    """Filters by email"""
    filtered_users = [user for user in users
                      if user.get("email", "").lower() == email.lower()]

    for user in filtered_users:
        print(user)


def select_filter_by_input(users):
    """Asks for user input and calls filter fn"""
    prompt = "What would you like to filter by? ('name','age', 'email' supported): "
    filter_option = input(prompt).strip().lower()
    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search, users)
    elif filter_option == "age":
        age_to_search = input("Enter a age to filter users: ").strip()
        filter_users_by_age(age_to_search, users)
    elif filter_option == "email":
        email_to_search = input("Enter a email to filter users: ").strip()
        filter_users_by_email(email_to_search, users)
    else:
        print("Filtering by that option is not yet supported.")


def load_user_data():
    """Loads user data from file."""
    try:
        with open("users.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("ERROR: users.json file not found.")
        return []


if __name__ == "__main__":
    user_data = load_user_data() ## pass for now, until we have classes
    if user_data:
        select_filter_by_input(user_data)
