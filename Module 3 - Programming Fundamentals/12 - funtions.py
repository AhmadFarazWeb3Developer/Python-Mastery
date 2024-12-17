
# Sorted vs Sort


ratings = [23, 45, 1, 2, 3, 4, 5, 6, 67, 87]
sortedRatings = sorted(ratings)
print("Sorted One  : ", sortedRatings, "\nOrignal One : ", ratings)


ratings.sort()
print("Orignal Ratings Sorted : ", ratings)

# Sorted One:  [1, 2, 3, 4, 5, 6, 23, 45, 67, 87]
# Orignal One:  [23, 45, 1, 2, 3, 4, 5, 6, 67, 87]
# Ratings:  [1, 2, 3, 4, 5, 6, 23, 45, 67, 87]


# FUNCTION

a = 1


def myFun(ratings):
    for i, rating in enumerate(ratings):
        print(i, ' rating ', rating)


myFun(ratings)


# Collecting Arguments

def Artists(*names):
    for artist in names:
        print(artist)


Artists("Ahmad Faraz", "Nadar Shah", "Saqib Khan", "Ali baba")

# Ahmad Faraz
# Nadar Shah
# Saqib Khan
# Ali baba


def f(*x):
    return sum(x)
