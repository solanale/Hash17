#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

#Files
file_in = "data/a_example.in"
# file_in = "data/b_should_be_easy.in"
# file_in = "data/c_no_hurry.in"
# file_in = "data/d_metropolis.in"
# file_in = "data/e_high_bonus.in"

file_out = "data/out.txt"

#Global vars

global NVIDEOS, NENDPOINTS, NPETICIONES, NSERVERS, CAPACIDAD
global Videos, Endpoints, Peticiones, Caches, Ganancias
global Solucion, Final


#Functions
def read(file_name):
    
    with open(file_name, 'r') as f:
        
        data = [[int(d) for d in l.split()] for l in f]
    
    return data
    
def write(file_name):
    global Final
    f = open(file_name, 'w')
    f.write(str(Final.pop(0)) + "\n")
    for line in Final:
        f.write(str(line[0]) + " " + " ".join(str(x) for x in line[1]) + "\n")


def formatSolucion():
    global Solucion, Final
    Final = [0]
    for x in range(0, len(Solucion)):
        if len(Solucion[x]) > 0:
            Final.append([x, Solucion[x]])
    Final[0] = len(Final)-1

def main():

    # Leer fichero
    data = read(file_in)
    
    print(data)

if __name__ == '__main__':
    main()


