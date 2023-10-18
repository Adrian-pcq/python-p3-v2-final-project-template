from lib.function_menu_helper.func_menu_factory import (
    list_factories,
    create_factory,
    find_factory_by_id,
    find_factory_by_name,
    update_factory,
    delete_factory,
    factory_car
)

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

        else: print("Invalid choice!")