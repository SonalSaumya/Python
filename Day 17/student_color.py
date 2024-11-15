dict = {
    'A': 'Blue',
    'D': 'Yellow',
    'C':'Purple',
    'B':'Pink'
}

print(len(dict))

dict['B'] = "Red"
print(dict)

del dict['D']


myKeys = list(dict.keys())
myKeys.sort()
print(myKeys)

dict_n = {}

for i in myKeys:
    dict_n[i] = dict[i]

print(dict_n)


