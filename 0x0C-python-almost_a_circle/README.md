# Python unittests, args and kwargs.

In this project, I got to study and understand arguments of variable length.
The project is also a recap on previously covered topics such as OOP, file input/output amongst others.  

## Tests.

The module `unittest` is utilized for testing the classes and methods.
All the test files for each module is stored in the folder [tests/test_models](./tests/test_models).  

## Modules.

The modules are stored in the directory [models](./models).

### base.py

This module defines a class `Base` that is the class from which other classes inherit from.  
Class `Base` has the following features:  

* Private class attribute `__nb_objects = 0`
* Class constructor: `def __init__(self, id=None)` that initializes an instance of `Base`
* Public instance attribute `id`
* Static method `def to_json_string(list_dictionaries):` that returns the JSON string representation of `list_dictionaries`.
* Class method `def save_to_file(cls, list_objs):` that writes the JSON string representation of `list_objs` to a file
* Static method `def from_json_string(json_string):` that returns the list of the JSON string representation `json_string`
* Class method `def create(cls, **dictionary):` that returns an instance with all attributes already set
* Class method `def load_from_file(cls):` that returns a list of instances
* Class methods `def save_to_file_csv(cls, list_objs):` and `def load_from_file_csv(cls):` that serializes and deserializes in CSV

The goal of it is to manage the `id` attribute in all the future classes and to avoid duplicating the same code (by extension, same bugs).

### rectangle.py

