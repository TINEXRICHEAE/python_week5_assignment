# Defining a base class
class Vehicle:
    def __init__(self, brand, speed):
        self._brand = brand  # Encapsulation (protected attribute)
        self._speed = speed

    def move(self):
        print(f"The {self._brand} vehicle is moving at {self._speed} km/h.")

# Defining derived classes to explore inheritance and polymorphism


class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)  # Initialize parent class attributes
        self.fuel_type = fuel_type  # Unique attribute for Car

    def move(self):  # Polymorphism
        print(
            f"The {self._brand} car is driving at {self._speed} km/h, using {self.fuel_type} fuel.")


class Plane(Vehicle):
    def __init__(self, brand, speed, altitude):
        super().__init__(brand, speed)
        self.altitude = altitude  # Unique attribute for Plane

    def move(self):  # Polymorphism
        print(
            f"The {self._brand} plane is flying at {self._speed} km/h, at an altitude of {self.altitude} feet.")


class Bicycle(Vehicle):
    def __init__(self, brand, speed, gear_count):
        super().__init__(brand, speed)
        self.gear_count = gear_count  # Unique attribute for Bicycle

    def move(self):  # Polymorphism
        print(
            f"The {self._brand} bicycle is pedaling at {self._speed} km/h, with {self.gear_count} gears.")

# Demonstrating the functionality


def main():
    # Create instances of each class
    car = Car("Toyota", 120, "Petrol")
    plane = Plane("Boeing", 900, 35000)
    bicycle = Bicycle("Giant", 25, 21)

    # Calling the move() method to show polymorphism
    car.move()
    plane.move()
    bicycle.move()


if __name__ == "__main__":
    main()
