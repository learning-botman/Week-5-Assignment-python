class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚴")

vehicles = [Car(), Plane(), Bicycle()]

for v in vehicles:
    v.move()  # Polymorphism: same method name, different behavior
