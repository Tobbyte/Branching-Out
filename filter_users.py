"""Module to read files"""
import json

def filter_users_by_name(name: str, users: list):
    """Filters by name"""
    filtered_users = [user for user in users
                      if user["name"].lower() == name.lower()]
    
    if not filtered_users:
        print("Name not found in users")
    else:
        for user in filtered_users:
            print(user)

def filter_users_by_age(age: int, users: list):
    """Filters by age"""
    filtered_users = [user for user in users
                      if user.get("age") == age]

    if not filtered_users:
        print("Age not found in users")
    else:
        for user in filtered_users:
            print(user)

def filter_users_by_email(email: str, users: list):
    """Filters by email"""
    filtered_users = [user for user in users
                      if user.get("email", "").lower() == email.lower()]

    if not filtered_users:
        print("Email not found in users")
    else:
        for user in filtered_users:
            print(user)

def check_if_dec(inp: str):
    """checks if input is decimal"""
    return inp.isdecimal()


def check_if_alpha(inp: str):
    """checks if input is alphabetical"""
    return inp.isalpha()

def check_if_email(inp: str):
    """checks if input contains '@' and '.' """
    return "@" in inp and "." in inp

def select_filter_by_input(users: list):
    """Asks for user input and calls filter fn"""
    prompt = "What would you like to filter by? ('name','age', 'email' supported): "
    filter_option = input(prompt).strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        if check_if_alpha((name_to_search)):
            filter_users_by_name(name_to_search, users)
        else:
            print("Valid input is [a-z]")

    elif filter_option == "age":
        age_to_search = input("Enter a age to filter users: ").strip()
        if check_if_dec((age_to_search)):
            filter_users_by_age(int(age_to_search), users)
        else:
            print("Valid input is [0-9]")

    elif filter_option == "email":
        email_to_search = input("Enter a email to filter users: ").strip()
        if check_if_email(email_to_search):
            filter_users_by_email(email_to_search, users)
        else:
            print("Email must contain '@‘ and ‘.‘")
    else:
        print("Filtering by that option is not yet supported.")
        select_filter_by_input(users)


def load_user_data() -> list[dict]:
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
