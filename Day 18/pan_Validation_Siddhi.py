import re

pan = input("Enter PAN no : ")

pat = r'\b[A-Z]{5}\d{4}[A-Z]\b'  #or
pat = r'^[A-Z]{5}\d{4}[A-Z]$'

result = re.findall(pat,pan)

if result:
    print(result)
    print("Valid")
else:
    print("Not valid")