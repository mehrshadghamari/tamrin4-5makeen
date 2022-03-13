from multiprocessing.sharedctypes import Value
from unittest import result
scores={
    'alireza':{'riazi':20,'tarikh':19,'arabi':11},
    'peyman':{'riazi':15,'tarikh':17,'arabi':16}

}
a=0
for i,j in scores['alireza'].items():
    a+=j
alirezaAVR=a/3

b=0
for k,z in scores['peyman'].items():
    b+=z
peymanAVR=b/3

res={'alireza': ''  , 'peyman':  '' }
res['alireza']=alirezaAVR
res['peyman']=peymanAVR
print(res)