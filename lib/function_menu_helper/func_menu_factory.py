from models.factory import Factory

def list_factories():
    
    factories = Factory.get_all()
    if len(factories)>0:
        for factory in factories:
            print(factory)
    else: print("There is no factory! Please add some!")

def create_factory():
    
    name = input("Enter the factory's name: ")
    country = input("Enter the factory's country: ")
    
    try:
        factory = Factory.create(name,country)
        print(f"Successfuly added: {factory}!")
    except Exception as exc:
        print("Error adding factory:",exc)

def find_factory_by_id():
    
    _id = input("Enter the factory's id: ")
    factory = Factory.find_by_id(_id)
    print(factory) if factory else print(f"Factory {_id} couldn't be found!")

def find_factory_by_name():
    
    name = input("Enter the factory's name: ")
    factory = Factory.find_by_name(name)
    print(factory) if factory else print(f"Factory {name} couldn't be found")

def update_factory():
    
    _id = input("Enter the factory's id: ")
    factory = Factory.find_by_id(_id)
    
    if factory:
        try:
            name = input("Enter the new name: ")
            factory.name = name

            country = input("Enter the new country: ")
            factory.country = country

            factory.update()
            print(f"Successfuly updated {factory}!")
        
        except Exception as exc:
            print("Error updating factory:",exc)
    else:
        print(f"Factory's id({_id}) not found!")

def delete_factory():
    
    _id = input("Enter the factory's id:")
    factory = Factory.find_by_id(_id)
    
    if factory:
        factory.delete()
        print(f"Successfuly deleted Factory:{_id} {factory.name} from {factory.country}!")
    else:
        print(f"Factory's id({_id}) not found!")

def factory_car():
    
    _id = input("Enter the factory's id:")
    factory = Factory.find_by_id(_id)
    
    if factory:
        
        if len(factory.cars())== 0 and len(factory.cars_rep())==0:
            print("There are no cars belonging to this factory!")
            
        elif len(factory.cars())>0 and len(factory.cars_rep())==0:
            car = factory.cars()
            print(car)

        elif len(factory.cars_rep())>0 and len(factory.cars())==0:
            car = factory.cars_rep()
            print(car)

        elif len(factory.cars_rep())>0 and len(factory.cars())>0:
            car = factory.cars()
            car_rep = factory.cars_rep()
            print(car)
            print(car_rep)

    else:
        print(f"Factory's id({_id}) not found!")

Factory.create_table()