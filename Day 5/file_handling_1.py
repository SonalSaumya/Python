def write_to_file(file,data):
    with open(file,'w') as file:
        file.write(data)

def read_from_file(filename):
    content = ""
    try:
        with open(filename,'r') as file :
            content += file.read()
            print(content)

        for i in range(len(content)):
            if content[i] == "after":
                print("before")
                content[i]="before"
                #file.write(content[i])
                #write_to_file("report.txt", )

    except FileNotFoundError:
        print('File not found ')

read_from_file("new_report.txt")
