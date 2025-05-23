# 7. (1 point) A university wants to automate the grading system for students. The system should
# categorize students based on their marks and assign letter grades.
# 1. Accept student names and their corresponding marks(out of 100) as a list of tuples.
# 2. Implement a function to assign grades based on the following criteria:
# • 90-100: A
# • 80-89: B
# • 70-79: C
# • 60-69: D
# • Below 60: F
# 3. Store students in different lists based on their grades.
# 4. Display the highest and lowest scorers.
# 5. Calculate and display the class average.



def assign_grades(students_marks):

    grade_categories = {
        "A": [],
        "B": [],
        "C": [],
        "D": [],
        "F": []
    }

    total_marks = 0

    for student, marks in students_marks:
        if 90 <= marks <= 100:
            grade_categories["A"].append((student, marks))
        elif 80 <= marks <= 89:
            grade_categories["B"].append((student, marks))
        elif 70 <= marks <= 79:
            grade_categories["C"].append((student, marks))
        elif 60 <= marks <= 69:
            grade_categories["D"].append((student, marks))
        else:
            grade_categories["F"].append((student, marks))

        total_marks += marks

    average = total_marks / len(students_marks)

    highest_scorer = max(students_marks, key=lambda x: x[1])
    lowest_scorer = min(students_marks, key=lambda x: x[1])

    return grade_categories, average, highest_scorer, lowest_scorer


students_marks = [
    ("Ahmad Faraz", 80),
    ("Saad Israr", 90),
    ("Sahal Sajeed", 80),
    ("Arsalan Aslam", 75),
    ("Hammayun Farrasat", 95),
    ("Muhammad Danish", 100),
    ("Huzaifa Sahahab", 90),
    ("James Goslang", 60),
    ("Nadar Shah", 55),
    ("Khanzada", 45)
]

grade_categories, average, highest_scorer, lowest_scorer = assign_grades(
    students_marks)

print("\n----Student Grades Categorization----\n")
for grade, students in grade_categories.items():
    print(f"Grade {grade}: {students}")

print("\n--------------------------------------\n")
print(f"\nClass Average Marks: {average:.2f}")
print("\n--------------------------------------\n")
print(
    f"\nHighest Scorer: {highest_scorer[0]} with {highest_scorer[1]} marks")
print(f"Lowest Scorer: {lowest_scorer[0]} with {lowest_scorer[1]} marks")
print("\n--------------------------------------\n")

# How lambda x: x[1] Works
# lambda x: x[1] is an anonymous function that tells max() and min() to only consider the marks(second value in the tuple) when comparing.
# x[1] means "use the second element (marks) from each tuple".
