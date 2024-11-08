vals = input("Enter values : ")

my_t = tuple(int(x) for x in vals.split(","))

print(sorted(my_t))

th = int(input("Enter threshold value : "))

new = []
for i in my_t :
    if i > th:
        new.append(i)

print(new)

