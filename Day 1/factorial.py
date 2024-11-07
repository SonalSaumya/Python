num = int(input("Enter number : "))
fact = 1
if num == 0 :
    fact =1

else :
     while num > 1:
        fact *= num
        num -= 1
print(fact)