from sub_menu.factory_sub_menu import factory_menu
from sub_menu.car_sub_menu import car_menu
from sub_menu.reparation_sub_menu import reparation_menu

def menu():
        print("Please select an option:")
        print("0. Exit the program")
        print("1. Factory Menu")
        print("2. Car Menu")
        print("3. Reparations Menu")

def welcome():
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

def bye():
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

def main():
    welcome()
    while True:
        menu()
        choice = input("> ")
        
        if choice == "0":
            bye()
            exit()
        
        elif choice == "1":
              factory_menu()

        elif choice == "2":
              car_menu()

        elif choice == "3":
            reparation_menu()
 
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()