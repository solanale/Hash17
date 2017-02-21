#!/usr/bin/env python
# -*- coding: utf-8 -*-

#It's Pizza Time

#Files
file_in = "data/example.in"
file_out = "data/out.txt"

#Global vars

# N x M (char, n slice), 0
global Matrix
# Lista con los tipos de trozos
global tipoTrozos
# Slice Array, index = n slice in Matrix
global Slices
global Solution
global ROW
global COL
global MIN
global MAX

#Functions

def generaTrozos(min, max):
    for i in range(1, max):
        for j in range(1, max):
            if ():
                tipoTrozos.append()

def read(file_name):
    f = open(file_name, 'r')
    global ROW, COL, MIN, MAX, Matrix
    ROW, COL, MIN, MAX = f.readline().strip().split()
    ROW, COL, MIN, MAX = int(ROW), int(COL), int(MIN), int(MAX)

    # Generamos la lista de formas posibles
    generaTrozos(MIN, MAX)

    #Comprehension list, magia oscura
    Matrix = [[(ch , 0) for ch in line.strip()] for line in f]

def write(file_name):
    global Slices
    f = open(file_name, 'w')
    print Matrix
    print Slices
    # f.write(Slices)

def run():
    global ROW, COL, Matrix, Slices
    r1, c1, r2, c2 = 0, 0, 0, 0
    trozoActual = 0
    Slices = [0]
    read(file_in)



    # Volcamos la solución
    write(file_out)

if __name__ == '__main__':
    run()
