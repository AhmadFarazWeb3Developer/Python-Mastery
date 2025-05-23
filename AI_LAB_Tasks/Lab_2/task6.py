# 6. (1 point) A company wants to keep track of daily tasks assigned to its employees. Each employee
# is assigned multiple tasks, and you are required to develop a Python program to manage this
# system.
# 1. Create a list where each element is a tuple containing the employee’s name and a list of
# their assigned tasks.
# 2. Implement a function that allows a manager to add a new task for an employee.
# 3. Implement a function that removes a completed task.
# 4. If an employee has more than 5 tasks, display a warning message.
# 5. Print all employees and their remaining tasks at the end.

# Function to add a new task for an employee
def add_new_task(employee_name, task, employees):
    for employee in employees:
        if employee[0] == employee_name:
            if len(employee[1]) >= 5:  # Warning if tasks exceed 5
                print(f"⚠️ Warning: {employee_name} has too many tasks!")
            employee[1].append(task)
            return
    print(f"Employee '{employee_name}' not found!")

# Function to remove a completed task


def remove_completed_task(employee_name, task, employees):
    for employee in employees:
        if employee[0] == employee_name:
            if task in employee[1]:
                employee[1].remove(task)
            else:
                print(f"Task '{task}' not found for {employee_name}!")
            return
    print(f"Employee '{employee_name}' not found!")

# Function to display all employees and their tasks


def display_tasks(employees):
    print("\n📋 Employee Task List:")
    for employee in employees:
        print(
            f"{employee[0]}: {', '.join(employee[1]) if employee[1] else 'No tasks assigned'}")


# Initialize the list of employees with their assigned tasks
employees = [
    ('Ahmad Faraz', ["Product Manager", "Event Organizer"]),
    ('Sahal Sajeed', ["HR Manager", "Public Speaker"])
]

# Add tasks
add_new_task("Ahmad Faraz", "Finance Manager", employees)
add_new_task("Ahmad Faraz", "Marketing Lead", employees)
add_new_task("Ahmad Faraz", "Tech Consultant", employees)
add_new_task("Ahmad Faraz", "Sales Representative", employees)
add_new_task("Ahmad Faraz", "Customer Support",
             employees)  # Should trigger a warning
add_new_task("Sahal Sajeed", "Team Coordinator", employees)

# Display tasks before removal
display_tasks(employees)

# Remove completed tasks
remove_completed_task("Sahal Sajeed", "Team Coordinator", employees)
remove_completed_task("Ahmad Faraz", "Finance Manager", employees)

# Display tasks after removal
display_tasks(employees)
