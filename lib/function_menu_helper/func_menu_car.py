from models.car import Car

def list_cars():
    
    cars = Car.get_all()
    for car in cars:
        print(car)

def create_car():
    
    model = input("Enter car's name: ")
    year = int(input("Enter car's year: "))
    weight = float(input("Enter car's weight: "))
    factory_id = int(input("Enter factory's id to which belongns: "))
    
    try:
        car = Car.create(model,year,weight,factory_id)
        print(f"Successfuly added: {car}")
    except Exception as exc:
        print("Error adding car:",exc)

def find_car_by_id():
    
    _id = input("Enter car's id: ")
    car = Car.find_by_id(_id)
    print(car) if car else print("Car couldn't be found!")
    return car

def find_car_by_model():
    
    model = input("Enter car's model: ")
    car = Car.find_by_model(model)
    print(car) if car else print(f"Car model({model}) couldn't be found")

def update_car():
    
    _id = input("Enter the car's id: ")
    car = Car.find_by_id(_id)
    
    if car:
        try:
            model = input("Enter the name: ")
            car.model = model

            year = int(input("Enter the year: "))
            car.year = year

            weight = float(input("Enter the weight: "))
            car.weight = weight

            factory_id = int(input("Enter the factory's id to which belongs: "))
            car.factory_id = factory_id

            car.update()
            print(f"Successfuly updated {car}!")
        
        except Exception as exc:
            print("Error updating car:",exc)
    else:
        print(f"Factory's id({_id}) not found!")

def delete_car():
    
    _id = input("Enter the car's id:")
    car = Car.find_by_id(_id)
    
    if car:
        while True:
            print(f"Are you sure you want to delete {car}?")
            print("0. No")
            print("1. Yes")
            choice = input("> ")
            
            if choice == "1":
                car.delete()
                print(f"Successfuly deleted Car:{_id} {car.model}, {car.year}, {car.weight}, factory id:{car.factory_id}!")
                break
            
            elif choice == "0":
                break
            else: print("Invalid choice!")
    else:
        print(f"Car's id({_id}) not found!")

def delete_car_for_rep(car):
    if car:
      car.delete()
    else:print("")