#a function is a block of code which only runs when it called,in python we do not use curly brackets we use indentation with tabs

#create function
def sayHello(name='damian'):
    print(f'hello {name}')
    
#sayHello()

#return values
def getSum(num1,num2):
    total=num1+num2
    return total

print(getSum(234,257))

num=getSum(245,685)

print(num)

# A lambda function is a small anonymous function
#A lambda function can take any number of arguments,but can only have one expression.very similar to js arrow functions

getSum=lambda num1,num2 : num1+num2

print(getSum(789,5668))
