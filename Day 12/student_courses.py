import sqlite3

conn = sqlite3.connect('school.db')

cursor = conn.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS students(id INTEGER, name TEXT,age INTEGER,grade TEXT)")

cursor.execute("CREATE TABLE IF NOT EXISTS  courses (cid INTEGER, cname TEXT, inst TEXT)")

cursor.execute("INSERT INTO students (id,name,age,grade) VALUES (1,'A',24,'A')")
cursor.execute("INSERT INTO students (id,name,age,grade) VALUES (2,'B',25,'B')")
cursor.execute("INSERT INTO students (id,name,age,grade) VALUES (3,'C',26,'C')")
cursor.execute("INSERT INTO students (id,name,age,grade) VALUES (4,'D',27,'D')")

cursor.execute("INSERT INTO courses(cid,cname ,inst) VALUES (9,'A','A')")
cursor.execute("INSERT INTO courses(cid,cname ,inst) VALUES (8,'B','B')")
cursor.execute("INSERT INTO courses(cid,cname ,inst) VALUES (7,'C','C')")

print("INSERTED")

conn.commit()

result = cursor.execute("SELECT * FROM students")
print(result)