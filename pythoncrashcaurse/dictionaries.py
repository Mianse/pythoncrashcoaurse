#a dictionary is a collection which is unordered,changeable indexed.No duplicate

#create dictionary

person={
    'first_name':'damian',
    'last_name':'orina',
    'age': 30
}
#use constructor
#person2= dict(first_name='william',last_name='saliba',age=23)


#print(person2,type(person2))
print(person,type(person));

#access a single value
print(person['first_name'])

print(person.get('last_name'))

#add key/value

person['phone']='0703449305'

#
# print(person)
# get Keys

print(person.keys())

print(person.items())

person2=person.copy()

person2['city']='carlifornia'

print(person2)

del(person['age'])
person.pop('phone')

person.clear()

#get length
print(len(person2))

print(person)

#list of dictionaries
people=[
    {'name':'Telkom','age':19},
    {'name':'Damian','age':23}
]

print(people)

print(people[1],['name'])
