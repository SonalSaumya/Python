class Car:
    no_of_cars = 0

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        Car.no_of_cars +=1

    @classmethod
    def get_no_of_cars(cls):
        return f"Total no.of cars : {cls.no_of_cars}"


c1 = Car("ABC","XYZ")

print(c1.no_of_cars)
print(c1.get_no_of_cars())
print(c1.get_no_of_cars())

c2 = Car("ABC","XYZ")

print(c1.no_of_cars)
print(c1.get_no_of_cars())
print(c1.get_no_of_cars())



