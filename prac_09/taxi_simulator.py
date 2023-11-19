from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU_PROMPT = "q)uit, c)hoose taxi, d)rive\n>>> "


def main():
    taxis = [Taxi("Taxi 1", 50), Taxi("Taxi 2", 100),
             SilverServiceTaxi("Fancy Taxi 1", 120, 2), SilverServiceTaxi("Fancy Taxi 2", 80, 3)]
    current_taxi = None
    total_bill = 0

    print(f"Let's drive!")
    menu_choice = input(MENU_PROMPT).lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
            current_taxi = get_valid_taxi(taxis, current_taxi)
        elif menu_choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                distance_to_drive = float(input("Drive how far? "))
                current_taxi.drive(distance_to_drive)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                total_bill += trip_cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        menu_choice = input(MENU_PROMPT).lower()
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {str(taxi)}")


def get_valid_taxi(taxis, current_taxi):
    is_valid_input = False
    while not is_valid_input:
        try:
            taxi_number = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_number]
            is_valid_input = True
        except ValueError:
            print("Input must be an integer")
    return current_taxi


def drive(current_taxi):
    print("You need to choose a taxi before you can drive")
    current_taxi.drive()


main()
