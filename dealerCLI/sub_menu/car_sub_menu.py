import colorama
from function_menu_helper.func_menu_car import (
    list_cars,
    create_car,
    find_car_by_id,
    find_car_by_model,
    update_car,
    delete_car,
    car_factories
)

def car_menu_print():
    print('')
    print('')
    print(colorama.Fore.BLUE +'--------------------Car Menu----------------------'+ colorama.Style.RESET_ALL )
    print('')
    print(colorama.Fore.BLUE + "0. Back to Main Menu"+ colorama.Style.RESET_ALL)
    print(colorama.Fore.BLUE +"1. List all cars"+ colorama.Style.RESET_ALL)
    print(colorama.Fore.BLUE +"2. Create a new car"+ colorama.Style.RESET_ALL)
    print(colorama.Fore.BLUE +"3. Find a car by id"+ colorama.Style.RESET_ALL)
    print(colorama.Fore.BLUE +"4. Find a car by model"+ colorama.Style.RESET_ALL)
    print(colorama.Fore.BLUE +"5. Update a car"+ colorama.Style.RESET_ALL)
    print(colorama.Fore.BLUE +"6. Delete a car"+ colorama.Style.RESET_ALL)
    print(colorama.Fore.BLUE +"7. See car's factory"+ colorama.Style.RESET_ALL)

def car_menu():
    while True:
        car_menu_print()
        choice = input("> ")

        if choice == "0":
            break

        elif choice == "1":
            print('')
            list_cars()

        elif choice == "2":
            print('')
            create_car()
            
            while True:
                print(colorama.Fore.BLUE +"Do you want to create another? "+ colorama.Style.RESET_ALL)
                print(colorama.Fore.BLUE +"0. No"+ colorama.Style.RESET_ALL)
                print(colorama.Fore.BLUE +"1. Yes"+ colorama.Style.RESET_ALL)
                choice = input("> ")
                
                if choice == "0":
                    break
                elif choice == "1":
                    print('')
                    create_car()
                else: print(colorama.Fore.BLUE +"Invalid choice!"+ colorama.Style.RESET_ALL)

        elif choice == "3":
            print('')
            find_car_by_id()
            
            while True:
                print(colorama.Fore.BLUE +"Do you want to find another? "+ colorama.Style.RESET_ALL)
                print(colorama.Fore.BLUE +"0. No"+ colorama.Style.RESET_ALL)
                print(colorama.Fore.BLUE +"1. Yes"+ colorama.Style.RESET_ALL)
                choice = input("> ")
                
                if choice == "0":
                    break
                elif choice == "1":
                    print('')
                    find_car_by_id()
                else: print(colorama.Fore.BLUE +"Invalid choice!"+ colorama.Style.RESET_ALL)

        elif choice == "4":
            print('')
            find_car_by_model()
            
            while True:
                print(colorama.Fore.BLUE +"Do you want to find another? "+ colorama.Style.RESET_ALL)
                print(colorama.Fore.BLUE +"0. No"+ colorama.Style.RESET_ALL)
                print(colorama.Fore.BLUE +"1. Yes"+ colorama.Style.RESET_ALL)
                choice = input("> ")
                
                if choice == "0":
                    break
                elif choice == "1":
                    print('')
                    find_car_by_model()
                else: print(colorama.Fore.BLUE +"Invalid choice!"+ colorama.Style.RESET_ALL)

        elif choice == "5":
            print('')
            update_car()
            
            while True:
                print(colorama.Fore.BLUE +"Do you want to update another? "+ colorama.Style.RESET_ALL)
                print(colorama.Fore.BLUE +"0. No"+ colorama.Style.RESET_ALL)
                print(colorama.Fore.BLUE +"1. Yes"+ colorama.Style.RESET_ALL)
                choice = input("> ")
                
                if choice == "0":
                    break
                elif choice == "1":
                    print('')
                    update_car()
                else: print(colorama.Fore.BLUE +"Invalid choice!"+ colorama.Style.RESET_ALL)

        elif choice == "6":
            print('')
            delete_car()
            
            while True:
                print(colorama.Fore.BLUE +"Do you want to delete another? "+ colorama.Style.RESET_ALL)
                print(colorama.Fore.BLUE +"0. No"+ colorama.Style.RESET_ALL)
                print(colorama.Fore.BLUE +"1. Yes"+ colorama.Style.RESET_ALL)
                choice = input("> ")
                
                if choice == "0":
                    break
                elif choice == "1":
                    print('')
                    delete_car()
                else: print(colorama.Fore.BLUE +"Invalid choice!"+ colorama.Style.RESET_ALL)
        
        elif choice == "7":
            print('')
            car_factories()
            while True:
                print(colorama.Fore.BLUE +"Do you want to check another car's factory? "+ colorama.Style.RESET_ALL)
                print(colorama.Fore.BLUE +"0. No"+ colorama.Style.RESET_ALL)
                print(colorama.Fore.BLUE +"1. Yes"+ colorama.Style.RESET_ALL)
                choice = input("> ")
                
                if choice == "0":
                    break
                elif choice == "1":
                    print('')
                    car_factories()
                else: print(colorama.Fore.BLUE +"Invalid choice!"+ colorama.Style.RESET_ALL)

        else: print(colorama.Fore.BLUE +"Invalid choice!"+ colorama.Style.RESET_ALL)