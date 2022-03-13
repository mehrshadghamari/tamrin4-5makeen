scores={'alireza':[12,19,19,20],'arash':[20,19,18,18]}
a=0
for i in scores['alireza']:
    a+=i
b=len(scores['alireza'])
scores['alireza']=a/b

c=0
for j in scores['arash']:
    c+=j
d=len(scores['arash'])
scores['arash']=c/d

print(scores)
