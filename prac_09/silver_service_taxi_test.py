"""CP1404 Practical - Code to test SilverServiceTaxi class."""

from prac_09.silver_service_taxi import SilverServiceTaxi

my_taxi = SilverServiceTaxi("Vroom Vroom", 100, 2)
my_taxi.drive(18)
print(my_taxi)
print(f"Total fare = ${my_taxi.get_fare()}")
