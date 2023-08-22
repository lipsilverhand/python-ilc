student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for x in student_scores:
    scores = student_scores[x]
    if scores > 90 :
        student_grades[x] = "Outstanding"
    elif scores > 80:
        student_grades[x] = "Exceeds Expectations"
    elif scores > 70:
        student_grades[x] = "Acceptable"
    else:
        student_grades[x] = "Fail"

print(student_grades)