def loru():
    lowCounter=0
    upCounter=0
    a=input('enter a word or sentence ')
    
    for i in a:
        if (i.islower()):
            lowCounter+=1
        elif(i.isupper()):
            upCounter+=1
        else:
            continue
    print(f'lowercase = {lowCounter}and  upercase = {upCounter}')

loru()
