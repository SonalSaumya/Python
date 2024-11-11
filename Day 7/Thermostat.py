from abc import ABC, abstractmethod

class SmartDevice(ABC):
    def __init__(self, name):
        self.name = name
        self.status = 'off'

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def device_info(self):

class SmartThermostat(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.temperature = 22

    def turn_on(self):



