'''class Democlass:
    x = 5;
    def add(a, b):
        return a+b
#def add(a, b):
    #return a+b
obj =  Democlass ()
print (obj.x)
print (obj.add(5,2))
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def myfunc(self):
        print ("My name is " + self.name)
p1 = Person("Jhon", 36)
p1.myfunc()
