

def update_state(current_states, bulb):
    current_states[bulb] = "On"


def rule_match(current_states):
    actions = []
    for bulb, state in current_states.items():
        if (state == "Off"):
            actions.append(bulb)
    return actions


def simulate_light_contoller():
    current_states = {"Bulb A": "On", "Bulb B": "Off"}
    goal_states = {"Bulb A": "On", "Bulb B": "On"}
    actionTaken = 0

    while current_states != goal_states:
        actions = rule_match(current_states)
        for bulb in actions:
            update_state(current_states, bulb)
            actionTaken += 1
        # Print progress
        print(f"Actions: {actions}, Current State: {current_states}")

    # Print the final result after achieving the goal state
    print(f"\n[Smart Light Controller] Final Bulb States: {goal_states}")
    print(f"Total Actions Taken: {actionTaken}")


simulate_light_contoller()
