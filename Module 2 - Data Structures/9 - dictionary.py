# Dictionaries are the collection of keys values pairs
# Keys are immutable and unique elements within curley brackets seperated by colon.
# The values are immutable, mutable and duplicates


dict1 = {"name": "Ahmad Faraz", "age": 23,
         'subjects': ["CS, SE, FSD,AI,ML,BC"]}

print(dict1["name"])
print(dict1["age"])
print(dict1["subjects"])


print(dict1.keys())  # dict_keys(['name', 'age', 'subjects'])
print(dict1.values())
# dict_values(['Ahmad Faraz', 23, ['CS, SE, FSD,AI,ML,BC']])


# Updation
dict1["graduation"] = 2026
print(dict1)

# Deletion
del (dict1["subjects"])
print(dict1)
