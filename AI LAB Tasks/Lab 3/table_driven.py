percepts = []
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
    action = table.get(tuple(percepts))
    return action


def table_driven_agent(percept):
    percepts.append(percept)
    action = lookup_table(percepts, table)
    return action


def main():
    print('Percepts \t\t\t Action')


main()
