# 9. (1 point) Create a program that processes sandwich orders:
# • Make a list called sandwich_orders and fill it with the names of various sandwiches.
# • Create an empty list called finished_sandwiches.
# • Loop through the list of sandwich orders using while loop and print a message for each
# order, such as: I made your tuna sandwich.
# • As each sandwich is made, move it to the list of finished_sandwiches.
# • After all the sandwiches have been made, print a message listing each sandwich that was
# made.

sandwich_orders = ["Chicken Sandwich", "Beef Sandwich",
                   "Fish Sandwich", "Veggie Sandwich", "Tuna Sandwich"]
finished_sandwiches = []


print("\nSandwich Orders are Processing ....\n")
for sandwich in sandwich_orders:
    print(f"I made your {sandwich}.")
    finished_sandwiches.append(sandwich)

print("\n\nSandwich Orders are Ready ....\n")
for sandwich in finished_sandwiches:
    print(f"{sandwich} is ready.")
