#!/usr/bin/python

#Files
file_in = "data/me_at_the_zoo.in"
file_out = "data/out.txt"

#Global vars

global NVIDEOS, NENDPOINTS, NPETICIONES, NSERVERS, CAPACIDAD
global Videos, Endpoints, Peticiones


#Functions
def read(file_name):
    f = open(file_name, 'r')
    global NVIDEOS, NENDPOINTS, NPETICIONES, NSERVERS, CAPACIDAD
    global Videos, Endpoints, Peticiones
    NVIDEOS, NENDPOINTS, NPETICIONES, NSERVERS, CAPACIDAD = f.readline().strip().split()
    print NVIDEOS, NENDPOINTS, NPETICIONES, NSERVERS, CAPACIDAD
    Videos = f.readline().strip().split()
    print Videos
    Endpoints = []
    for x in range(0,int(NENDPOINTS)):
        Ld, K = f.readline().strip().split()
        Endpoints.append((Ld, []))
        for y in range (0, int(K)):
            (_, array) = Endpoints[x]
            array.append(f.readline().strip().split())
    print Endpoints
    Peticiones = []
    for x in range (0, int(NPETICIONES)):
        Rv, Re, Rn = f.readline().strip().split()
        Peticiones.append((Rv, Re, Rn))
    print Peticiones
    #Comprehension list, magia oscura
    # Matrix = [[(ch , 0) for ch in line.strip()] for line in f]

def write(file_name):
    global Slices
    f = open(file_name, 'w')
    f.write(str(len(Slices)) + "\n")
    for slice in Slices:
        (n1,n2,n3,n4) = slice
        f.write(str(n1)+" "+str(n2)+" "+str(n3)+" "+str(n4)+"\n")

def run():

    # Leer fichero
    read(file_in)

    # Do things

    write (file_out)

if __name__ == '__main__':
    run()


