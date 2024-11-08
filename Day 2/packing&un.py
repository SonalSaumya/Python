info = input("Enter information : ")

info = info.split(",")
my_t = tuple(info)
cc = my_t[2].split()
cc=tuple(cc)

name = my_t[0]
age = my_t[1]

city = cc[0]
country = cc[1]

print("name : " , name)
print("age : ",age)

print("city : ",city)
print("country : ", country)