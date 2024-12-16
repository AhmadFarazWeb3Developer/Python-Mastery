# List is an order sequence (means index-wise)
# List are expressed as comma-separated elements within Sqaure brackets.
# Lists are mutable


list1 = [1, 2.2, 'disco']

print(type(list1))  # < class 'list' >
print(list1)  # [1, 2.2, 'disco']

# List Slicing
print(list1[0:2])  # [1, 2.2]


# Mutating List

list1.extend(['party', 'enjoy'])
print(list1)  # [1, 2.2, 'disco', 'ma', 'tum']
list1.append(['eat', 'talk'])
print(list1)  # [1, 2.2, 'disco', 'ma', 'tum', ['ma', 'tum']]
list1.append('laugh')
print(list1)  # [1, 2.2, 'disco', 'ma', 'tum', ['ma', 'tum'], 'A']
list1[0] = "night"
list1[1] = "dinner"
print(list1)

del (list1[2])
print(list1)  # ['night', 'dinner', 'party', 'enjoy', ['eat', 'talk'], 'laugh']

# Concatination
list2 = list1+["Ahmad Faraz", 23]  # [1, 2.2, 'disco', 'Ahmad Faraz', 23]
print(list2)


# Spliting a string and converting to list
# We can use the split function to separate strings on a specific character, known as a delimiter.
print('Ahmad Faraz'.split())
print('A,h,m,a,d F,a,r,a,z'.split(','))  # ['A,h,m,a,d', 'F,a,r,a,z']


# Clone list

list3 = [1, 2, 3, 4, 5, 6, 7, 8]
list4 = list3[:]

print(list4)  # [1, 2, 3, 4, 5, 6, 7, 8]
