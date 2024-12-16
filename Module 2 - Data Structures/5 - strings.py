# Strings are immutable by nature. Assignment is allowed, but it just changes the reference
# to another memory location. However, modifying a string at any specific index is not possible.

name = "Ahmad Faraz"
print("Id before assignment: ", id(name))  # Id of name: 1894708035376
name = "Nadar shah"
print("Id after assignment: ", id(name))  # Id after assignment: 2534080753264

# This is not possible
# name[0] = "Y"  # Error


# Forward indexing

# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])
# print(name[6])
# print(name[7])
# print(name[8])
# print(name[9])
# print(name[10])


# Backward indexing
# It starts with -1 and goes to the negative end-value.

# print('---------------------')
# print(name[-1])
# print(name[-2])
# print(name[-3])
# print(name[-4])
# print(name[-5])
# print(name[-6])
# print(name[-7])
# print(name[-8])
# print(name[-9])
# print(name[-10])
# print(name[-11])


name = "Michal Jackson"


# firstName = name[0:4]  # From index 0 to < 4
# lastName = name[7:11]  # From index 7 to < 11
# print(firstName)  # Mich
# print(lastName)  # Jack


# Slicing

# Picks every second character starting from the beginning
print(name[::2])  # Mca ako

# From index 0 to < 5 with a step of 2 (every second character)
print(name[0:5:2])  # mca


# String Length

strLength = len(name)
print(strLength)  # 14


# String Concatenation

name = name + " is a blockchain developer"
print(name)


# Replicate String

# Replicate string three times , string supports only + and *
name = 3 * " Ahmad Faraz "
print("Replicated name : ", name)  # Ahmad Faraz  Ahmad Faraz  Ahmad Faraz


name = "saqib khan"
# String Methods

print(name.upper())  # SAQIB KHAN
print(name.lower())  # saqib khan
print(name.capitalize())  # Saqib khan
print(name.find('A'))  # -1
print(name.find('a'))  # 1
print(name.replace('saqib', 'Ali'))  # Ali khan
