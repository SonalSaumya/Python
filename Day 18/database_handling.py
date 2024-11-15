import  sqlite3

conn = sqlite3.connect('DB.db')

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS user")

cursor.execute("CREATE TABLE IF NOT EXISTS user(name TEXT, address TEXT, mobile INTEGER, email TEXT )")

cursor.execute("INSERT INTO user(name,address,mobile,email) VALUES('A','abc',123,'Agmail.com')")
cursor.execute("INSERT INTO user(name,address,mobile,email) VALUES('B','def',456,'Bgmail.com')")
cursor.execute("INSERT INTO user(name,address,mobile,email) VALUES('C','ghi',789,'Cgmail.com')")
cursor.execute("INSERT INTO user(name,address,mobile,email) VALUES('D','jkl',123,'Dgmail.com')")
cursor.execute("INSERT INTO user(name,address,mobile,email) VALUES('A','jkl',777,'ABgmail.com')")
cursor.execute("INSERT INTO user(name,address,mobile,email) VALUES('C','jkl',333,'CDgmail.com')")

conn.commit()


try:
    uname = input("Enter name : ")
    query = "SELECT * FROM user WHERE name LIKE ?"
    cursor.execute(query, uname)
    result = cursor.fetchall()

    for row in result:
        print(row)
except:
    print("Entry not found !")




