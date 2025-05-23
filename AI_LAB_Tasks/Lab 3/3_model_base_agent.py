# A Model-Based Agent is an AI agent that maintains an internal model of the environment
# to track the state of the world. Unlike reflex agents, which rely only on current percepts,
# model-based agents use stored knowledge to make better decisions.

# Characteristics of a Model-Based Agent:
# Maintains an internal state to keep track of past actions and their effects.
# Uses a model of the environment to predict outcomes.
# Decision-making is based on both current percepts and stored state.
# Can handle partially observable environments by updating its knowledge.

# Function to update the state of a bulb (Turns it "On")
def update_state(state, bulb):
    state[bulb] = "On"  # Change the bulb state to "On"

# Function to check which bulbs are still "Off" and need to be turned "On"


def rule_match(state):
    actions = []  # List to store actions (bulbs that need turning on)
    for bulb, status in state.items():  # Loop through each bulb and its status
        if status == "Off":  # If the bulb is "Off", add it to actions list
            actions.append(bulb)
    return actions  # Return the list of bulbs that need to be turned on

# Main function to simulate the smart light controller


def simulate_light_controller():

    # Initial state: Both bulbs are "Off"
    state = {"Bulb A": "Off", "Bulb B": "Off"}

    # Goal state: Both bulbs should be "On"
    goal_state = {"Bulb A": "On", "Bulb B": "On"}

    # Counter for tracking the number of actions taken
    actions_taken = 0

    print(f"\n[Smart Light Controller] Initial Bulb States: {state}")

    # Loop until the current state matches the goal state
    while state != goal_state:
        actions = rule_match(state)  # Get bulbs that need to be turned on
        for bulb in actions:  # Iterate through the list of bulbs that need an action
            update_state(state, bulb)  # Turn the bulb on
            actions_taken += 1  # Increment action count
        print(f"Actions: {actions}, Current State: {state}")  # Print progress

    # Print the final result after achieving the goal state
    print(f"\n[Smart Light Controller] Final Bulb States: {state}")
    print(f"Total Actions Taken: {actions_taken}")


# Run the simulation
simulate_light_controller()
