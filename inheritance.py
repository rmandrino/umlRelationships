# Parent class
class Animal:
    def eat(self):
        print("Animal is eating")


# Child class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")


# Main program
dog = Dog()

dog.eat()   # Inherited method
dog.bark()