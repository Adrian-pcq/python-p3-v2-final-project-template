from sub_menu.factory_sub_menu import factory_menu
from sub_menu.car_sub_menu import car_menu
from sub_menu.reparation_sub_menu import reparation_menu
import colorama
colorama.init()

def menu():
        print('')
        print('')
        print(colorama.Fore.RED +'---------------------- Menu ----------------------'+ colorama.Style.RESET_ALL)
        print('')
        print(colorama.Fore.RED + "Please select an option:"+ colorama.Style.RESET_ALL)
        print(colorama.Fore.RED + "0. Exit the program"+ colorama.Style.RESET_ALL)
        print(colorama.Fore.RED + "1. Factory Menu"+ colorama.Style.RESET_ALL)
        print(colorama.Fore.RED + "2. Car Menu"+ colorama.Style.RESET_ALL)
        print(colorama.Fore.RED + "3. Reparations Menu"+ colorama.Style.RESET_ALL )

def welcome():
    print(" ")
    print(" ")
    print(colorama.Fore.RED +"         Welcome to the Dealer CLI!!!"+ colorama.Style.RESET_ALL)
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
    print(colorama.Fore.RED +"         I hope you enjoyed it a lot!!!"+ colorama.Style.RESET_ALL)
    print("")
    print("")
    print(colorama.Fore.RED +" BBBBBBBBBBB    YYY       YYY   EEEEEEEEEE   !!!!!!! "+ colorama.Style.RESET_ALL)
    print(colorama.Fore.RED +" BBB    BBBB     YYY     YYY    EEEEEEEEEE   !!!!!!! "+ colorama.Style.RESET_ALL)
    print(colorama.Fore.RED +" BBBBBBBBBBB      YYY   YYY     EEE           !!!!!  "+ colorama.Style.RESET_ALL)
    print(colorama.Fore.RED +" BBB               YYYYYYY      EEEEEEEEEE     !!!   "+ colorama.Style.RESET_ALL)
    print(colorama.Fore.RED +" BBBBBBBBBBB         YYY        EEE                  "+ colorama.Style.RESET_ALL)
    print(colorama.Fore.RED +" BBB    BBBB         YYY        EEEEEEEEEE     !!!   "+ colorama.Style.RESET_ALL)
    print(colorama.Fore.RED +" BBBBBBBBBBB         YYY        EEEEEEEEEE     !!!   "+ colorama.Style.RESET_ALL)
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
            print(colorama.Fore.RED +"Invalid choice!"+ colorama.Style.RESET_ALL)

if __name__ == "__main__":
    main()