no = input("Enter number : ")
ans = 0
for i in no :
    ans = ans + int(i)

print(ans)


n =  int(input("Enter number : "))
sum = 0
while n >0:
    mod = n%10
    sum+=mod
    n= n/10

print(int(sum))

