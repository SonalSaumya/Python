def open_file(filename):
    try:
        with open(filename,'r') as file:
            data = file.read()
        print(data)
        file.close()
    except FileNotFoundError:
        print("File not found error")


open_file('extra_scores.csv')
open_file('xyz.csv')

