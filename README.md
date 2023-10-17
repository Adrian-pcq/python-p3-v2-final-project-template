# Phase 3 Project: Cape Coral Dealer CLI 

---

## Introduction 

This code uses all the skills learned in this phase:
- Python fundamentals.
- Data structures (and more recently, algorithms).
- Object-oriented programming.
- Object inheritance.
- Instance and class attributes and methods.
- Configuring applications.
- SQL fundamentals.
- Table relations in SQL.
- Object-relational mapping with Python.
- Building CLIs.

It's a CLI APP that contains information about available cars and the factories they belong to. Comes with multiples functionalities for the user. 

---

## Description

The application uses classes and a one-to-many relationship to manage factories and cars. The Factory class represents a factory with its identifier and name, while the Car class represents a car with its identifier, model, year, weight and the identifier of the factory it belongs to.

The application interacts with the SQLite database to perform CRUD operations on the factories and cars tables.

The application displays a menu with options to perform different operations related to factories and cars. The user can select an option and provide the necessary data to carry out the desired operation. For example, they can list all existing factories, create a new factory, search for a factory by its identifier or name, update an existing factory, or delete a factory.

Similarly, the user can perform operations related to cars, such as listing all existing cars, creating a new car, searching for a car by its identifier or model, updating an existing car, or deleting a car.

In summary, the implemented application allows managing factories and cars using classes and a one-to-many relationship through a SQLite database. The user can perform different operations related to factories and cars through an interactive menu.

---

## Structure

The `lib/menu.py`file contains the implementation of the menu, which uses functions from `func_menu_car.py` and `func_menu_factory.py` to perform tasks. In `data.py`, the persistent information related to the database is stored. In `lib/model/_init_.py`, the application's connection to SQLite is created. Factory and Car classes are stored in `lib/model/factory.py` and `lib/model/car.py`respectively.  


