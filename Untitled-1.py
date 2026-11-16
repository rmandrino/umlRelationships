import ABC from abstract

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

  def study(self):
    print(self.name, "is studying")
  

  def role(self):
    print(self.name, "is a student")
  
person1 = Person("Lina", 20)

print(person1.name)
print(person1.get_age())
person1.study()
person1.role()
print()

class Teacher(Person):
    def teach (self):
        print(self.name, "is teaching")
    def role(self):
      print(self.name, "is a teacher")

person2 = Teacher("Mona", 30)

print(person2.name)
print(person2.get_age())
person2.teach()
person2.role()