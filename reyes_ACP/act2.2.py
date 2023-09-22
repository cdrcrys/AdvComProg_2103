grades = []

subjects = ["English", "Filipino", "Science", "Math", "Araling Panlipunan", "Physical Education"]

for subject in subjects:
    grade = float(input(f"Enter your grade for {subject}: "))
    grades.append(grade)

average = sum(grades) / len(grades)
print(f"Average Grade: {average:.2f}")