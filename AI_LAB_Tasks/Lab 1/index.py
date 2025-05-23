# Name: Lab 1
#  --- LIST COMPREHENSION ---
#  list comprehension is a concise way to create lists. It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.
# The expressions can be anything, meaning you can put in all kinds of objects in lists.


# a = int(input("Input : "))
# result = a+5
# print(result)

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9.56, 10]

for a in myList:  # 2,4,6,8 from 2 to 10 with step size 2
    print(myList.index(a), " : ", a)
