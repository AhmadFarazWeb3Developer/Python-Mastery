# 8. (1 point) A car rental company wants a Python system to manage their vehicle rentals. Each
# vehicle has a unique ID, model name, rental price per day, and availability status.
# 1. Store vehicle details in a list of tuples in the format: (ID, Model, Price per day, Available/Not
# Available).
# 2. Implement a function that allows a customer to rent a vehicle by providing its ID.
# 3. Prevent a vehicle from being rented if it is already taken.
# 4. Implement a function to return a rented vehicle and mark it as available.
# 5. Display the total earnings from rented vehicles.


def rentVehicle(vehicleID, vehicles):
    for i, vehicle in enumerate(vehicles):
        if vehicle[0] == vehicleID:
            if vehicle[3] == "Available":
                vehicles[i] = (vehicle[0], vehicle[1],
                               vehicle[2], "Not Available")
                print(f"Vehicle {vehicleID} has been rented.")
                return vehicle[2]
            else:
                print(f"Vehicle {vehicleID} is already rented.")
                return 0
    print("Vehicle does not exist.")
    return 0


def returnVehicle(vehicleID, vehicles):
    for i, vehicle in enumerate(vehicles):
        if vehicle[0] == vehicleID:
            if vehicle[3] == "Not Available":
                vehicles[i] = (vehicle[0], vehicle[1], vehicle[2], "Available")
                print(f"Vehicle {vehicleID} has been returned.")
                return
            else:
                print(f"Vehicle {vehicleID} is already available.")
                return
    print("Vehicle does not exist.")


def totalEarnings(rented_prices):
    print(f"Total earnings from rented vehicles: ${sum(rented_prices)}")


vehicles = [
    ("LZR", "2012", 1000, "Available"),
    ("TYT", "2018", 1500, "Not Available"),
    ("HND", "2020", 2000, "Available"),
    ("FRD", "2015", 1300, "Available"),
    ("BMW", "2022", 3000, "Not Available"),
    ("MCD", "2019", 2500, "Available"),
    ("AUD", "2021", 2800, "Not Available"),
    ("KIA", "2017", 1600, "Available"),
    ("TES", "2023", 3500, "Available"),
    ("NIS", "2016", 1400, "Not Available")
]

rented_prices = []
rented_prices.append(rentVehicle("LZR", vehicles))
rented_prices.append(rentVehicle("HND", vehicles))
rented_prices.append(rentVehicle("TES", vehicles))


returnVehicle("LZR", vehicles)

totalEarnings(rented_prices)


# The enumerate() function in Python is used when you need
# both the index and the value of items while looping through
# a list ( or any iterable).
