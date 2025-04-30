def summary(data):
    for student in data:
        total = sum(student['scores'])
        avg = round(total / len(student['scores']), 1)
        print(f"{student['name']}: Total = {total}, Average = {avg}")

students = [
    {'name': 'Alice', 'scores': [90, 80, 70]},
    {'name': 'Bob', 'scores': [100, 85, 95]}
]

print("Student Summary:")
summary(students)

