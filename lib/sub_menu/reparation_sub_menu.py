from function_menu_helper.func_menu_reparation import (
    list_cars_rep,
    create_car_rep,
    find_car_rep_by_id,
    find_car_rep_by_model,
    find_car_by_cause,
    delete_car_rep
)

from function_menu_helper.func_menu_car import ( delete_car_for_rep, find_car_by_id)

def reparation_menu_print():
    print("0. Back to Main Menu")
    print("1. List all the cars been repaired")
    print("2. Set a new car for repair")
    print("3. Find a car by id")
    print("4. Find a car by model")
    print("5. Find a car by cause of repair")
    print("6. Finish a car reparation")

def reparation_menu():
    while True:
        reparation_menu_print()
        choice = input("> ")
        
        if choice == "0":
            break

        elif choice == "1":
            list_cars_rep()

        elif choice == "2":
            delete_car_for_rep(create_car_rep(find_car_by_id()))
            
            while True:
                print("Do you want to set another?")
                print("0. No")
                print("1. Yes")
                choice=input("> ")
                
                if choice == "0":
                    break
                elif choice == "1":
                    delete_car_for_rep(create_car_rep(find_car_by_id()))
                else: print("Invalid choice")    

        elif choice =="3":
            find_car_rep_by_id()
            
            while True:
                print("Do you want to find another?")
                print("0. No")
                print("1. Yes")
                choice=input("> ")
                
                if choice == "0":
                    break
                elif choice == "1":
                    find_car_rep_by_id()
                else: print("Invalid choice")

        elif choice =="4":
            find_car_rep_by_model()
            
            while True:
                print("Do you want to find another?")
                print("0. No")
                print("1. Yes")
                choice=input("> ")
                
                if choice == "0":
                    break
                elif choice == "1":
                    find_car_rep_by_model()
                else: print("Invalid choice")

        elif choice == "5":
            find_car_by_cause()
            
            while True:
                print("Do you want to find another?")
                print("0. No")
                print("1. Yes")
                choice=input("> ")
                
                if choice == "0":
                    break
                elif choice == "1":
                    find_car_by_cause()
                else: print("Invalid choice")

        elif choice == "6":
            delete_car_rep()
            
            while True:
                print("Do you want to repair another?")
                print("0. No")
                print("1. Yes")
                choice=input("> ")
                
                if choice == "0":
                    break
                elif choice == "1":
                    delete_car_rep()
                else: print("Invalid choice")
        
        else: print("Invalid choice!")