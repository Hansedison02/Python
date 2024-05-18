# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Find the highest score
highest_score = max(student_scores)

print(f"The highest score in the class is: {highest_score}")