class Animal:
    def __init__(self,name):
        self.name= name

    def sound(self):
        print(f"{self.name}makes a sound.")

class Dog(Animal):
    def sound(self):
        print(f"{self.name} barks.")

dog= Dog("Buddy")
dog.sound()                