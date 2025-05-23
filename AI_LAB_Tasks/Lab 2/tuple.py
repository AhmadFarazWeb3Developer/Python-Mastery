
# Tuples are immutable

fruits = ("Apple", "Orange", "Cherry", "Guvava")
# fruits.append("Banana") cannot be changed

print(fruits)

for fruit in fruits:
    if (fruit == "Orange"):
        print("Yes")
    else:
        print("No")
