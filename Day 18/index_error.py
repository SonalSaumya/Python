def list_print(name):
    try:
        for i in range(10):
            print(name[i])
    except :
        print("Index error")


list = [1,2,3,4,5]

list_print(list)