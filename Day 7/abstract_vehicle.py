from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")

    def stop(self):
        print("car stopped")


class Bike(Vehicle):
    def start(self):
        print("Bike started")

    def stop(self):
        print("Bike stopped")


class Bus(Vehicle):
    def start(self):
        print("Bus started")

    def stop(self):
        print("Bus stopped")


class Garage:

    vehicle_list=[]
    def add_vehicles(self,*args):
        Garage.vehicle_list.append(args)

    def operate(self,obj):
        obj.start()
        obj.stop()


cr1 = Car()
bk1 = Bike()
bs1 = Bus()

g1 = Garage()

g1.add_vehicles(cr1,bk1,bs1)

for i in Garage.vehicle_list[0]:
    g1.operate(i)
    print("_____________________")
    #g1.operate(i)
    # print(i)
    # print(len(Garage.vehicle_list[0]))

#print(len(Garage.vehicle_list))


