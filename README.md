# Phase 3 Project: Dealer CLI 
It's a CLI APP that contains information about available cars and the factories they belong to. Comes with multiples functionalities for the user. 

---

## Runing the App
- `cd dealerCLI` for open app's directory.
- `pipenv install` & `pipenv shell` to settup the virtual envyroment.
- `python lib/data.py` for seeding the app.
- `python lib/menu.py` for run the app in the Terminal.

---

## Description

The application uses classes and a one-to-many relationship to manage factories and cars also related to reparation the same way. The Factory class represents a factory with its identifier and name, while the Car class represents a car with its identifier, model, year, weight and the identifier of the factory it belongs to. Reparation is a class that holds the cars been repaired, it has cause and the attributes from Car as its own.

The application interacts with the SQLite database to perform CRUD operations on the factories, cars and reparations tables.

The application displays a menu with options to perform different operations related to factories, cars and reparations. The user can select an option and provide the necessary data to carry out the desired operation. For example: they can list all existing factories, create a new factory, search for a factory by its id or name, update an existing factory, or delete a factory.

Similarly, the user can perform operations related to cars, such as listing all existing cars, creating a new car, searching for a car by its id or model, updating an existing car, or deleting a car.

Additionally, the user can manage car repairs by adding cars to a repair list, searching for cars by model or cause of repair, and finishing repairs by removing cars from the repair list    

In summary, the implemented application allows managing factories and cars, been repaired or not, using classes and a one-to-many relationship through a SQLite database. Overall, it provides a comprehensive way to manage factories, cars, and repairs through a user-friendly menu interface.

---

## Structure

The `lib/menu.py`file contains the menu were the user can interact with the app, this file uses information from `lib/sub_menu`'s three files: `car_sub_menu.py `, `factory_sub_menu.py ` and  `reparation_sub_menu.py `  to display each menu belonging to each class. Within the `lib/function_menu_helper` folder, there are three files: `func_menu_car.py `, `func_menu_factory.py ` and `func_menu_reparation.py ` where all the functions used in the `sub_menu`'s files are implemented, respectively. The main code, that is, the three Factory, Car, and Reparation classes, is located in the `lib/models` folder. In `lib/data.py` is where the persistent information is stored.

