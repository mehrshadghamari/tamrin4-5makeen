def removeDupDic():


    a={'1':1,'2':2,'3':3,'4':4,'5':5,'6':5}
    b={}
    for k ,v in a.items():
        if v not in b.values():
         b[k]=v
    print(b)

removeDupDic()