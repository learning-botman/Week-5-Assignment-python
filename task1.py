# Base class
class Superhero:
    def __init__(self, name, power, universe):
        self.name = name
        self.power = power
        self.universe = universe

    def show_info(self):
        print(f"{self.name} is from {self.universe} and has the power of {self.power}.")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

# Subclass with Encapsulation
class FlyingHero(Superhero):
    def __init__(self, name, power, universe, max_altitude):
        super().__init__(name, power, universe)
        self.__max_altitude = max_altitude  # Encapsulated (private) attribute

    def fly(self):
        print(f"{self.name} is flying at an altitude of {self.__max_altitude} meters!")

    def get_altitude(self):
        return self.__max_altitude



hero1 = Superhero("ShadowMan", "Invisibility", "ShadowVerse")
hero2 = FlyingHero("SkyGirl", "Wind Control", "SkyVerse", 5000)

hero1.show_info()
hero1.use_power()

hero2.show_info()
hero2.use_power()
hero2.fly()
print("Max Altitude:", hero2.get_altitude())  # Accessing encapsulated data safely


