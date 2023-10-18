from models.reparation import Reparation

def list_cars_rep():
    cars = Reparation.get_all()
    for car in cars:
        print(car)

def create_car_rep(car):
    
    cause=input("Enter the cause you have to repair the car for: ")

    try:
        new_car = Reparation.create(cause,car.model,car.year,car.weight,car.factory_id)
        print(f"Successfuly added: {new_car}")
    except Exception as exc:
        print("Error adding the car:",exc)
    return car
    
def find_car_rep_by_id():
    _id = input("Enter car's id: ")
    car = Reparation.find_by_id(_id)
    print(car) if car else print("Car couldn't be found!")

def find_car_rep_by_model():
    model = input("Enter car's model: ")
    car = Reparation.find_by_model(model)
    print(car) if car else print(f"Car model({model}) couldn't be found")

def find_car_by_cause():
    cause = input("Enter car's cause for repair: ")
    car = Reparation.find_by_cause(cause)
    print(car) if car else print(f"Car with this cause:({cause}) couldn't be found")

def delete_car_rep():
    from models.car import Car
    _id = input("Enter the car's id:")
    car = Reparation.find_by_id(_id)
    if car:
        car.delete()
        print(f"Successfuly repaired Car:{_id} {car.model}, {car.year}, {car.weight}, factory id:{car.factory_id}!")
    else:
        print(f"Car's id({_id}) not found!")
    Car.create(car.model,car.year,car.weight,car.factory_id)