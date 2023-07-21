s = {1,2,3,4,4}
print(s)
type(s)
s.add(7)
print(s)
fs =frozenset(s)
type(fs)
print(fs)
#
'''
d={1:'siri',2:'venky',3:'raj'}
print(d)
type(d)


a,b=10,20
x=30 if a<b else 100
print(x)
'''

#a=int(input("enter first number: ") )
#b=int(input("enter second number: "))
#min=b if b<a else a
#print(min)

#
def m():
    a=int(input("enter first number: ") )
    b=int(input("enter second number: "))
    n=b if b<a else a
    return n

 

import math
print(math.sqrt(16))
print(math.pi)