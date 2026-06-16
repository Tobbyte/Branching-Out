"""Module to read files"""
import json

def filter_users(search_by: str, search_value: str | int, users: list):
    """Filters users by a search_by key and search_value."""
    filtered_users = [user for user in users
        if str(user.get(search_by, "")).lower() == str(search_value).lower()
    ]

    if not filtered_users:
        print(f"No users found for {search_by}: {search_value}")
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
    ## TODO:
    # - refactor ifs on filter_option f.e. by using a config set
    #   that defines per keyword validation rules, and error message
    # - refactor to use while insead of recursive call
    prompt = "What would you like to filter by? ('name','age', 'email' supported): "
    filter_option = input(prompt).strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        if check_if_alpha((name_to_search)):
            filter_users(filter_option, name_to_search, users)
        else:
            print("Valid input is [a-z]")

    elif filter_option == "age":
        age_to_search = input("Enter a age to filter users: ").strip()
        if check_if_dec((age_to_search)):
            filter_users(filter_option, age_to_search, users)
        else:
            print("Valid input is [0-9]")

    elif filter_option == "email":
        email_to_search = input("Enter a email to filter users: ").strip()
        if check_if_email(email_to_search):
            filter_users(filter_option, email_to_search, users)
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
