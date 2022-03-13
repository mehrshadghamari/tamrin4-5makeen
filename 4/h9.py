def kl():

    myList=[(),(2,3,4,),('a','b','c',),(),]
    print(f'my list befor change {myList}')
    for i in myList:
        if i==():
            myList.remove(i)
    print(f'my list after change {myList}')


kl()