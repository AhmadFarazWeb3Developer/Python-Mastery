# What is a Table-Driven Agent?
# A Table-Driven Agent is an AI agent that stores all possible percepts(sensor inputs) in a
# predefined lookup table and decides on an action based on those stored values.
# It follows a simple condition-action rule, meaning that for every specific input(percept),
# there is a predefined output(action).

# 🚀 Key Features of a Table-Driven Agent:
# Uses a lookup table to determine actions.
# Not adaptive(doesn’t learn or improve over time).
# Works well for small, well-defined environments.
# Inefficient for large or complex environments(since storing all possible percepts is impractical).


# Stores past percepts (sensor readings)
percepts = []

# Lookup table defining actions for different sequences of percepts
table = {

    (('A', 'Clean'),): 'Right',
    (('A', 'Dirty'),): 'Remove Dirt',
    (('B', 'Clean'),): 'Left',
    (('B', 'Dirty'),): 'Remove Dirt',
    (('A', 'Clean'), ('A', "Clean")): 'Right',
    (('A', 'Clean'), ('A', "Dirty")): 'Remove Dirt',
    (('B', 'Dirty'), ('B', 'Dirty')): 'Remove Dirt',
    (('B', 'Dirty'), ('B', 'Clean')): 'Left',
    (('A', 'Dirty'), ('A', 'Dirty')): 'Remove Dirt',
    (('A', 'Dirty'), ('A', 'Clean')): 'Right',
    (('A', 'Clean'), ('A', 'Clean'), ('B', 'Dirty')): 'Remove Dirt',
    (('A', 'Clean'), ('A', 'Dirty'), ('A', 'Clean')): 'Right',
}


def lookup_table(percepts, table):
    print("Lookup table percept : ", percepts)
    action = table.get(tuple(percepts))  # nested tuple
    print("Action ", action)
    return action


def handle_percept(percept):
    print(" Captured percept :  ", percept)
    percepts.append(percept)
    action = lookup_table(percepts, table)
    return action


def main():
    percepts_list = [('A', 'Clean'), ('A', 'Clean'), ('B', 'Dirty')]
    print("Percpts     Action")
    for percept in percepts_list:
        action = handle_percept(percept)
        print(action)


main()
