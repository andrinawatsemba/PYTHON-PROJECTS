def calculate_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

students = []

while True:
    name = input("Enter student name (or 'q' to quit): ")
    if name.lower() == 'q':
        break
    scores = []
    for i in range(3):
        score = float(input(f"Enter mark {i+1}: "))
        scores.append(score)
    avg = sum(scores) / len(scores)
    grade = calculate_grade(avg)
    students.append((name, avg, grade))
    print(f"{name}'s average: {avg:.2f}, Grade: {grade}\n")

print("\nAll Records:")
for s in students:
    print(f"Name: {s[0]}, Avg: {s[1]:.2f}, Grade: {s[2]}")