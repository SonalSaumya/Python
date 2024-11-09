txt = input("Enter Text :")
txt = txt.split()
print(txt)

for i in range(0,len(txt)):
    if i%2 != 0:
        txt[i] = 'replaced'

new_string = ""

#using string cincatination
# for i in txt:
#     new_string=new_string+i

#using join
print(txt)
print(new_string.join(txt))


