c1 = 0

password = input("Enter password : ")

if len(password) >=8 :
    c1 = c1+1

for i in password :
    if i.isupper() :
        c1 = c1+1
        break

for i in password:
    if i.islower():
        c1 = c1+1
        break

for i in password :
    if i== '!' or i=='@' or i=='@' or i=='#' or i=='$' :
        c1 = c1+1
        break

if c1 == 1:
    print("Weak")
elif c1 == 2 or c1==3:
    print("Moderate")
elif c1==4:
    print("Strong")
else :
    print("Invalid")

