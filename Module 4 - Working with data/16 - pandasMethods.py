import pandas as pd

data = [
    {"Name": "Alice", "Age": 25, "City": "New York"},
    {"Name": "Bob", "Age": 30, "City": "Los Angeles"},
    {"Name": "Alice", "Age": 25, "City": "New York"},
    {"Name": "David", "Age": 35, "City": "Chicago"},
    {"Name": "Eve", "Age": 28, "City": "Houston"},
    {"Name": "Frank", "Age": 22, "City": "Phoenix"},
    {"Name": "Grace", "Age": 28, "City": "Houston"},
    {"Name": "Hannah", "Age": 35, "City": "Chicago"},
    {"Name": "Isaac", "Age": 40, "City": "San Francisco"},
    {"Name": "Jack", "Age": 22, "City": "Phoenix"}
]


df = pd.DataFrame(data)
print(df.head())  # prints the first five lines of dataframe

# print(df['Age'] > 30)
# print(df['City'].duplicated())


# df = pd.DataFrame({'a': [1, 2, 1], 'b': [1, 1, 1]})
# print(df['a'] == 1)
