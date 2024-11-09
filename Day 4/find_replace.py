txt = input("Enter string : ")
sub_string = input("Enter substring : ")
replace_string = input("Enter string to replace : ")

#first occurrence
print("First occurence : ",txt.find(sub_string))
print("Replacesed : ",txt.replace(sub_string,replace_string))


#all occurrences
# cnt = 0
# for i in txt:
#     for j in sub_string:
#         if j==i:
#             cnt=cnt+1
#
# print(int(cnt/len(sub_string)))


i=0
j=0
cnt=0

while i < len(txt):
    while j < len(sub_string):
        if sub_string[j]==txt[i]:
           j=j+1

    cnt = cnt+1

print(cnt)



