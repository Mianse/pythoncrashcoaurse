# a list is a collection which is ordered  in a changeable.allow duplicate numbers

#create list
numbers =[1,2,3,4,5,6]

fruits=['apples','oranges','grapes','Pears']
# use constructor
numbers2= list((1,2,3,4,5,6))

print(numbers,numbers2)

#get value from a list

print(fruits[2])

print(len(fruits[3]))

#Append to list

fruits.append('mangoes')

print(fruits)

fruits.remove('grapes')

print(fruits)

#insert into position
fruits.insert(2,'strawberry')

print(fruits)

#remove  with pop
fruits.pop(2)

#reverse
fruits.reverse()

print(fruits)

#sort list

fruits.sort()

print(fruits)

#reverse sort
fruits.sort(reverse=True)

print(fruits)

#change value

fruits[1]='blueberries'

print(fruits)