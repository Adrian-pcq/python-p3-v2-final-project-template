from models.factory import Factory

def list_factories():
    
    factories = Factory.get_all()
    for factory in factories:
        print(factory)

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
    print(factory) if factory else print("Factory couldn't be found!")

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
        car = factory.cars()
        print(car)
    else:
        print(f"Factory's id({_id}) not found!")