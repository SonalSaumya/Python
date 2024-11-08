

n1 = input("Enter tuple")
t1 = tuple(int(x) for x in n1.split(","))
s1 = set(t1)

n2 = input("Enter tuple")
t2 = tuple(int(x) for x in n2.split(","))
s2 = set(t2)

common = s1.intersection(s2)

print(common)






