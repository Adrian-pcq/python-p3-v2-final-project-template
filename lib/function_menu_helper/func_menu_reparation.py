from models.reparation import Reparation

def list_cars_rep():
    cars = Reparation.get_all()
    if len(cars)>0:
        for car in cars:
            print(car)
    else: print("There is no car being repaired!")

def create_car_rep(car):
    
    if car:
        
        cause=input("Enter the cause you have to repair the car for: ")
        new_car = Reparation.create(cause,car.model,car.year,car.weight,car.factory_id)
        print(f"Successfuly added: {new_car}")
        return car
    
    
def find_car_rep_by_id():
    _id = input("Enter car's id: ")
    car = Reparation.find_by_id(_id)
    print(car) if car else print(f"Car id({_id}) couldn't be found!")

def find_car_rep_by_model():
    
    model = input("Enter car's model: ")
    car = Reparation.find_by_model(model)
    print(car) if car else print(f"Car model({model}) couldn't be found")

def find_car_by_cause():
    
    cause = input("Enter car's cause for repair: ")
    car = Reparation.find_by_cause(cause)
    print(car) if car else print(f"Car with :({cause}) couldn't be found")

def delete_car_rep():
    
    from models.car import Car

    _id = input("Enter the car's id:")
    car = Reparation.find_by_id(_id)
    
    if car:
        car.delete()
        print(f"Successfuly repaired Car:{_id} {car.model}, {car.year}, {car.weight}, factory id:{car.factory_id}!")
        Car.create(car.model,car.year,car.weight,car.factory_id)
    else:
        print(f"Car id({_id}) not found!")

def car_factories():
    _id = input("Enter the car's id:")
    car = Reparation.find_by_id(_id)
    
    if car:
        factory = car.factory()
        print("Car: ")
        print(car)
        print("Factory: ")
        print(factory)
    else: (f"Car id({_id}) not found!")  