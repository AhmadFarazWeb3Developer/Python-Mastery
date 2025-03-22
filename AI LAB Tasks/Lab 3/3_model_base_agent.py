def update_state(state, bulb):

    state[bulb] = "On"


def rule_match(state):

    actions = []
    for bulb, status in state.items():
        if status == "Off":
            actions.append(bulb)
    return actions


def simulate_light_controller():

    state = {"Bulb A": "Off", "Bulb B": "Off"}
    goal_state = {"Bulb A": "On", "Bulb B": "On"}
    actions_taken = 0

    print(f"\n[Smart Light Controller] Initial Bulb States: {state}")

    while state != goal_state:
        actions = rule_match(state)
        for bulb in actions:
            update_state(state, bulb)
            actions_taken += 1
        print(f"Actions: {actions}, Current State: {state}")

    print(f"\n[Smart Light Controller] Final Bulb States: {state}")
    print(f"Total Actions Taken: {actions_taken}")


simulate_light_controller()
