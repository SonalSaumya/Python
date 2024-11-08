



print("Enter 1 to add ")
print("Enter 2 to remove  ")
print("Enter 3 to view  ")


'''
while True:
    if input('Do You Want To Continue? ') != 'y':

        action = input("Enter action : ")
    if action ==1 :
        t = print("Enter task to add : ")
        todo.append(t)
        print(todo)

    elif action == 2:
        r = print("Enter task to remove : ")
        todo.pop(todo.index(r))

    elif action == 3 :
        print(todo)
        
'''
todo=[]
y = input("Do ypu want to continue : ")
if y=='y':
    action = input("Enter action : ")

    if action == 1:
        t = print("Enter task to add : ")
        todo.append(t)
        print(todo)

    elif action == 2:
        r = print("Enter task to remove : ")
        todo.pop(todo.index(r))

    elif action == 3:
        print(todo)







