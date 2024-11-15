"""def grades(list):
    try:
        for i in list:
            print(int(i))
    except :
        print("Cant convert to integer")


list = list(input("Enter : ").split(","))
grades(list)
"""

def get_grades():
    grades_input= input("Enter a list: ")
    grades_list =grades_input.split(',')
    try:
        grades = [int(grade.strip()) for grade in grades_list]
        print(f"Grades Entered: {grades}")

    except ValueError:
        print("Error: Please enter valid numbers.")

get_grades()


