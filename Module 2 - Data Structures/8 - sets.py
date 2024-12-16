# sets are an onordered collection of elements
# List are expressed as comma-separated elements within curley brackets.
# Duplicate items are ignored in set


set1 = {1, 2, 3, 4, 4, 5, 6}
print(set1)  # {1, 2, 3, 4, 5, 6}

set1.add('Nadar shah')
print(set1)  # {1, 2, 3, 4, 5, 6, 'Nadar shah'}

set1.remove(1)
print(set1)  # {2, 3, 4, 5, 6, 'Nadar shah'}

print("Nadar shah" in set1)  # True


# Intersection of Sets using '&' , which retuns the elements which are present in both of the sets.


A = {10, 20, 30, 40, 50, 60}
B = {70, 80, 90, 100, 70, 10}
C = A & B
print(C)  # {'apple'}


x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

result = x & y & z  # {'c'}

print(result)


# Union of sets using union

A = {10, 20, 30, 40, 50, 60}
B = {70, 80, 90, 100, 70, 10}
z = {"f", "g", "c"}

C = A | B | z
print(C)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)  # {'apple', 'banana', 'cherry', 'microsoft', 'google'}

print(z)
