# Lista de elementos de uso facil o notorio


def main():

    # Open Files
    f = open("data/small.in", 'r') # r - read, w - write, a - append, r+ both reading and writing

    # Comprehension list
    Matrix = [[(ch , 0) for ch in line.strip()] for line in f]


    # Python dictionary is a built-in type that supports key-value pairs.
    streetno = {"1": "Sachine Tendulkar", "2": "Dravid", "3": "Sehwag", "4": "Laxman", "5": "Kohli"}
    # as well as dict
    streetno = dict({"1":"Sachine Tendulkar", "2":"Dravid"})
    # or
    streetno = {}
    streetno["1"] = "Sachine Tendulkar"


    import numpy as np




