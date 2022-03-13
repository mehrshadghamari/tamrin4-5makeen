def evenOrOdd():

    a=[12,14,56,90,1,5,9]
    b=len(a)
    j=0
    z=0
    for i in a:
        if type(i)==str:
            print('please dont write string in list')
            break
        if i%2==0:
            j+=1
       
        if i%2!=0:
            z+=1
        if j==b:
            print('all even')
            break
        if z==b:
            print('all odd')
            break

    print(f' {j} even numbers and {z} odd numbers')

    
evenOrOdd()