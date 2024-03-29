#!/usr/bin/python3
"""Define a base class model."""
import json
import os.path
import turtle


class Base:
    """this is inside the class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """inits the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json string"""
        return json.dumps(list_dictionaries or [])

    @staticmethod
    def from_json_string(json_string):
        """returns list of jsons"""
        return json.loads(json_string or "[]")

    @classmethod
    def create(cls, **dictionary):
        """makes instance"""
        if cls.__name__ is 'Square':
            newcreate = cls(1)
        if cls.__name__ is 'Rectangle':
            newcreate = cls(1, 1)
        if newcreate:
            newcreate.update(**dictionary)
            return newcreate

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file"""
        try:
            jsons = cls.to_json_string([x.to_dictionary() for x in list_objs])
        except Exception:
            jsons = '[]'
        with open(cls.__name__+'.json', 'w', encoding='utf-8') as f:
            f.write(jsons)

    @classmethod
    def load_from_file(cls):
        if not os.path.isfile(cls.__name__ + '.json'):
            return []
        else:
            with open(cls.__name__ + '.json', 'r', encoding='utf-8') as f:
                list_dicts = cls.from_json_string(f.read())
            return [cls.create(**dic) for dic in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        import csv
        try:
            csvs = [x.to_dictionary() for x in list_objs]
        except Exception:
            csvs = '[]'
        keys = csvs[0].keys()
        with open(cls.__name__ + '.csv', 'w') as f:
            writer = csv.DictWriter(f, keys)
            writer.writeheader()
            writer.writerows(csvs)

    @classmethod
    def load_from_file_csv(cls):
        import csv
        if not os.path.isfile(cls.__name__ + '.csv'):
            return []
        else:
            with open(cls.__name__ + '.csv', 'r') as f:
                reader = csv.DictReader(f)
                csvs = [row for row in reader]
                for row in csvs:
                    for key, val in row.items():
                        try:
                            row[key] = int(val)
                        except Exception:
                            pass
            return [cls.create(**dic) for dic in csvs]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turlt = turtle.Turtle()
        turlt.screen.bgcolor("#b7312c")
        turlt.pensize(3)
        turlt.shape("turtle")

        turlt.color("#ffffff")
        for rect in list_rectangles:
            turlt.showturtle()
            turlt.up()
            turlt.goto(rect.x, rect.y)
            turlt.down()
            for i in range(2):
                turlt.forward(rect.width)
                turlt.left(90)
                turlt.forward(rect.height)
                turlt.left(90)
            turlt.hideturtle()

        turlt.color("#b5e3d8")
        for square in list_squares:
            turlt.showturtle()
            turlt.up()
            turlt.goto(square.x, square.y)
            turlt.down()
            for i in range(2):
                turlt.forward(square.width)
                turlt.left(90)
                turlt.forward(square.height)
                turlt.left(90)
            turlt.hideturtle()

        turtle.exitonclick()
