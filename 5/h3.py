def caculat(num1,num2,Arithmetic):
    if Arithmetic=='+':
        print(num1+num2)
    elif Arithmetic=='-':
        print(num1-num2)
    elif Arithmetic=='*':
         print(num1*num2)
    elif Arithmetic=='/':
        print(num1/num2)

a=int(input('enter number '))
b=int(input('enter number '))
c=input('enter Arithmetic ')
caculat(a,b,c)