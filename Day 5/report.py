# def generate_report(title,*args,**kwargs):
#     return title, args, kwargs

'''
title , args ,kwargs = generate_report("Monthly sales Report","intro : overview","data analysis : breakdown","Market trends:Analysis", Author="John",Date="sept",Conclusion = "Ovreall")

print(title , args ,kwargs)

print(f"Report Title : {title}")
print("=====================================")


for i in kwargs:
    if i == "Conclusion":
        continue
    else:
        print(i ,":",kwargs[i])

print("\n")
print("Report Section : ")
print("----------------------")

for i in range (len(args)):
    if i%2 == 0 :
        print("section",i+1,":",args[i])

print("\n")
print("Conclusion : ")
print("-------------------------")
print(kwargs["Conclusion"])
'''
'''

title , args ,kwargs = generate_report("Monthly sales Report","intro : overview","data analysis : breakdown","Market trends:Analysis", Author="John",Date="sept",Conclusion = "Ovreall",skip =[2])

print(title , args ,kwargs)

print(f"Report Title : {title}")
print("=====================================")


for i in kwargs:
    if i == "Conclusion":
        continue
    else:
        print(i ,":",kwargs[i])

print("\n")
print("Report Section : ")
print("----------------------")

for i in range (len(args)):
    if i%2 == 0 :
        print("section",i+1,":",args[i])

print("\n")
print("Conclusion : ")
print("-------------------------")
print(kwargs["Conclusion"])

'''

# def write_to_file(filename,data):
#     with open(filename, 'w' ) as file:
#         file.write(data)
#
#         title, args, kwargs = generate_report("Monthly sales Report", "intro : overview", "data analysis : breakdown",
#                                               "Market trends:Analysis", Author="John", Date="sept",
#                                               Conclusion="Ovreall", skip=[2])
#
#         file.write(title, args, kwargs)
#
#         file.write(f"Report Title : {title}")
#         file.write("=====================================")
#
#         for i in kwargs:
#             if i == "Conclusion":
#                 continue
#             else:
#                 file.write(i, ":", kwargs[i])
#
#         file.write("\n")
#         file.write("Report Section : ")
#         file.write("----------------------")
#
#         for i in range(len(args)):
#             if i % 2 == 0:
#                 file.write("section", i + 1, ":", args[i])
#
#         file.write("\n")
#         file.write("Conclusion : ")
#         file.write("-------------------------")
#         file.write(kwargs["Conclusion"])
#
#     file.write("Succesful")
#
# #write_to_file("report.txt",generate_report("Monthly sales Report","intro : overview","data analysis : breakdown","Market trends:Analysis", Author="John",Date="sept",Conclusion = "Ovreall",skip =[2]))
#
#


def generate_report(title,*args,**kwargs):
    return title, args, kwargs
def write_to_file(file,data):
    with open(file,'w') as file:
        file.write(data)

        title, args, kwargs = generate_report("Monthly sales Report", "intro : overview", "data analysis : breakdown",
                                              "Market trends:Analysis", Author="John", Date="sept",
                                              Conclusion="Ovreall", skip=[2])
        file.write(title)




write_to_file("report.txt",)



