
from func_menu_factory import (
    list_factories,
    create_factory,
    find_factory_by_id,
    find_factory_by_name,
    update_factory,
    delete_factory,
    factory_car
)

from func_menu_car import (
    list_cars,
    create_car,
    find_car_by_id,
    find_car_by_model,
    update_car,
    delete_car
)


def main():
    print(" ")
    print(" ")
    print("         Welcome to the Dealer CLI!!!")
    print("   ----------------------------------------- ")
    print("  |  HH                                 HH  |")
    print("  |  HHH                               HHH  |")
    print("  |  HHHH                             HHHH  |")
    print("  |   HHHH                           HHHH   |")
    print("  |   HHHHH                         HHHHH   |")
    print("  |    HHHHHH                     HHHHHH    |")
    print("  |    HHHHHHH                   HHHHHHH    |")
    print("  |     HHHHHHHH               HHHHHHHH     |")
    print("  |     HHHHHHHHH             HHHHHHHHH     |")
    print("  |     HHHHHHHHHHHhhhhhhhhhHHHHHHHHHHH     |")
    print("  |     HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH     |")
    print("  |      HHHHHHH               HHHHHHH      |")
    print("  |      HHHHHH                 HHHHHH      |")
    print("  |      HHHHH                   HHHHH      |")
    print("   ----------------------------------------- ")


    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            print("")
            print("")
            print("         I hope you enjoyed it a lot!!!")
            print("")
            print("")
            print(" BBBBBBBBBBB    YYY       YYY   EEEEEEEEEE   !!!!!!! ")
            print(" BBB    BBBB     YYY     YYY    EEEEEEEEEE   !!!!!!! ")
            print(" BBBBBBBBBBB      YYY   YYY     EEE           !!!!!  ")
            print(" BBB               YYYYYYY      EEEEEEEEEE     !!!   ")
            print(" BBBBBBBBBBB         YYY        EEE                  ")
            print(" BBB    BBBB         YYY        EEEEEEEEEE     !!!   ")
            print(" BBBBBBBBBBB         YYY        EEEEEEEEEE     !!!   ")
            print("")
            print("")
            exit()
        
        elif choice == "1":
              factory_menu()

        elif choice == "2":
              car_menu()
 
        else:
            print("Invalid choice!")


def menu():
        print("Please select an option:")
        print("0. Exit the program")
        print("1. Factory Menu")
        print("2. Car Menu")

def factory_menu_print():
    print("0. Back to Main Menu")
    print("1. List all the factories")
    print("2. Create a new factory")
    print("3. Find a factory by id")
    print("4. Find a factory by name")
    print("5. Update a factory")
    print("6. Delete a factory")
    print("7. See factory's cars")
     
def factory_menu():
    while True:
        factory_menu_print()
        choice = input("> ")
        if choice == "0":
             break 

        elif choice == "1":
            list_factories()
        
        elif choice == "2":
            create_factory()
            while True:
                print("Do you want to create another?")
                print("0. No")
                print("1. Yes")
                choice = input("> ")
                if choice == "0":
                    break
                elif choice == "1":
                    create_factory()
                else: print("Invalid choice!")

        elif choice == "3":
            find_factory_by_id()
            while True:
                print("Do you want to find another?")
                print("0. No")
                print("1. Yes")
                choice = input("> ")
                if choice == "0":
                    break
                elif choice == "1":
                    find_factory_by_id()
                else: print("Invalid choice!")

        elif choice == "4":
            find_factory_by_name()
            while True:
                print("Do you want to find another?")
                print("0. No")
                print("1. Yes")
                choice = input("> ")
                if choice == "0":
                    break
                elif choice == "1":
                    find_factory_by_name()
                else: print("Invalid choice!")

        elif choice == "5":
            update_factory()
            while True:
                print("Do you want to update another?")
                print("0. No")
                print("1. Yes")
                choice = input("> ")
                if choice == "0":
                    break
                elif choice == "1":
                    update_factory()
                else: print("Invalid choice!")

        elif choice == "6":
            delete_factory()
            while True:
                print("Do you want to delete another?")
                print("0. No")
                print("1. Yes")
                choice = input("> ")
                if choice == "0":
                    break
                elif choice == "1":
                    delete_factory()
                else: print("Invalid choice!")

        elif choice == "7":
            factory_car()

        else:
             print("Invalid choice!")
    

def car_menu_print():
    print("0. Back to Main Menu")
    print("1. List all cars")
    print("2. Create a new car")
    print("3. Find a car by id")
    print("4. Find a car by model")
    print("5. Update a car")
    print("6. Delete a car")

def car_menu():
    while True:
        car_menu_print()
        choice = input("> ")

        if choice == "0":
            break

        elif choice == "1":
            list_cars()

        elif choice == "2":
            create_car()
            while True:
                print("Do you want to create another: ")
                print("0. No")
                print("1. Yes")
                choice = input("> ")
                if choice == "0":
                    break
                elif choice == "1":
                    create_car()
                else: print("Invalid choice!")

        elif choice == "3":
            find_car_by_id()
            while True:
                print("Do you want to find another: ")
                print("0. No")
                print("1. Yes")
                choice = input("> ")
                if choice == "0":
                    break
                elif choice == "1":
                    find_car_by_id()
                else: print("Invalid choice!")

        elif choice == "4":
            find_car_by_model()
            while True:
                print("Do you want to find another: ")
                print("0. No")
                print("1. Yes")
                choice = input("> ")
                if choice == "0":
                    break
                elif choice == "1":
                    find_car_by_model()
                else: print("Invalid choice!")

        elif choice == "5":
            update_car()
            while True:
                print("Do you want to update another: ")
                print("0. No")
                print("1. Yes")
                choice = input("> ")
                if choice == "0":
                    break
                elif choice == "1":
                    update_car()
                else: print("Invalid choice!")

        elif choice == "6":
            delete_car()
            while True:
                print("Do you want to delete another: ")
                print("0. No")
                print("1. Yes")
                choice = input("> ")
                if choice == "0":
                    break
                elif choice == "1":
                    update_car()
                else: print("Invalid choice!")
        
        else: print("Invalid choice!")



    


if __name__ == "__main__":
    main()
