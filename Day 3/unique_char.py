
para = input("Enter : ")

words = list(x for x in para.split())

let = []

for i in range(len(words)):
    for j in range(len(words[i])):
        let.append(words[i][j])

let = sorted(set(let))
#print(sorted(let))

letters=""
for i in let:
    letters+=i

print(letters)






'''

text= input("Enter a paragraph of text : ")
words= text.split()
unique_words = set(words)
sorted_words = sorted(unique_words)
print("\n Unique Words :")
for words in sorted_words:
    print(words)
    
    '''
