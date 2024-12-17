import pandas as pd


# Working with CSV (comma-seperated values) file


import pandas as pd

# List of dictionaries
data = [
    {"ID": 1, "Name": "John Doe", "Age": 28, "Country": "USA",
        "Salary": 50000, "Department": "IT"},
    {"ID": 2, "Name": "Jane Smith", "Age": 32,
        "Country": "Canada", "Salary": 55000, "Department": "HR"},
    {"ID": 3, "Name": "Ali Khan", "Age": 25, "Country": "Pakistan",
        "Salary": 40000, "Department": "Finance"},
    {"ID": 4, "Name": "Maria Gonzalez", "Age": 30, "Country": "Mexico",
        "Salary": 48000, "Department": "Marketing"},
    {"ID": 5, "Name": "Hiroshi Tanaka", "Age": 35,
        "Country": "Japan", "Salary": 60000, "Department": "IT"},
]

# Create DataFrame
df = pd.DataFrame(data)


# Saving file as csv type
df.to_csv('./dummy_data.csv',  index=False)

readDataframe = pd.read_csv('./dummy_data.csv')
# print(dataframe.to_string())
# print(dataframe.head(1))
# print(readDataframe[['Name', 'Salary']])
print(readDataframe.iloc[0, 1])  # John Doe
