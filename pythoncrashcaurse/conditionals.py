#if/else conditions are used to decide based on something being true or false


x=50
y=50

#comparison operators (==,!=,>,<,=<,<=) used to compare values

#if simple if
#if x > y:
    #print(f'{x} is greater than {y}')
    
#if  else 
#if x > y:
    #print(f'{x} is greater than {y}')
#else:
    #print(f'{y} is greater than {x}')
    
#elif
#if x > y:
   # print(f'{x} is greater than {y}')
#elif x==y:
   # print(f'{x} is equal to {y}')
#else:
    #print(f'{y} is greater than {x}' )
    
# nested if else statement
#if x>2:
 #if x<=10:
    #print(f'{x} is greater than 2 or less than or equal to 10')
    
#logical operators (and ,or,not) = used to combine conditional statements
#and
##if x>2 and x<=10:
   # print(f'{x} is greater than 2 and less than or equal to 10')

#or
#if x>2 or x<=10:
    #3print(f'{x} is greater than 2 or less than or equal to 10')
    
#not
#if not(x==y):
    #print(f'{x} is not equal to {y}')
    
#membership operators (not, not in) membership operators is used to test if a sequence is presented into 

#not
#numbers = [1,2,3,4]

#if x in numbers:
    # print(x in numbers)

# in
#if x not in numbers:
    #print(x not in numbers)
    
# identity operators (is,is not) compare the objects, not if they are equal,but if they are actually the same object memory location

#is 
if x is y:
    print(x is y)

#is not
if x is not y:
    print(x is not y)
        