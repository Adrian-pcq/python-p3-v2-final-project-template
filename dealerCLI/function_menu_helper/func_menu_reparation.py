import colorama
from models.reparation import Reparation

def list_cars_rep():
    cars = Reparation.get_all()
    if len(cars)>0:
        for car in cars:
            print(car)
    else: print(colorama.Fore.MAGENTA+"There is no car being repaired!"+ colorama.Style.RESET_ALL)

def create_car_rep(car):
    
    if car:
        
        cause=input(colorama.Fore.MAGENTA+"Enter the cause you have to repair the car for: "+ colorama.Style.RESET_ALL)
        new_car = Reparation.create(cause,car.model,car.year,car.weight,car.factory_id)
        print(colorama.Fore.MAGENTA+"Successfuly added: "+ colorama.Style.RESET_ALL+f"{new_car}")
        return car
    
    
def find_car_rep_by_id():
    _id = input(colorama.Fore.MAGENTA+"Enter car's id: "+ colorama.Style.RESET_ALL)
    car = Reparation.find_by_id(_id)
    print(car) if car else print(colorama.Fore.MAGENTA+"Car id("+ colorama.Style.RESET_ALL+f"{_id}"+ colorama.Fore.MAGENTA+") couldn't be found!"+ colorama.Style.RESET_ALL)

def find_car_rep_by_model():
    
    model = input(colorama.Fore.MAGENTA+"Enter car's model: "+ colorama.Style.RESET_ALL)
    car = Reparation.find_by_model(model)
    print(car) if car else print(colorama.Fore.MAGENTA+"Car model("+ colorama.Style.RESET_ALL+f"{model}"+ colorama.Fore.MAGENTA+") couldn't be found"+ colorama.Style.RESET_ALL)

def find_car_by_cause():
    
    cause = input(colorama.Fore.MAGENTA+"Enter car's cause for repair: "+ colorama.Style.RESET_ALL)
    car = Reparation.find_by_cause(cause)
    print(car) if car else print(colorama.Fore.MAGENTA+"Car with :("+ colorama.Style.RESET_ALL+f"{cause}"+ colorama.Fore.MAGENTA+") couldn't be found"+ colorama.Style.RESET_ALL)

def delete_car_rep():
    
    from models.car import Car

    _id = input(colorama.Fore.MAGENTA+"Enter the car's id:"+ colorama.Style.RESET_ALL)
    car = Reparation.find_by_id(_id)
    
    if car:
        car.delete()
        print(colorama.Fore.MAGENTA+f"Successfuly repaired Car:{_id} {car.model}, {car.year}, {car.weight}, factory id:{car.factory_id}!"+ colorama.Style.RESET_ALL)
        Car.create(car.model,car.year,car.weight,car.factory_id)
    else:
        print(colorama.Fore.MAGENTA+"Car id("+ colorama.Style.RESET_ALL+f"{_id}"+ colorama.Fore.MAGENTA+") not found!"+ colorama.Style.RESET_ALL)

def car_factories():
    _id = input(colorama.Fore.MAGENTA+"Enter the car's id:"+ colorama.Style.RESET_ALL)
    car = Reparation.find_by_id(_id)
    
    if car:
        factory = car.factory()
        print(colorama.Fore.MAGENTA+"Car: "+ colorama.Style.RESET_ALL)
        print(car)
        print('')
        print(colorama.Fore.MAGENTA+"Factory: "+ colorama.Style.RESET_ALL)
        [print(fact) for fact in factory]
    else: print(colorama.Fore.MAGENTA+f"Car id("+ colorama.Style.RESET_ALL+f"{_id}"+ colorama.Fore.MAGENTA+") not found!"+ colorama.Style.RESET_ALL)  