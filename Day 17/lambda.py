# names = [('A',30),('A',25),('A',35)]
#
# sorted_list = (lambda names : names[i][1].sort() for i in range(len(names)-1))
#
# print(sorted_list(names))

people = [('Maurya', 30), ('Pravin',25), ('Reeya',35)]
sorted_people = sorted(people, key = lambda x: x[1])
print ("Sorted list by age:", sorted_people)
