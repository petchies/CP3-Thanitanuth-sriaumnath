class Vehicle:
    licenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")

class Car(Vehicle):
    def sayHello(self):
        print("Meng Hao")
    pass
class PickUp(Vehicle):
    pass
class Van(Vehicle):
    pass
class Estatecar(Vehicle):
    pass

car1 = Car()
car1.turnOnAirConditioner()
car1.sayHello()
pickUp1 = PickUp()
pickUp1.turnOnAirConditioner()
van1 = Van()
van1.turnOnAirConditioner()
estatecar1 = Estatecar()
estatecar1.turnOnAirConditioner()