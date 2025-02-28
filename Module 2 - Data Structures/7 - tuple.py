# Tuple is an order sequence (means index-wise)
# Tuples are expressed as comma-separated elements within round brackets.
# Tuples are immutable

tuple1 = (1, 2.2, 'disco')
print(type(tuple1))  # <class 'tuple'>
print(tuple1)  # (1, 2.2, 'disco')
print(tuple1[0])  # 1
print(tuple1[1])  # 2.2
print(tuple1[2])  # disco


# Concatination

tuple2 = tuple1+("Ahmad Faraz", 23)  # (1, 2.2, 'disco', 'Ahmad Faraz', 23)
print(tuple2)


# Tuple Slicing

print(tuple2[0:3])  # 0 to < 3 = (1, 2.2, 'disco')

# Length

print(len(tuple2))  # 5


# Nested Tuple


nestedTuple = (12, 34, ("Ahmad", "Faraz"), 3.4, (1, 2, (3, 4)))

print(nestedTuple[0])  # 12
print(nestedTuple[2][1][0])  # F
print(nestedTuple[4][2][0])  # 3
