# Pandas is a Python library used for working with DATA SETS.
# It has functions for analyzing, cleaning, exploring, and manipulating data.
# The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis"
# and was created by Wes McKinney in 2008.

import pandas as pd

# print(pd.__version__) checking pandas version

# -- LIST OF STRINGS TO SERIES --
studentsList = ["alice", "jack", "molly"]

studentsSeries = pd.Series(studentsList)  # creating a series from a list
print(studentsSeries)  # printing the series


for i in studentsSeries:  # iterating through the series
    print(i)


# -- LIST OF NUMBERS TO SERIES --

numbersList = [1, 2, 3, 4, 5]
numbersSeries = pd.Series(numbersList)  # creating a series from a list
print(numbersSeries)  # printing the series

#  -- LIST OF FLOATS TO SERIES --

floatsList = [1.1, 2.2, 3.3, 4.4, 5.5]
floatsSeries = pd.Series(floatsList)  # creating a series from a list
print(floatsSeries)  # printing the


# -- LIST OF MIXED DATA TYPES TO SERIES --

mixedList = [1, "alice", 3.3, 4.4, 5.5, {"name": "jack"}]
mixedSeries = pd.Series(mixedList)  # creating a series from a list
print(mixedSeries)  # printing the series
