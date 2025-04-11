goalStates = {'A': '0', 'B': '0', 'C': '0'}
cost = 0
roomsStates = {'A': '0', 'B': '0', 'C': '0'}


location = input(
    'Enter Starting Location for Vacumme Cleaner A/B/C : ').strip().upper()

for room in roomsStates:
    status = input('Enter 0/1 against Clean/Dirty for {room} : ').strip()
    roomsStates[room] = status

print("Starting at Room ", location)
print("Rooms States :", roomsStates)


if goalStates != roomsStates:
    currentLocation = location

    for room in ['A', 'B', 'C']:
        if room != currentLocation:
            cost += 1
            print(
                f"\nMoving to location {room}\nCost for moving within rooms = 1")
            currentLocation = room
            if (roomsStates[room] == '1'):
                roomsStates[room] == '0'
                cost += 1
                print(
                    f"Location {room} was dirty\nLocation {room} has been cleaned\nCost for cleaning is 1.")

print("Rooms States Updated  :", roomsStates)
print("Total Cost : ", cost)
