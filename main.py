#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Files
file_in = "data/me_at_the_zoo.in"
file_out = "data/out.txt"

#Global vars

global NVIDEOS, NENDPOINTS, NPETICIONES, NSERVERS, CAPACIDAD
global Videos, Endpoints, Peticiones, Caches
global Solucion, Final


#Functions
def read(file_name):
    f = open(file_name, 'r')

    global NVIDEOS, NENDPOINTS, NPETICIONES, NSERVERS, CAPACIDAD
    global Videos, Endpoints, Peticiones, Caches
    NVIDEOS, NENDPOINTS, NPETICIONES, NSERVERS, CAPACIDAD = f.readline().strip().split()
    print NVIDEOS, NENDPOINTS, NPETICIONES, NSERVERS, CAPACIDAD
    Videos = f.readline().strip().split()
    print "Videos"
    print Videos

    Endpoints = []
    Peticiones = []
    Caches = []
    for x in range(0,int(NSERVERS)):
        Caches.append([])
    for x in range(0,int(NENDPOINTS)):
        Ld, K = f.readline().strip().split()
        Endpoints.append((Ld, []))
        for y in range (0, int(K)):
            (_, array) = Endpoints[x]
            aux = f.readline().strip().split()
            array.append(aux)
            Caches[int(aux[0])].append((x,aux[1]))
        Peticiones.append([])
    print "Endpoints"
    print Endpoints
    print "Caches"
    print Caches

    for x in range (0, int(NPETICIONES)):
        Rv, Re, Rn = f.readline().strip().split()
        Peticiones[int(Re)].append((int(Rv), int(Rn)))
    for n in range (0, int(NSERVERS)):
        Peticiones[n] = sorted(Peticiones[n], key=lambda x: x[1], reverse=True)
    print "Peticiones"
    print Peticiones

    #Comprehension list, magia oscura
    # Matrix = [[(ch , 0) for ch in line.strip()] for line in f]

def write(file_name):
    global Final
    f = open(file_name, 'w')
    f.write(str(Final.pop(0)) + "\n")
    for line in Final:
        f.write(str(line[0]) + " " + " ".join(str(x) for x in line[1]) + "\n")
    #f write len del array

    #f write

    # f.write(str(len(Slices)) + "\n")
    # for slice in Slices:
    #     (n1,n2,n3,n4) = slice
    #     f.write(str(n1)+" "+str(n2)+" "+str(n3)+" "+str(n4)+"\n")

def formatSolucion():
    global Solucion, Final
    Final = [0]
    for x in range(0, len(Solucion)):
        Final.append([x, Solucion[x]])
    Final[0] = len(Final)-1

def run():

    # Leer fichero
    read(file_in)

    # Do things

    write (file_out)

if __name__ == '__main__':
    run()


