# for marshmallow eg:
class Person:
    def __init__(self,name,age):
      self.name=name
      self.age=age

# representation of it:

    def __repr__(self):
     return f'{self.name} is {self.age} yrs old.'

# to get input data we creating a dictonary
input_data={}
# input data for the name will be :
input_data['name']=input('what is your name? ')
input_data['age']=input('what is your age?')




person=Person(name=input_data['name'],age=input_data['age'])

print(person)