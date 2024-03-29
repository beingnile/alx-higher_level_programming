#!/usr/bin/python3
"""Defines a base class to manage the id attribute"""
import json
import csv
import turtle


class Base:
    """A base class from which other classes inherit from"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            from models.rectangle import Rectangle
            instance = Rectangle(1, 1)
            instance.update(**dictionary)
        if cls.__name__ == 'Square':
            from models.square import Square
            instance = Square(1)
            instance.update(**dictionary)

        return instance

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of
        list_objs to a file
        """
        filename = f'{cls.__name__}.json'
        if list_objs is None or len(list_objs) == 0:
            with open(filename, 'w') as f:
                f.write('[]')
        else:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
            list_json = cls.to_json_string(list_dicts)
            with open(filename, 'w') as f:
                f.write(list_json)

    @classmethod
    def load_from_file(cls):
        """Return a list of instances"""
        filename = f'{cls.__name__}.json'
        res = []
        try:
            with open(filename, 'r') as f:
                str_json = f.read()
                list_json = cls.from_json_string(str_json)
                for instance in list_json:
                    ins = cls.create(**instance)
                    res.append(ins)
            return res
        except FileNotFoundError:
            return res

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes objects to csv files"""
        filename = f'{cls.__name__}.csv'
        if cls.__name__ == 'Rectangle':
            fieldnames = ['id', 'width', 'height', 'x', 'y']
        else:
            fieldnames = ['id', 'size', 'x', 'y']
        if list_objs is None or len(list_objs) == 0:
            with open(filename, 'w') as f:
                writer = csv.DictWriter(f, fieldnames)
                writer.writeheader()
        else:
            data = [obj.to_dictionary() for obj in list_objs]
            with open(filename, 'w') as f:
                writer = csv.DictWriter(f, fieldnames)
                writer.writeheader()
                writer.writerows(data)

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of objects from a csv file"""
        filename = f'{cls.__name__}.csv'
        dict_res = []
        res = []
        try:
            with open(filename, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    dict_res.append(row)
                for dictionary in dict_res:
                    for key, value in dictionary.items():
                        dictionary[key] = int(value)
                    obj = cls.create(**dictionary)
                    res.append(obj)
            return res
        except FileNotFoundError:
            return res

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of
        list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws Squares and rectangles using the turtle module"""
        turtle.speed(3)
        for obj in list_rectangles:
            turtle.up()
            turtle.goto(obj.x, obj.y)
            turtle.down()
            turtle.forward(obj.width)
            turtle.rt(90)
            turtle.forward(obj.height)
            turtle.rt(90)
            turtle.forward(obj.width)
            turtle.rt(90)
            turtle.forward(obj.height)
            turtle.rt(90)
            turtle.up()
            turtle.home()
        for obj in list_squares:
            turtle.pencolor("violet")
            turtle.up()
            turtle.goto(obj.x, obj.y)
            turtle.down()
            turtle.forward(obj.size)
            turtle.rt(90)
            turtle.forward(obj.size)
            turtle.rt(90)
            turtle.forward(obj.size)
            turtle.rt(90)
            turtle.forward(obj.size)
            turtle.rt(90)
            turtle.up()
            turtle.home()
            turtle.ht()
