import re
#
# with open('text.txt','r') as file :
#     text = file.read()
#
# #print(text)
#
# #date = r'[0-9]+/[0-12][0-9]{4}'
# # date = r'[0-30]?/[0-12]?/[0-9]{4}'
# # 16/02/2002
# # date = r'[1-31]/[1-12]/[0-9]{4}'
# date = []
#
#
# result =  re.findall(date,text)
# print(result)

text = "Today's date is 16/12/2024., 12/12/2024/ 12323/05/2024"

# date = r'\\w\w\d{2}/\d{2}/\d{4}'

# date = r'\b[0-3][1-9]\/[0-1][1-2]\/\d{4}\b]'

match = re.search(date, text)
print(match)


text = "plsaskmeanything"

match = re.sub('ask','tell',text)
print(match)



