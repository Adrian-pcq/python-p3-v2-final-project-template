from lib.function_menu_helper.func_menu_car import (
    list_cars,
    create_car,
    find_car_by_id,
    find_car_by_model,
    update_car,
    delete_car,
)


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
                    delete_car()
                else: print("Invalid choice!")
        
        else: print("Invalid choice!")