# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total = 0  
for student_height in student_heights:
  total += student_height

AVG = total / len(student_heights)
print(f"total height = {total}")
print(f"number of students = {len(student_heights)}")
print(f"average height = {round(AVG)}")