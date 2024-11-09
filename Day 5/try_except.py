# def pint():
#     try :
#         no = int(input("Enter no :"))
#         print(no)
#     except ValueError:
#         print("Not a integer ")
#
#
# print(pint())

''' Code for Try Except '''
def pint():
    ''' Code for pint'''
    try :
        no = int(input("Enter no :"))
        print(no)

    except ValueError:
        print("Not a integer ")

print(pint())

def get_ele_list ():
    try :
        no = list(input("Enter list : ").split())
        pos = int(input("Enter index : "))

        # for i in range(0,10):
        #     print(no[i])

        print(no[pos])

    except IndexError:
        print("Item not found")

    except ValueError:
        print("Index not a integer")

    else :
        print("Completed")



print(get_ele_list())







