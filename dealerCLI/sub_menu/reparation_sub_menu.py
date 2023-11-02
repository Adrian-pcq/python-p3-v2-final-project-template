import colorama
from function_menu_helper.func_menu_reparation import (
    list_cars_rep,
    create_car_rep,
    find_car_rep_by_id,
    find_car_rep_by_model,
    find_car_by_cause,
    delete_car_rep,
    car_factories
)

from function_menu_helper.func_menu_car import ( delete_car_for_rep, find_car_by_id)

def reparation_menu_print():
    print('')
    print('')
    print(colorama.Fore.MAGENTA +'------------------Reparation Menu------------------'+ colorama.Style.RESET_ALL)
    print('')
    print(colorama.Fore.MAGENTA +"0. Back to Main Menu"+ colorama.Style.RESET_ALL)
    print(colorama.Fore.MAGENTA +"1. List all the cars been repaired"+ colorama.Style.RESET_ALL)
    print(colorama.Fore.MAGENTA +"2. Set a new car for repair"+ colorama.Style.RESET_ALL)
    print(colorama.Fore.MAGENTA +"3. Find a car by id"+ colorama.Style.RESET_ALL)
    print(colorama.Fore.MAGENTA +"4. Find a car by model"+ colorama.Style.RESET_ALL)
    print(colorama.Fore.MAGENTA +"5. Find a car by cause of repair"+ colorama.Style.RESET_ALL)
    print(colorama.Fore.MAGENTA +"6. Finish a car reparation"+ colorama.Style.RESET_ALL)
    print(colorama.Fore.MAGENTA +"7. See car's factory"+ colorama.Style.RESET_ALL)

def reparation_menu():
    while True:
        reparation_menu_print()
        choice = input("> ")
        
        if choice == "0":
            break

        elif choice == "1":
            print('')
            list_cars_rep()

        elif choice == "2":
            print('')
            delete_car_for_rep(create_car_rep(find_car_by_id()))
            
            while True:
                print(colorama.Fore.MAGENTA +"Do you want to set another?"+ colorama.Style.RESET_ALL)
                print(colorama.Fore.MAGENTA +"0. No"+ colorama.Style.RESET_ALL)
                print(colorama.Fore.MAGENTA +"1. Yes"+ colorama.Style.RESET_ALL)
                choice=input("> ")
                
                if choice == "0":
                    break
                elif choice == "1":
                    print('')
                    delete_car_for_rep(create_car_rep(find_car_by_id()))
                else: print(colorama.Fore.MAGENTA +"Invalid choice"+ colorama.Style.RESET_ALL)    

        elif choice =="3":
            print('')
            find_car_rep_by_id()
            
            while True:
                print(colorama.Fore.MAGENTA +"Do you want to find another?"+ colorama.Style.RESET_ALL)
                print(colorama.Fore.MAGENTA +"0. No"+ colorama.Style.RESET_ALL)
                print(colorama.Fore.MAGENTA +"1. Yes"+ colorama.Style.RESET_ALL)
                choice=input("> ")
                
                if choice == "0":
                    break
                elif choice == "1":
                    print('')
                    find_car_rep_by_id()
                else: print(colorama.Fore.MAGENTA +"Invalid choice"+ colorama.Style.RESET_ALL)

        elif choice =="4":
            print('')
            find_car_rep_by_model()
            
            while True:
                print(colorama.Fore.MAGENTA +"Do you want to find another?"+ colorama.Style.RESET_ALL)
                print(colorama.Fore.MAGENTA +"0. No"+ colorama.Style.RESET_ALL)
                print(colorama.Fore.MAGENTA +"1. Yes"+ colorama.Style.RESET_ALL)
                choice=input("> ")
                
                if choice == "0":
                    break
                elif choice == "1":
                    print('')
                    find_car_rep_by_model()
                else: print(colorama.Fore.MAGENTA +"Invalid choice"+ colorama.Style.RESET_ALL)

        elif choice == "5":
            print('')
            find_car_by_cause()
            
            while True:
                print(colorama.Fore.MAGENTA +"Do you want to find another?"+ colorama.Style.RESET_ALL)
                print(colorama.Fore.MAGENTA +"0. No"+ colorama.Style.RESET_ALL)
                print(colorama.Fore.MAGENTA +"1. Yes"+ colorama.Style.RESET_ALL)
                choice=input("> ")
                
                if choice == "0":
                    break
                elif choice == "1":
                    print('')
                    find_car_by_cause()
                else: print(colorama.Fore.MAGENTA +"Invalid choice"+ colorama.Style.RESET_ALL)

        elif choice == "6":
            print('')
            delete_car_rep()
            
            while True:
                print(colorama.Fore.MAGENTA +"Do you want to repair another?"+ colorama.Style.RESET_ALL)
                print(colorama.Fore.MAGENTA +"0. No"+ colorama.Style.RESET_ALL)
                print(colorama.Fore.MAGENTA +"1. Yes"+ colorama.Style.RESET_ALL)
                choice=input("> ")
                
                if choice == "0":
                    break
                elif choice == "1":
                    print('')
                    delete_car_rep()
                else: print(colorama.Fore.MAGENTA +"Invalid choice"+ colorama.Style.RESET_ALL)

        elif choice == "7":
            print('')
            car_factories()

            while True:
                print(colorama.Fore.MAGENTA +"Do you want to check another car's factory?"+ colorama.Style.RESET_ALL)
                print(colorama.Fore.MAGENTA +"0. No"+ colorama.Style.RESET_ALL)
                print(colorama.Fore.MAGENTA +"1. Yes"+ colorama.Style.RESET_ALL)
                choice=input("> ")
                
                if choice == "0":
                    break
                elif choice == "1":
                    print('')
                    car_factories()
                else: print(colorama.Fore.MAGENTA +"Invalid choice"+ colorama.Style.RESET_ALL)
        
        else: print(colorama.Fore.MAGENTA +"Invalid choice!"+ colorama.Style.RESET_ALL)