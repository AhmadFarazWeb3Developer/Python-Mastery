# 4. (1 point) Make a dictionary containing three major rivers and the country each river runs th-
# rough. One key-value pair might be ’nile’: ’egypt’.

# 1. Use a loop to print a sentence about each river, such as “The Nile runs through Egypt.”
# 2. Use a loop to print the name of each river included in the dictionary.
# 3. Use a loop to print the name of each country included in the dictionary.

rivers = {
    "Nile": "Egypt",
    "Indus": "Pakistan",
    "Yellow": "China"
}


print("\n------------------\n")
for river, country in rivers.items():
    print(f"{river} runs through {country}")
print("\n--------River Names----------\n")
for river in rivers.items():
    print(f"{river[0]}")
print("\n--------Country Names----------\n")
for country in rivers.items():
    print(f"{country[1]}")
