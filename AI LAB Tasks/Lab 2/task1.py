# 1. Write a Python program to create a list of six school subjects. Ask the user which of
# these subjects they don’t like. Delete the subjects they have chosen from the list. Display the
# final list(after deletion).


subjects = ["Maths", "Physics", 'Biology', "Chemistry", "English", "Pak Study"]

for subject in subjects:
    interest = input(f"Do You like {subject}? Yes/No: ")
    if interest.lower() == "no":
        subjects.remove(subject)


print("Final list of subjects:", subjects)
