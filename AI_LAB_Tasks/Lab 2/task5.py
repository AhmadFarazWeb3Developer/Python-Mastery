# # 5. (1 point) Make a dictionary called cities. Use the names of three cities as keys in your dictio-
# # nary. Create a dictionary of information about each city and include the country that the city is
# # in , its approximate population, and one fact about that city. The keys for each city’s dictionary
# # should be something like country, population, and fact. Print the name of each city and all
# # of the information you have stored about it.


# cities = {
#     "Paris": {
#         "country": "France",
#         "population": "2.1 million",
#         "fact": "Paris is known as the 'City of Light' and is home to the Eiffel Tower."
#     },
#     "Tokyo": {
#         "country": "Japan",
#         "population": "14 million",
#         "fact": "Tokyo is the most populous metropolitan area in the world."
#     },
#     "New York": {
#         "country": "USA",
#         "population": "8.3 million",
#         "fact": "New York City is known as 'The Big Apple' and has the famous Times Square."
#     }
# }


# for city, info in cities.items():
#     print(f"\nCity: {city}")
#     for key, value in info.items():
#         print(f"{key.capitalize()}: {value}")
list=['1','2','3']
for item in list:
    print("Item in {item}")