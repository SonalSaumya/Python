'''

#siddhi

dict = {}

while True:
    l = []
    tup = ()

    tup = tuple(input("Enter elemts of Tuple :").split())
    l.append(tup)

    if tup[0] in dict:
        del dict[tup[0]]

    for i in tup:
        dict[tup[0]]=tup[1]

    print(tup)
    print(dict)

'''


dict = {}
while True:
    l=[]

    tup = tuple(input("Enter elements of Tuple : ").split())
    l.append(tup)


    for i in tup:
        dict[tup[0]] = tup[1]

    print(tup)
    print(dict)