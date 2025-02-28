# 2. (1 point) Write a Python program to enter a list of ten colors. Ask the user for a starting number
# between 0 and 4 and an end number between 5 and 9. Display the list for those colors between
# the start and end numbers the user input.


colors = ["red", "green", "blue", "white",
          "yellow", "orange", "gray", "black", "cyan", "pink"]

num1 = int(input("Enter number betwen 0 to 4 :"))
num2 = int(input("Enter number betwen 5 to 9 :"))
newColors = colors[num1:num2]
print(newColors)

