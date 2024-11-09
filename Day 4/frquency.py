
#Siddhi
nums = list(input("Enter list of elements : ").split(","))
dict={}

for i in nums:
    cnt = 0
    for j in nums:
        if j==i:
            cnt=cnt+1

        dict[i]=cnt
print("Original List:",nums)

print("Frequency : ",dict)




#
# nums = list(input("Enter the required elements : ").split(","))
# dict = {}
#
# for i in nums:
#     count=0
#     for j in nums:
#         if j==i:
#             count=count+1
#             dict[i]=count
#
#
#
# print("keys&values", dict)