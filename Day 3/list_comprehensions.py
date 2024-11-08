'''
text = input("Enter : ")
v=['a','e','i','o','u']
vowels = [x for x in text if x in v]
print(vowels)


'''

'''

even = [x for x in range(1,11) if x%2 == 0]
print(even)
'''

dict = {'a':1, 'b':2,'c':3}

for i in dict:
    new = [v: k for k,v in dict.items()]

print(new)











