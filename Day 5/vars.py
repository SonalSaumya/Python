# sum = 0
#
# def nums():
#     numbers = list(input("Enter numbers : ").split())
#     num_list  = [int(x) for x in numbers]
#     add=0
#     for i in num_list:
#         add=add+i
#     return add
#
#
#
#
# print("Global Sum Before Calling: ", sum)
# sum = nums()
# print("Global sum after calling : ",sum)

x = "global"

def modify_global():
    global x
    print ("Before modification: ",x)
    x = "modified global"
    print ("After modification: ",x)
print(x)
modify_global()
print(x)
