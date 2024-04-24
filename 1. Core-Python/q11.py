# @author: 22000214 - Abhiraj Chaudhuri
# @description: Program No. 11. Write a program to input roll no, student name, marks of physics, chemistry and maths out of
# 100. (0-100). Calculate total, percentage, calculate STATUS (pass, fail) if students scores
# above 40 in all the 3 subjects the STATUS should be pass otherwise fail.
# Calculate GRADE if STATUS is pass.
# Grade must be based on percentage value
# if percentage is above 70, then grade must be DISTINCTION if
# percentage is above 60, then grade must be FIRST CLASS
# if percentage is above 50, then grade must be SECOND CLASS if
# percentage is above 40, then grade must be PASS CLASS

rollNo = int(input("Enter roll no: "))
physics = int(input("Enter physics marks: "))
chemistry = int(input("Enter chemistry marks: "))
maths = int(input("Enter maths marks: "))

total = physics + chemistry + maths
percentage = total / 3

if physics > 40 and chemistry > 40 and maths > 40:
    status = "Pass"
else:
    status = "Fail"

if percentage > 70:
    grade = "Distinction"
elif percentage > 60:
    grade = "First Class"
elif percentage > 50:
    grade = "Second Class"
elif percentage > 40:
    grade = "Pass Class"
else:
    grade = "Fail"
print(f"Total marks: {total}")
print(f"Percentage: {percentage}%")
print(f"Status: {status}")
print(f"Grade: {grade}")

# output:
# Enter roll no: 214
# Enter physics marks: 89
# Enter chemistry marks: 73
# Enter maths marks: 92
# Total marks: 254
# Percentage: 84.66666666666667%
# Status: Pass
# Grade: Distinction
