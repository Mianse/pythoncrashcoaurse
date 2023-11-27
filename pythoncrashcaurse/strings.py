name='Damian'
Age=25


#concatenate
print('hello my name is ' +name)

#print('my name is '+name+'and i am' +str(Age)+' years old')


#string formatting

#Arguments by position
#print('my name is {name} and i am {Age}'.format(name=name,Age=Age))

#F-strings 
print(f'my name is {name} and i am{Age}')


#string methods

s="hello world"

#capitalize string

print(s.capitalize())

#uppercase
print(s.upper())

#lowercase

print(s.lower())

#swap case
print(s.swapcase())

#replace
print(s.replace('world','everyone'))

# count
sub='h'

print(s.count(sub))

#starts with
print(s.startswith('tommylee'))

#endswith
print(s.endswith('sparta'))

#split into a list

print(s.split())

#find position

print(s.find('s'))

#is all alpha numeric
print(s.isalnum())

#is all alphabetic
print(s.isalpha())

#is all numeric

print(s.isnumeric())

