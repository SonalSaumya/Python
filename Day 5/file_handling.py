def write_to_file(file,data):
    with open(file,'w') as file:
        file.write(data)

write_to_file("new_report.txt","sonal")

def read_from_file(filename):
    try:
        with open(filename,'r') as file :
            content = file.read()
            print(content)
    except FileNotFoundError:
        print('File not found ')

read_from_file("new_report.txt")

#
# def write_to_file(file,data)
#     with open


#
# def generate_report(title,*args,**kwargs):
#     return title
# def report(filename):
#     with open(filename,'w') as file :
#         title,args,kwargs= generate_report("Monthly sales Report","intro : overview","data analysis : breakdown","Market trends:Analysis", Author="John",Date="sept",Conclusion = "Ovreall")
#
#         file.write(title)
#         # file.write(args)
#         # file.write(kwargs)
#
#
# report("new_report.txt")