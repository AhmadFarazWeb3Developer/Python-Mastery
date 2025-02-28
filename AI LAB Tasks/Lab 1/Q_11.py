# 11. Write a program to print the output of a given number from last to first.
# • Take input from users in integer form.
# • Ensure that the input number is greater than zero.
# • Divide the number and print its result in integer form only.

number = int(input("Enter a number: "))

if number > 0:
    while number > 0:
        print(number % 10, end=" ")
        number = number // 10  # round down to the nearest whole number

else:
    print("Please enter a number greater than zero")
