a={'k2':45.5,'k1':35,'k3':41.30,'k4':55,'k5':24}
b=dict(sorted(a.items(), key=lambda item: item[1],reverse=True))

c={}
i=0
for j,z in b.items():
    if i<3:
        c[j]=z
        i+=1
print(c)
