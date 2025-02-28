
name = input("Enter student name: ")
reg_no = int(input("Enter registration number: "))
subject_names = ["Maths", "Physics",
                 "Chemistry", "Biology", "Computer Science"]
subject_marks = []

print("\nEnter total marks for each subject out of 100 : \n")

obtained_marks = 0
for i in range(5):
    print("Enter mark of ", subject_names[i], ": ")
    subject_marks.append(int(input(subject_names[i] + ": ")))
    obtained_marks += subject_marks[i]

percentage = float(obtained_marks/500*100)

print("\n\n--- Your Details ---\n")
print(name)
print(reg_no)
for i in range(5):
    print("subject name", "Marks")
    print(subject_names[i], subject_marks[i])
print("Obtained Marks ", obtained_marks)
print("Total Marks 500")
print("Percentage : ", round(percentage, 2), "%")
