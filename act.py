from abc import ABC

class Animal(ABC):

    def  move(self):
        pass
class Human(Animal):
        def move(self):
            print("i am inteligent")

class Snake(Animal):
                def move(self):
                    print("i have no legs")


 
class Dog(Animal):
                def move(self):
                    print("i can run faster than human")

class LIon(Animal):
                def move(self):
                        print("i kill animals")
r=Human()
r.move()

r=Snake()
r.move()

r=Dog()
r.move()
r=LIon()
r.move()