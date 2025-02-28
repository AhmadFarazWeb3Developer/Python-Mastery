
cities = {
    "Paris": {
        "country": "France",
        "population": "2.1 million",
        "fact": "Paris is known as the 'City of Light' and is home to the Eiffel Tower."
    },
    "Tokyo": {
        "country": "Japan",
        "population": "14 million",
        "fact": "Tokyo is the most populous metropolitan area in the world."
    },
    "New York": {
        "country": "USA",
        "population": "8.3 million",
        "fact": "New York City is known as 'The Big Apple' and has the famous Times Square."
    }
}


for city, info in cities.items():
    print(f"\nCity: {city}")
    for key, value in info.items():
        print(f"{key.capitalize()}: {value}")
