import re
txt = "aiddhi and sonal a 777hhh ee i ies no 777h priya siddh7i oi sh7intre and sonal 6ngh and aaumyas 1jkj Notebfh_____==-=-gf!"

# task 1
for i in txt.split():
   result = re.findall(r'\b[aeiou].*[bcdfghjklmnqrstvwxyz]\b', i)
   if result:
       print(result)
#
# task 2
for i in txt.split():
    result = re.findall(r'\b\d.*[^0-9]\b',i)
    if result :
        print(result)

#task3
for i in txt.split():
    result = re.findall(r'^Note.*!$',i)
    if result:
        print(result)










