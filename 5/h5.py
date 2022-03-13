
def upstr(str1):
    c=''
    for i in str1:
        if (i.islower()):
            b=i.upper()
            c+=b    
        elif (i.isupper()):
            print('false')
            break
    print(c) 
a=input('enter word ')

upstr(a)

       