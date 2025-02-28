# 8. (1 point) Create a program that simulates how websites ensure that everyone has a unique
# username:
# • Make a list of five or more usernames called current_users.
# • Make another list of five usernames called new_users. Ensure that one or two of the new
# usernames are also in the current_users list.

# • Loop through the new_users list to check if each new username has already been used.
# – If a username has been used, print a message that the person will need to enter a new
# username.
# – If a username has not been used, print a message saying that the username is available.

# • Ensure that the comparison is case insensitive. If ’John’ has been used, ’JOHN’ should
# not be accepted. (To achieve this, create a copy of current_users containing the lowercase
# versions of all existing usernames.)


current_users = ["Ahmad Faraz", "Saqib Nisar",
                 "Muhammad Ali", "Arsalan Aslam", "Saad Israr"]
new_users = ["Ahmad Faraz", "Saad Israr",
             "Muhammad Ali", "Ali Raza", "Zakir Naik"]


for new_user in new_users:
    if new_user in current_users:
        print(f"{new_user} is not available. Please enter a new username.")
    else:
        print(f"{new_user} is available.")
