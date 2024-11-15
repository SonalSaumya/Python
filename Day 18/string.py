
'''
#Siddhi
string = input("Enter string : ")
length = len(string)
print(length)


if length%2 != 0:
    a=length//2
    print(string[a-1:a+2])
else:
    a=(length//2)-1
    print(string[a:a+2])


str = "Hello,world!"

print(str[0:len(str):2])
'''
