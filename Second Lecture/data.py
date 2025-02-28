import pandas as pd


bookList = ["Rich Dad Poor Dad",
            "The Millionaire Next Door", "Think and Grow Rich"]

serialNumbers = [101, 202, 303]

bookSeries = pd.Series(bookList, index=serialNumbers)
print(bookSeries)


books_dict = {1001: 'Fooled by Randomness',
              2002: 'Sapiens', 3003: 'Lenin on the Train'}
books_series = pd.Series(books_dict)
print(books_series)


print(books_series.equals(bookSeries))  # False
