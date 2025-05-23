# 1. Write a Python program to create a list of six school subjects. Ask the user which of
# these subjects they don’t like. Delete the subjects they have chosen from the list. Display the
# final list(after deletion).

# List of school subjects
subjects = ["Maths", "Physics", "Biology", "Chemistry", "English", "Pak Study"]

# Iterate over a copy of the list using slicing (subjects[:])
for subject in subjects[:]:  # subjects[:] creates a new copy of the list
    interest = input(f"Do You like {subject}? Yes/No: ")
    if interest.lower() == "no":
        subjects.remove(subject)  # Modify the original list safely


print("Final list of subjects:", subjects)
