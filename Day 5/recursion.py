# n = int(input("Enter number : "))
# factorial = 1
# def fact(n):
#     if n==0:
#         return  1
#     else :
#         factorial= n * fact(n-1)
#         return factorial
#
# print(fact(n))

n = int(input("Enter Number:"))
factorial = 1
def fact(n):
    if n==0:
        return 1
    else :
        factorial = n* fact(n-1)
        return factorial

print(fact(n))
