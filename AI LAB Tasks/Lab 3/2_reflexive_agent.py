
# A reflexive agent (or simple reflex agent) is an AI agent that
# acts based on the current percept without considering past percepts
# or future consequences.It follows a set of predefined condition-action rules, meaning
# that for each specific percept (input from the environment), the agent takes a corresponding action.

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
print("\nVacuumer is placed in location " + location)

if roomStates != goalState:
    # Keep track of current position
    current_location = location

    for room in ['A', 'B', 'C']:
        if room != current_location:
            cost += 1
            print(
                f"\nMoving to location {room}\nCost for moving within rooms = 1")
            current_location = room  # Update current location

        if roomStates[room] == '1':  # Check for dirt AFTER moving
            roomStates[room] = '0'
            cost += 1
            print(
                f"Location {room} was dirty\nLocation {room} has been cleaned\nCost for cleaning is 1.")

    print("\nGoal state has been met.")
    print("\nTotal cost: " + str(cost))
else:
    print("\nAll rooms are already clean")
    print("\nTotal cost: " + str(cost))
