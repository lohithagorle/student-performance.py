# Student Performance Management System

print("===== Student Performance Management System =====")

# Input student details
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

# Input marks
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))
sub4 = float(input("Enter marks for Subject 4: "))
sub5 = float(input("Enter marks for Subject 5: "))

# Calculate total and percentage
total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total / 5

# Check pass/fail
if sub1 >= 35 and sub2 >= 35 and sub3 >= 35 and sub4 >= 35 and sub5 >= 35:
    result = "PASS"
else:
    result = "FAIL"

# Assign grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
elif percentage >= 35:
    grade = "E"
else:
    grade = "F"

# Display report
print("\n========== STUDENT REPORT ==========")
print("Student Name :", name)
print("Roll Number  :", roll_no)
print("Total Marks  :", total, "/500")
print("Percentage   :", round(percentage, 2), "%")
print("Grade        :", grade)
print("Result       :", result)
print("====================================")
