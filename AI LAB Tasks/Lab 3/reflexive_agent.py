
goalState = {'A': '0', 'B': '0', 'C': '0'}
cost = 0
roomStates = {'A': '0', 'B': '0', 'C': '0'}

print("Enter the starting location of vacuum (A/B/C) = ")
location = input().strip().upper()
print()

for room in roomStates:
    action = input("Enter the state of " + room +
                   " (0 for clean /1 for dirty): ").strip()
    roomStates[room] = action

print("\nCurrent State: " + str(roomStates))
print("\nGoal state: " + str(goalState))
print("\nVacuum is placed in location " + location)

if roomStates != goalState:
    for room in ['A', 'B', 'C']:
        if roomStates[room] == '1':
            roomStates[room] = '0'
            cost += 1
            print(
                f"Location {room} was dirty\nLocation {room} has been cleaned\nCost for cleaning is 1.")
        if room != location:
            cost += 1
            print(
                f"\nMoving to location {room}\nCost for moving within rooms = 1")

    print("\nGoal state has been met.")
    print("\nTotal cost: " + str(cost))
else:
    print("\nAll rooms are already clean")
    print("\nTotal cost: " + str(cost))
