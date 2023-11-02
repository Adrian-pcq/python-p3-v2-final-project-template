from models.car import Car
import colorama

def list_cars():
    
    cars = Car.get_all()
    if len(cars)>0:
        for car in cars:
            print(car)
    else: print(colorama.Fore.BLUE +"There is no car! Please add some!"+ colorama.Style.RESET_ALL)

def create_car():
    
    model = input(colorama.Fore.BLUE +"Enter car's model: "+ colorama.Style.RESET_ALL)
    year = input(colorama.Fore.BLUE +"Enter car's year: "+ colorama.Style.RESET_ALL)
    weight = input(colorama.Fore.BLUE +"Enter car's weight: "+ colorama.Style.RESET_ALL)
    factory_id = input(colorama.Fore.BLUE +"Enter factory's id to which belongns: "+ colorama.Style.RESET_ALL)
    
    try:
        car = Car.create(model,int(year),float(weight),int(factory_id))
        print(colorama.Fore.BLUE +"Successfuly added: "+ colorama.Style.RESET_ALL +f"{car}")
    except Exception as exc:
        print(colorama.Fore.BLUE +"Error adding car:"+ colorama.Style.RESET_ALL,exc)

def find_car_by_id():
    
    _id = input(colorama.Fore.BLUE +"Enter car's id: "+ colorama.Style.RESET_ALL)
    car = Car.find_by_id(_id)
    print(car) if car else print(colorama.Fore.BLUE +"Car id("+ colorama.Style.RESET_ALL +f"{_id}" + colorama.Fore.BLUE +") couldn't be found!"+ colorama.Style.RESET_ALL)
    return car

def find_car_by_model():
    
    model = input(colorama.Fore.BLUE +"Enter car's model: "+ colorama.Style.RESET_ALL)
    car = Car.find_by_model(model)
    print(car) if car else print(colorama.Fore.BLUE +"Car model("+ colorama.Style.RESET_ALL+f"{model}"+ colorama.Fore.BLUE + ") couldn't be found"+ colorama.Style.RESET_ALL)

def update_car():
    
    _id = input(colorama.Fore.BLUE +"Enter the car's id: "+ colorama.Style.RESET_ALL)
    car = Car.find_by_id(_id)
    
    if car:
        try:
            model = input(colorama.Fore.BLUE +"Enter the name: "+ colorama.Style.RESET_ALL)
            car.model = model

            year = int(input(colorama.Fore.BLUE +"Enter the year: "+ colorama.Style.RESET_ALL))
            car.year = year

            weight = float(input(colorama.Fore.BLUE +"Enter the weight: "+ colorama.Style.RESET_ALL))
            car.weight = weight

            factory_id = int(input(colorama.Fore.BLUE +"Enter the factory's id to which belongs: "+ colorama.Style.RESET_ALL))
            car.factory_id = factory_id

            car.update()
            print(colorama.Fore.BLUE + "Successfuly updated "+ colorama.Style.RESET_ALL+f"{car}")
        
        except Exception as exc:
            print(colorama.Fore.BLUE +"Error updating car:"+ colorama.Style.RESET_ALL ,exc)
    else:
        print(colorama.Fore.BLUE +"Car id("+ colorama.Style.RESET_ALL+f"{_id}"+ colorama.Fore.BLUE+") not found!"+ colorama.Style.RESET_ALL)

def delete_car():
    
    _id = input(colorama.Fore.BLUE +"Enter the car's id:"+ colorama.Style.RESET_ALL)
    car = Car.find_by_id(_id)
    
    if car:
        while True:
            print(colorama.Fore.BLUE +"Are you sure you want to delete "+ colorama.Style.RESET_ALL+f"{car}"+ colorama.Fore.BLUE +"?"+ colorama.Style.RESET_ALL)
            print(colorama.Fore.BLUE +"0. No"+ colorama.Style.RESET_ALL)
            print(colorama.Fore.BLUE +"1. Yes"+ colorama.Style.RESET_ALL)
            choice = input("> ")
            
            if choice == "1":
                car.delete()
                print(colorama.Fore.BLUE +f"Successfuly deleted Car:{_id} {car.model}, {car.year}, {car.weight}, factory id:{car.factory_id}!"+ colorama.Style.RESET_ALL)
                break
            
            elif choice == "0":
                break
            else: print(colorama.Fore.BLUE +"Invalid choice!"+ colorama.Style.RESET_ALL)
    else:
        print(colorama.Fore.BLUE +"Car id("+ colorama.Style.RESET_ALL+f"{_id}"+ colorama.Fore.MAGENTA+") not found!"+ colorama.Style.RESET_ALL)

def delete_car_for_rep(car):
    if car:
      car.delete()
    else:print("")

def car_factories():
    _id = input(colorama.Fore.BLUE +"Enter the car's id:"+ colorama.Style.RESET_ALL)
    car = Car.find_by_id(_id)
    
    if car:
        factory = car.factory()
        print(colorama.Fore.BLUE +"Car: "+ colorama.Style.RESET_ALL)
        print(car)
        print('')
        print(colorama.Fore.BLUE +"Factory: "+ colorama.Style.RESET_ALL)
        print(factory)
    else: print(colorama.Fore.BLUE +"Car id("+ colorama.Style.RESET_ALL+f"{_id}"+ colorama.Fore.BLUE +") not found!"+ colorama.Style.RESET_ALL)

Car.create_table()