txt = input("Enter paragraph : ")
txt = txt.split()
txt = set(txt)
txt = sorted(txt)
print(txt)

for i in txt:
    print(i)