"""
CP1404 Practical - Client code to use the Car class.
"""

from prac_06.car import Car


def main():
    """Test code to use Car class."""
    my_car = Car(180, "Astra")
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)
    limo = Car(100, "limo")
    limo.add_fuel(20)
    print(f"Car has fuel: {limo.fuel}")
    limo.drive(115)
    print(limo)


main()
