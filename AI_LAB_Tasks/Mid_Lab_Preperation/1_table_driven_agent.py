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

percepts = []


def lookup_table(percepts, table):
    action = table.get(tuple(percepts))
    return action


def handle_percepts(percept):
    percepts.append(percept)
    action = lookup_table(percepts, table)
    return action


percepts_list = (('A', 'Clean'), ('A', "Clean"))


for percept in percepts_list:
    action = handle_percepts(percept)
print("Action :", action)
