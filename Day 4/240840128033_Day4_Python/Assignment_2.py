scores = {'Alice': 85 , 'Bob':92,'Charlie':65}

'''
for i in scores:
    if scores[i] > 80:
        #print(scores[i])
        scores[i] = int(scores[i])+5

print(scores)

'''
#using list comprehension

new_scores = {i : scores[i]+5 for i in scores if scores[i] > 80}
print(new_scores)
