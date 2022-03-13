b=[7,10,71,2,2,3,3,3,6,38,38,38,39,40,40,40,1,3,39]
res=[]
for index in b:
    if index not in res:
        res.append(index)

print(res)
