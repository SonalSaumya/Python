import sqlite3

conn = sqlite3.connect('school.db')

cursor = conn.cursor()

#
cursor.execute("DROP TABLE students")
cursor.execute("DROP TABLE courses")

cursor.execute("CREATE TABLE IF NOT EXISTS students (student_id INTEGER PRIMARY KEY, name TEXT, age INTEGER, grade TEXT)")

cursor.execute("CREATE TABLE IF NOT EXISTS courses (course_id INTEGER PRIMARY KEY,course_name TEXT,instructor TEXT)")


cursor.execute("INSERT INTO students (student_id, name, age, grade) VALUES (1,'Sonal',  24, 'A')")
cursor.execute("INSERT INTO students (student_id, name, age, grade) VALUES (2, 'Siddhi', 23, 'A')")
cursor.execute("INSERT INTO students (student_id, name, age, grade) VALUES (3, 'Alisa',  25, 'B')")
cursor.execute("INSERT INTO students (student_id, name, age, grade) VALUES (4, 'Geetika',24, 'C')")
cursor.execute("INSERT INTO students (student_id, name, age, grade) VALUES (5, 'Hemanshi',26, 'B')")


cursor.execute("INSERT INTO courses(course_id , course_name, instructor) VALUES (1, 'DAI', 'Anjali')")
cursor.execute("INSERT INTO courses (course_id , course_name, instructor) VALUES (2, 'Maths', 'Sajida')")
cursor.execute("INSERT INTO courses (course_id , course_name, instructor) VALUES (3, 'English', 'Vishwanath')")

conn.commit()



cursor.execute("SELECT * FROM students WHERE grade = 'A'")
result= cursor.fetchall()
for row in result:
    print(row)



cursor.execute("UPDATE courses SET instructor = 'Anjali' WHERE course_id =2")
cursor.execute("SELECT * FROM courses")
data= cursor.fetchall()
for row in data:
    print(row)


cursor.execute("DROP TABLE students")


# res  = cursor.execute("SELECT * FROM courses")
# print(res)


