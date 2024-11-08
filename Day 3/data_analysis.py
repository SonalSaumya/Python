'''
no = int(input("Number of Students : "))

s_list = []

for i in range(0,no):
    info = input("Enter information : ")
    tup = tuple( x  for x in info.split(","))
    s_list.append(tup)
print(s_list)

sum = 0
stud = []
#for i in range (3):
#stud.append(s_list[0][2])

marks=[]
marks.append(list(s_list[0][2].split()))

for i in range(3):
    sum = sum + int(marks[0][i])

avg = sum/3
marks[0].append(avg)

s_list[0][2] = mar


s_list



print("marks : ",marks)
print(s_list)

no = int(input("Number of Students : "))

s_list = []

for i in range(0,no):
    info = input("Enter information : ")
    tup = tuple( x  for x in info.split(","))
    s_list.append(tup)
print(s_list)

marks=[]
marks.append(list(s_list[0][2].split()))
#print("marks : ",marks)

sum = 0
for i in range(3):
    sum+=int(marks[0][i])

avg=sum/3
#print(sum)

marks.append(avg)
print(marks)

new_list = []
new_list.append(s_list[0])
print(new_list)

'''


s_list = []
while True:
    name = input("Enter the student's name : ")
    if name.lower() == 'done' :
        break
        age = int(input(f"Enter the age for {name} : ")
        score1 = int(input(f"Enter the score for subject1 : "))
        score2 = int(input(f"Enter the score for subject2 : "))
        score3 = int(input(f"Enter the score for subject3 : "))

       # s_list.append(name,)





















