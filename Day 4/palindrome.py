'''
#siddhi

txt = input("Enter string : ")

new_txt = txt.replace(" ","")

new_new_text = new_txt.lower()

length = len(new_new_text)-1

reverse = []
while length >= 0:
    reverse.append(new_new_text[length])
    length=length-1

#print(reverse)

rev_string =""
for i in reverse:
    rev_string= rev_string+i

if new_new_text==rev_string:
    print("Yes")
else:
    print("No")

#print(rev_string)
'''
