
'''
#Siddhi
text = input("Enter string : ")

vowel= ['a','e','i','o','u','A','E','I','O','U']

new_str=""
for i in text:
    if i in vowel:
        new_str+="abc"
    else:
        new_str+=i

print(new_str)
'''


import re
def translate(text):
    return
text = "This is fun."
pat = r'AEIOUaeiou'
match= re.sub(r'[AEIOUaeiou]', 'abc', text)
print(match)