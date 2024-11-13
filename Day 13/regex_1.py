import re

text = "catatlog category mat cat mat sat cat sarcatwat CAT caT Cat cAt cat's"
pat = r'\b[c|C][a|A][t|T]\b'
match = re.findall(pat,text)
print(match)


text = "My phone number is 123-456-7890"
pat = r'\d'
match = re.findall(pat,text)
print(match)

text = "My number is 123, and my friend's number is 4567890. 215 365365 "
pat = r'\b[0-9]{3}\b'
match = re.findall(pat,text)
print(match)


text = "Error: File not found.\nWarning:Low disk space.\nError:Access denied."
pat = r'^Error.*\.'
match = re.findall(pat,text)
print(match)





