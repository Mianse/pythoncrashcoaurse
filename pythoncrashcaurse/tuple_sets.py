#a tuple is a collection  which is ordered and unchangeable

#create tuple
fruits= ('apples','oranges','grapes')
#fruits2= tuple(('apples','oranges','grapes'))

fruits2 = ('apples',)

print(fruits2,type(fruits2))

#SINGLE VALUE TRAILING COMMAND
print(fruits2,type(fruits2))

print(fruits[1])
#cant change value

#delete tuple
del fruits2
#print(fruits2)

#length in tuple

print(len(fruits))

#a set is a collection which is unordered or un indexed .no duplicate numbers

#create set
fruit_set={'Apples','Oranges','Grapes'}

#check if in set
print('Apples' in fruit_set)

#add to set
fruit_set.add('strawberry')

print(fruit_set)

#remove

fruit_set.remove('strawberry')
print(fruit_set)

#clear set
#print(fruit_set.clear())

#add duplicate set
print(fruit_set.add('Apples'))