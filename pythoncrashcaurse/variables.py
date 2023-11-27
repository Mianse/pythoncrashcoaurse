'''
container that consist values
'''
"""
variables are case sensitive
(name and Name are different variables)
can have numbers but cannot start with one
"""

from xmlrpc.client import boolean


#x=1 #int
#y=2.5 #float
#name="john" #string
#is_cool= True #boolean

#multiple assignment
x,y,name,is_cool=(1,2.5,'JOHN',True)

print('hello')

print(x,y,name,is_cool)

a=x+y

print(a)
x=str(x)
y=int(y)

print(type(x))

z=float(y)

print(type(z),z)
print(type(y),y)

