#prime = [x for x in range(1,51)  if x%2!==0 ]
# y = 50
# prime = [x for x in range(2,y+1) if all x%y != 0 for y in range(2,x)]
# print(prime)
'''
def is_prime(n):
    if n <= 1:
       return False
    for i in range(2, int(n**0.5) + 1):
        if n % 1== 0:
           return False
    return True

prime = [x for x in range (1,51) if is_prime(x)]
print(prime)
'''

prime = [num for num in range(2,15) if all (num%i !=0 for i in range (2, int (n**0.5)+1))]