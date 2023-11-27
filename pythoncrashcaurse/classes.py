# a class is a blueprint for for creating objects.an object has properties and methods(functions) associated with it
#almost everything in python is an everything

#create a class
class user:
    
#constructor
  def __init__(self,name,email,age):
    self.name=name
    self.email=email
    self.age=age
    
def greeting(self):
    return f'my name is{self.name} and i am {self.age}'
        
# init user object
brad=user('Damian orina','damianorina17@gmail.com',25)

print(brad.greeting())
    
