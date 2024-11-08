l1 = []

n = int(input("Enter no of elements : "))

for i in range(0,n):
    l1.append(int(input("Enter element : ")))

print(l1)


l2 = []

for i in range (len(l1)):
    if (i+2) < len(l1):
        l2.insert((i+2),l1[i])
    else :
        l2.insert((i-(n-2)),l1[i])

print(l2)







