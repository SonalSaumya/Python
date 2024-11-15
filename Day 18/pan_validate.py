import re
def validate_pan(pan):
    pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'
    if re.match(pattern,pan):
        return True
    else:
        return

pan_no = input("Enter the PAN No to validate: ")

if validate_pan(pan_no):
    print(f"{pan_no} is a valid PAN No")

else:
    print(f"{pan_no} is not a valid PAN No")

