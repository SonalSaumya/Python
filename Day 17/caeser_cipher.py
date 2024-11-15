
dict= {}

for i in range(97,110):
    k=(i+13)
    dict[chr(i)] = chr(k)

for i in range(65,78):
    k = (i + 13)
    dict[chr(i)] = chr(k)


i=110
while(i>=122):
    k=i-13
    dict[chr(i)]=chr(k)
    i=i+1


print(dict)

code = input("Enter code : ")
new_code=""

for i in code:
    new_code+=dict[i]

print(new_code)


