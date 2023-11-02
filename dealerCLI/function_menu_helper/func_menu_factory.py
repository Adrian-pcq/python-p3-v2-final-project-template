import colorama
from models.factory import Factory

def list_factories():
    
    factories = Factory.get_all()
    if len(factories)>0:
        for factory in factories:
            print(factory)
    else: print(colorama.Fore.GREEN +"There is no factory! Please add some!"+ colorama.Style.RESET_ALL)

def create_factory():
    
    name = input(colorama.Fore.GREEN +"Enter the factory's name: "+ colorama.Style.RESET_ALL)
    country = input(colorama.Fore.GREEN +"Enter the factory's country: "+ colorama.Style.RESET_ALL)
    
    try:
        factory = Factory.create(name,country)
        print(colorama.Fore.GREEN +"Successfuly added: "+ colorama.Style.RESET_ALL+f"{factory}")
    except Exception as exc:
        print(colorama.Fore.GREEN +"Error adding factory:"+ colorama.Style.RESET_ALL,exc)

def find_factory_by_id():
    
    _id = input(colorama.Fore.GREEN +"Enter the factory's id: "+ colorama.Style.RESET_ALL)
    factory = Factory.find_by_id(_id)
    print(factory) if factory else print(colorama.Fore.GREEN +"Factory id("+ colorama.Style.RESET_ALL+f"{_id}"+ colorama.Fore.GREEN +") couldn't be found!"+ colorama.Style.RESET_ALL)

def find_factory_by_name():
    
    name = input(colorama.Fore.GREEN +"Enter the factory's name: "+ colorama.Style.RESET_ALL)
    factory = Factory.find_by_name(name)
    print(factory) if factory else print(colorama.Fore.GREEN +"Factory name("+ colorama.Style.RESET_ALL+f"{name}"+ colorama.Fore.GREEN +") couldn't be found"+ colorama.Style.RESET_ALL)

def update_factory():
    
    _id = input(colorama.Fore.GREEN +"Enter the factory's id: "+ colorama.Style.RESET_ALL)
    factory = Factory.find_by_id(_id)
    
    if factory:
        try:
            name = input(colorama.Fore.GREEN +"Enter the new name: "+ colorama.Style.RESET_ALL)
            factory.name = name

            country = input(colorama.Fore.GREEN +"Enter the new country: "+ colorama.Style.RESET_ALL)
            factory.country = country

            factory.update()
            print(colorama.Fore.GREEN +f"Successfuly updated "+ colorama.Style.RESET_ALL+f"{factory}")
        
        except Exception as exc:
            print(colorama.Fore.GREEN +"Error updating factory:"+ colorama.Style.RESET_ALL,exc)
    else:
        print(colorama.Fore.GREEN +f"Factory id("+ colorama.Style.RESET_ALL+f"{_id}" + colorama.Fore.GREEN +") not found!"+ colorama.Style.RESET_ALL)

def delete_factory():
    
    _id = input(colorama.Fore.GREEN +"Enter the factory's id:"+ colorama.Style.RESET_ALL)
    factory = Factory.find_by_id(_id)
    
    if factory:
        while True:
            print(colorama.Fore.GREEN +f"Are you sure to delete "+ colorama.Style.RESET_ALL + f"{factory}")
            print(colorama.Fore.GREEN +"0. No"+ colorama.Style.RESET_ALL)
            print(colorama.Fore.GREEN +"1. Yes"+ colorama.Style.RESET_ALL)
            choice = input("> ")
            
            if choice == "1":
                factory.delete()
                print(colorama.Fore.GREEN +f"Successfuly deleted Factory:{_id} {factory.name} from {factory.country}!"+ colorama.Style.RESET_ALL)
                break

            elif choice == "0": 
                break
            
            else: print(colorama.Fore.GREEN +"Invalid choice!"+ colorama.Style.RESET_ALL)
    else:
        print(colorama.Fore.GREEN +f"Factory id("+ colorama.Style.RESET_ALL+"{_id}"+ colorama.Fore.GREEN +") not found!"+ colorama.Style.RESET_ALL)

def factory_car():
    
    _id = input(colorama.Fore.GREEN +"Enter the factory's id:"+ colorama.Style.RESET_ALL)
    factory = Factory.find_by_id(_id)
    
    if factory:
        
        if len(factory.cars())== 0 and len(factory.cars_rep())==0:
            print(colorama.Fore.GREEN +f"There are no cars belonging to "+ colorama.Style.RESET_ALL+f"{factory}")
            
        elif len(factory.cars())>0 and len(factory.cars_rep())==0:
            print(colorama.Fore.GREEN +"Factory: "+ colorama.Style.RESET_ALL)
            print(factory)
            print('')
            print(colorama.Fore.GREEN +"Cars: "+ colorama.Style.RESET_ALL)
            car = factory.cars()
            [print(ca) for ca in car]

        elif len(factory.cars_rep())>0 and len(factory.cars())==0:
            print(colorama.Fore.GREEN +"Factory: "+ colorama.Style.RESET_ALL)
            print(factory)
            print('')
            print(colorama.Fore.GREEN +"Cars: "+ colorama.Style.RESET_ALL)
            car = factory.cars_rep()
            [print(ca) for ca in car]

        elif len(factory.cars_rep())>0 and len(factory.cars())>0:
            print(colorama.Fore.GREEN +"Factory: "+ colorama.Style.RESET_ALL)
            print(factory)
            print('')
            print(colorama.Fore.GREEN +"Cars: "+ colorama.Style.RESET_ALL)
            car = factory.cars()
            car_rep = factory.cars_rep()
            [print(ca) for ca in car]
            [print(ca_r) for ca_r in car_rep]

    else:
        print(colorama.Fore.GREEN +f"Factory id("+ colorama.Style.RESET_ALL+f"{_id}"+ colorama.Fore.GREEN +") not found!"+ colorama.Style.RESET_ALL)

Factory.create_table()