

def remove_duplicates(name):
    new_str=""
    
    if name=="":
        return "Empty string"
    else:
        for i in name:
            if i not in new_str:
                new_str+=i
        return new_str

if __name__ == '__main__':
    name = str(input("Enter string :"))
    print(remove_duplicates(name))
