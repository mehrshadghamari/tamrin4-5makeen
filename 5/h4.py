def DivisibleNum (num):
    if num%15==0:
        print('feezbuzz')
    elif num%3==0:
        print('feez')
    elif num%5==0:
        print('buzz')
    else:
        print('not divisible to 3 or 5 or 3 and 5')

t=int(input('enter a number '))

DivisibleNum(t)