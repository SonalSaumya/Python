

from abc import ABC,abstractmethod

class SmartDevice(ABC):

    def __init__(self):
        _name = ""
        _status = ""



    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class SmartLight(SmartDevice):

    def __init__(self):
        super().__init__()
    def turn_on(self):
        self.status= "ON"
        print(f"Smart light is now {self.status}")

    def turn_off(self):
        self.status = "OFF"
        print(f"Smart light is now {self.status}")

    def device_info(self):
        self.name = input("Enter light name : ")
        print(f"Light name : {self.name}\t Status : {self.status}")

    def set_brightness(self):
        level = int(input("Enter brightness level : "))
        print(f"Brightness set to {level}%.")



class SmartThermostat(SmartDevice):
    def __init__(self):
        super().__init__()
    def turn_on(self):
        self.status= "ON"
        print(f"Smart light is now {self.status}")

    def turn_off(self):
        self.status = "OFF"
        print(f"Smart light is now {self.status}")

    def device_info(self):
        self.name = input("Enter light name : ")
        print(f"Light name : {self.name}\t Status : {self.status}")

    def set_brightness(self):
        level = int(input("Enter brightness level : "))
        print(f"Brightness set to {level}%.")



l1 = SmartLight()
l1.turn_off()
l1.turn_on()
l1.device_info()
l1.set_brightness()

'''

from abc import ABC, abstractmethod
class SmartDevice(ABC):
    def __init__(self):
      _name= ""
      _status= ""

    @abstractmethod
    def turn_on(self):
     pass

    @abstractmethod
    def turn_off(self):
        pass

class SmartLight(SmartDevice):

    def __init__(self):
        super().__init__()
    def turn_on(self):
        self.status = "ON"
        print(f"Smart Light is now {self.status}")


    def turn_off(self):
        self.status = "OFF"
        print(f"Smart Light is now {self.status}")

    def set_brightness(self):
        level= int(input("Enter brightness level ; "))
        print(f"Brightness set to {level}%")

    

l1 = SmartLight()
l1.turn_off()
l1.turn_on()
#l1.device_info()
l1.set_brightness()
'''