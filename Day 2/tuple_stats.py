vals = input("Enter values : ")

my_t = tuple(int(x) for x in vals.split(","))
print(my_t)

#sum
sum =0
for i in my_t:
    sum+=i
print("Sum of elemenst : ", sum)

#avg
print("Average : ",sum/len(my_t))

#max
max = my_t[0]
for i in range(1,len(my_t)):
    if my_t[i] > my_t[0]:
        max = my_t[i]

print("Max value : ",max)

#min
min = my_t[0]
for i in range(1,len(my_t)):
    if my_t[i] < my_t[0]:
        min = my_t[i]
print("Min value : ",min)

print("Lenth of tuple : ", len(my_t))


