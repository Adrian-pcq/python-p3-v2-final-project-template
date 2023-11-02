import colorama
from function_menu_helper.func_menu_factory import (
    list_factories,
    create_factory,
    find_factory_by_id,
    find_factory_by_name,
    update_factory,
    delete_factory,
    factory_car
)

def factory_menu_print():
    print('')
    print('')
    print(colorama.Fore.GREEN +"------------------- Factory Menu ------------------"+ colorama.Style.RESET_ALL)
    print('')
    print(colorama.Fore.GREEN +"0. Back to Main Menu"+ colorama.Style.RESET_ALL)
    print(colorama.Fore.GREEN +"1. List all the factories"+ colorama.Style.RESET_ALL)
    print(colorama.Fore.GREEN +"2. Create a new factory"+ colorama.Style.RESET_ALL)
    print(colorama.Fore.GREEN +"3. Find a factory by id"+ colorama.Style.RESET_ALL)
    print(colorama.Fore.GREEN +"4. Find a factory by name"+ colorama.Style.RESET_ALL)
    print(colorama.Fore.GREEN +"5. Update a factory"+ colorama.Style.RESET_ALL)
    print(colorama.Fore.GREEN +"6. Delete a factory"+ colorama.Style.RESET_ALL)
    print(colorama.Fore.GREEN +"7. See factory's cars"+ colorama.Style.RESET_ALL)

def factory_menu():
    while True:
        factory_menu_print()
        choice = input("> ")
        
        if choice == "0":
             break 

        elif choice == "1":
            print('')
            list_factories()
        
        elif choice == "2":
            print('')
            create_factory()
            while True:
                print(colorama.Fore.GREEN +"Do you want to create another?"+ colorama.Style.RESET_ALL)
                print(colorama.Fore.GREEN +"0. No"+ colorama.Style.RESET_ALL)
                print(colorama.Fore.GREEN +"1. Yes"+ colorama.Style.RESET_ALL)
                choice = input("> ")
                
                if choice == "0":
                    break
                elif choice == "1":
                    print('')
                    create_factory()
                else: print(colorama.Fore.GREEN +"Invalid choice!"+ colorama.Style.RESET_ALL)

        elif choice == "3":
            print('')
            find_factory_by_id()
            while True:
                print(colorama.Fore.GREEN +"Do you want to find another?"+ colorama.Style.RESET_ALL)
                print(colorama.Fore.GREEN +"0. No"+ colorama.Style.RESET_ALL)
                print(colorama.Fore.GREEN +"1. Yes"+ colorama.Style.RESET_ALL)
                choice = input("> ")
                
                if choice == "0":
                    break
                elif choice == "1":
                    print('')
                    find_factory_by_id()
                else: print(colorama.Fore.GREEN +"Invalid choice!"+ colorama.Style.RESET_ALL)

        elif choice == "4":
            print('')
            find_factory_by_name()
            while True:
                print(colorama.Fore.GREEN +"Do you want to find another?"+ colorama.Style.RESET_ALL)
                print(colorama.Fore.GREEN +"0. No"+ colorama.Style.RESET_ALL)
                print(colorama.Fore.GREEN +"1. Yes"+ colorama.Style.RESET_ALL)
                choice = input("> ")
                
                if choice == "0":
                    break
                elif choice == "1":
                    print('')
                    find_factory_by_name()
                else: print(colorama.Fore.GREEN +"Invalid choice!"+ colorama.Style.RESET_ALL)

        elif choice == "5":
            print('')
            update_factory()
            while True:
                print(colorama.Fore.GREEN +"Do you want to update another?"+ colorama.Style.RESET_ALL)
                print(colorama.Fore.GREEN +"0. No"+ colorama.Style.RESET_ALL)
                print(colorama.Fore.GREEN +"1. Yes"+ colorama.Style.RESET_ALL)
                choice = input("> ")
                
                if choice == "0":
                    break
                elif choice == "1":
                    print('')
                    update_factory()
                else: print(colorama.Fore.GREEN +"Invalid choice!"+ colorama.Style.RESET_ALL)

        elif choice == "6":
            print('')
            delete_factory()
            while True:
                print(colorama.Fore.GREEN +"Do you want to delete another?"+ colorama.Style.RESET_ALL)
                print(colorama.Fore.GREEN +"0. No"+ colorama.Style.RESET_ALL)
                print(colorama.Fore.GREEN +"1. Yes"+ colorama.Style.RESET_ALL)
                choice = input("> ")
                
                if choice == "0":
                    break
                elif choice == "1":
                    print('')
                    delete_factory()
                else: print(colorama.Fore.GREEN +"Invalid choice!"+ colorama.Style.RESET_ALL)

        elif choice == "7":
            print('')
            factory_car()
            while True:
                print(colorama.Fore.GREEN +"Do you want to check another factory's cars?"+ colorama.Style.RESET_ALL)
                print(colorama.Fore.GREEN +"0. No"+ colorama.Style.RESET_ALL)
                print(colorama.Fore.GREEN +"1. Yes"+ colorama.Style.RESET_ALL)
                choice = input("> ")
                
                if choice == "0":
                    break
                elif choice == "1":
                    print('')
                    factory_car()
                else: print(colorama.Fore.GREEN +"Invalid choice!"+ colorama.Style.RESET_ALL)

        else: print(colorama.Fore.GREEN +"Invalid choice!"+ colorama.Style.RESET_ALL)