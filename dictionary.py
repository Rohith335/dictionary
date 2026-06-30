# Create a Python program that initializes an empty dictionary to store user profiles, with keys representing user IDs and values representing user names.
dictionary = {}


# Implement a function to add a new user profile to the dictionary, taking user ID and name as input parameters.
def add_user(user_id, name):
    dictionary[user_id] = name


# Implement a function to retrieve a user's name by their ID, handling cases where the ID is not found in the dictionary.
def get_user_name(user_id):
    return dictionary.get(user_id, "User not found")


# Implement a function to update an existing user's name, given their ID and new name.
def update_user_name(user_id, new_name):
    if user_id in dictionary:
        dictionary[user_id] = new_name
    else:
        print("User not found")


# Implement a function to remove a user profile by their ID, handling cases where the ID is not found in the dictionary.
def remove_user(user_id):
    if user_id in dictionary:
        del dictionary[user_id]
    else:
        print("User not found") 
# Test each function with sample data to demonstrate their correctness, printing the resulting dictionary after each operation.
# Test adding users
add_user(1, "Alice")        
add_user(2, "Bob")
print(dictionary)  # Output: {1: 'Alice', 2: 'Bob'} 


