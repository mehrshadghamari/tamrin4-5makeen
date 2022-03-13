

def sedadarbiseda():  

    a=input()
    b=a.replace(" ","")
    vowel=0
    consonant=0
    for i in b:
        if i in ['a','e','i','o','u','A','E','I','O','U']:
            vowel+=1
        else:
            consonant+=1
    c={'vowel' : vowel ,  'consonant' : consonant}
    print(c)

sedadarbiseda()