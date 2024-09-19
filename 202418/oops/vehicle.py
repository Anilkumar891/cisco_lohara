from abc import ABC,abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        return "car starts"


class Bike(Vehicle):
    def start(self):
        return "bike starts"
    

car = Car()
bike = Bike()
print(car.start())  # Output: Car starts.
print(bike.start())  # Output: Bike starts.   
