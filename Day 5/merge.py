def read_from_file(filename):
    try:
        with open(filename,'r') as file :
            content = file.read()
            print(content)
    except FileNotFoundError:
        print('File not found ')

read_from_file("file1.txt")

def read_from_file(filename):
    try:
        with open(filename,'r') as file :
            content = file.read()
            print(content)
    except FileNotFoundError:
        print('File not found ')

read_from_file("file2.txt")





