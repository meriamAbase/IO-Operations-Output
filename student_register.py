# For this task, I am going to write a program that allows a user to register
# students for an exam venue. 
# I am going to store this data in a new 'txt' file.

# First, we ask the user to input the number of students they would
# like to register.
# We use a `while True` loop to continuously prompt the user until a valid
# integer is entered.
while True:
    try:
        num_of_students = int(input("How many students would you like to register? "))
        break
    except ValueError:
        print(f"{ValueError}: Please enter a valid number: ")

# We use a for loop to iterate through the `num_of_students` depending on the 
# given input.

# We then open a file named "reg_form.txt" in append mode. 
# This will create a file if one does not exist. 
# This also means that any data written to the file will be added to the end of
# the existing content, rather than overwriting it.
for student in range(num_of_students):
    student_id = input("Please enter the student ID number: ")
    with open("reg_form.txt", "a") as file:
        file.write(student_id + "........................\n")

# ==========This also works! However you prefer to write it.===========
with open("reg_form.txt", "a") as file:
    for student in range(num_of_students):
        student_id = input("Please enter the student ID number: ")
        file.write(student_id + "........................\n")
