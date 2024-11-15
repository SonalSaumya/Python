'''

#Siddhi
contact = {}

total = int(input("Enter no of contact you want to add : "))
try:
    for i in range(total):
        id = int(input("Enter ID : "))
        value = {}

        name = input("Enter name : ")
        no = list(input("Enter no : ").split(","))
        email = input("Enter email :")

        value['name'] = name
        value['no'] = no
        value['email'] = email

        contact[id] = value

except:
    print("Invalid input")



print("=========================")
print("Contact details")
for i in contact:
    print(i,"==",contact[i])

'''

#========================================================================
#Siddhi
contact = {}
def add_contact():
    id = int(input("Enter ID : "))
    value = {}

    name = input("Enter name : ")
    no = list(input("Enter no : ").split(","))
    email = input("Enter email :")

    value['name'] = name
    value['no'] = no
    value['email'] = email

    contact[id] = value

def add_to_file():
    with open('contact.txt','w') as file:
        file.write(str(contact))
    file.close()


#incomplete code
def update_details():
    uid = int(input("Enter id to updates : "))
    detail = input()


while True:
    choice = input("Enter choice : ")

    if choice == "add":
        add_contact()
    if choice == "add to file":
        add_to_file()
    if choice == "update details":
        update_details()

