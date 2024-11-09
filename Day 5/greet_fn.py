# def sum_numbers(*args):
#     sum = 0
#     for i in args:
#         if i >0:
#             sum= sum+i
#
#     return sum
#
#
# print(sum_numbers(1,2,3,-4,5,-5))

def sum_number(*args):
    sum=0
    for i in args:
        if i>0:
            sum=sum+i

    return sum

print(sum_number(1,2,3,-5,-6))

