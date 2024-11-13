import sqlite3

conn = sqlite3.connect('DAI.db')

cursor = conn.cursor()

#cursor.execute("drop table users")

cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TXT, age INTEGER)")

cursor.execute("INSERT INTO users(name, age) VALUES ('Sonal',23)")
cursor.execute("INSERT INTO users(name, age) VALUES ('Niranjan',24)")
cursor.execute("INSERT INTO users(name, age) VALUES ('Siddhi',20)")
cursor.execute("INSERT INTO users(name, age) VALUES ('Priya',25)")


conn.commit()

print("Users: \n")
cursor.execute("SELECT * FROM users")

print("Order by clause \n")
cursor.execute("SELECT * FROm users ORDER BY age")
while True:
    row = cursor.fetchone()
    if row is None:
        break
    print(row)
print("\n Users grouped by age with count:")
cursor.execute("SELECT age,COUNT(*) as count FROM users GROUP BY age")
results = cursor.fetchall()
for row in results:
    print(row)

cursor.execute(UPDATE users SET age= 22 WHERE name = 'Siddhi'")




