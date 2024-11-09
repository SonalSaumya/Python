import csv
def write_students_to_csv(filename:str, student_list: list):
    fieldnames = [ 'ID', 'Name', 'Age', 'Grade' ]

    try:
        with open(filename, mode = 'w', newline = '') as file:
            writer = csv.DictWriter(file,fieldnames=fieldnames)

            writer.writeheader()
            for student in student_list:
                writer.writerow(student)

                print(f"Data successfully written to {filename}" )
    except Exception as e: print(f"An error occurred while writing to {filename}: {e}")


def read_csv_and_print(filename:str):
    try:
        with open(filename,mode='r', newline='') as file:
            reader= csv.DictReade(file)

            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred while reading from {filename}: {e}")

student_list = [{'ID':1, 'Name': 'Alice', 'Age': 14,'Grade': 'A'},
{'ID':2, 'Name': 'Bob', 'Age': 15,'Grade': 'B'},
{'ID':3, 'Name': 'Charlie', 'Age': 13,'Grade': 'A'},
{'ID':4, 'Name': 'Diana', 'Age': 14,'Grade': 'C'}]

filename = "student.csv"
write_students_to_csv(filename,student_list)
read_csv_and_print(filename)




