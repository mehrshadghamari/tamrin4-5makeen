from random import sample


sampledict={
    'class': {
        'student':{
            'name':'mike' ,
            'marks':{
                'physics':70,
                'history':80
            }
        }
    }
}

b=sampledict['class']['student']['marks']['history']
print(b)
