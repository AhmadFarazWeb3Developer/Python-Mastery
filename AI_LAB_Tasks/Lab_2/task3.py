# 3. (1 point) Write a Python program that asks the user to enter four of their favorite foods and
# store them in a dictionary so that they are indexed with numbers starting from 1. Display the
# dictionary in full, showing the index number and the item. Ask them which they want to get rid
# of and remove it from the list. Sort the remaining data and display the dictionary.


favorite_foods_dict = {}

for i in range(1, 5):
    food = input(f"Enter your favorite food {i}: ")
    favorite_foods_dict[i] = food


print("\nYour favorite foods:")

for index, food in favorite_foods_dict.items():
    print(f"{index}: {food}")

# Ask the user which food to remove
remove_index = int(
    input("\nEnter the index number of the food you want to remove: "))


if remove_index in favorite_foods_dict:
    del favorite_foods_dict[remove_index]
else:
    print("Invalid index number!")

# Sort the remaining food items
sorted_foods = sorted(favorite_foods_dict.values())

# Reconstruct the dictionary with new indices
favorite_foods_dict = {index: value for index,
                       value in enumerate(sorted_foods, 1)}

# # Display the updated dictionary
# print("\nUpdated favorite foods:")
for index, food in favorite_foods_dict.items():
    print(f"{index}: {food}")
