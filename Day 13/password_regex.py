import re

text = "abc1234 A1c3d4e5f1 a12 A1b@d5e9f6g a454 agfg8 A1c3d4e@5f1"
# pat = r'\b[a-z A-Z]\w{5,10}[0-9]\b'
pat = r'[a-z A-Z]\w\S{5,10}[0-9]'


match = re.findall(pat,text)
print(match)