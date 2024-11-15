
import re

text = "2024-09-21T15:30:00 and 12334 dfbn:553:653655: 5:52:"
pattern = r'\d{4}-\d{2}-\d{2}Td\d{2}:\{2}:\d{2}'

result = re.findall(pattern,text)
new_pat = r'date=\d{4}-\d{2}-\d{2} time=d\d{2}:\{2}:\d{2}'

new_text = re.sub(pattern,new_pat,text)
print(result)
print(new_text)

