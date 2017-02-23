#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Files
file_in = "data/me_at_the_zoo.in"
file_out = "data/out.txt"

#Global vars

global NVIDEOS, NENDPOINTS, NPETICIONES, NSERVERS, CAPACIDAD
global Videos, Endpoints, Peticiones, Caches, Ganancias
global Solucion, Final


#Functions
def read(file_name):
    f = open(file_name, 'r')

    global NVIDEOS, NENDPOINTS, NPETICIONES, NSERVERS, CAPACIDAD
    global Videos, Endpoints, Peticiones, Caches
    NVIDEOS, NENDPOINTS, NPETICIONES, NSERVERS, CAPACIDAD = f.readline().strip().split()
    NVIDEOS, NENDPOINTS, NPETICIONES, NSERVERS, CAPACIDAD = int(NVIDEOS), int(NENDPOINTS), int(NPETICIONES), int(NSERVERS), int(CAPACIDAD)
    print NVIDEOS, NENDPOINTS, NPETICIONES, NSERVERS, CAPACIDAD
    Videos = f.readline().strip().split()
    Videos = [int(i) for i in Videos]
    print "Videos"
    print Videos

    Endpoints = []
    Peticiones = []
    Caches = []
    for x in range(0,int(NSERVERS)):
        Caches.append([])
    for x in range(0,int(NENDPOINTS)):
        Ld, K = f.readline().strip().split()
        Endpoints.append((int(Ld), []))
        for y in range (0, int(K)):
            (_, array) = Endpoints[x]
            aux = f.readline().strip().split()
            aux = [int(i) for i in aux]
            array.append(aux)
            Caches[int(aux[0])].append((int(x),int(aux[1])))
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
        Final.append([x, Solucion[x]])
    Final[0] = len(Final)-1

def run():

    # Leer fichero
    read(file_in)

    global NVIDEOS, NENDPOINTS, NPETICIONES, NSERVERS, CAPACIDAD
    global Videos, Endpoints, Peticiones, Caches, Ganancias
    global Solucion, Final

    Solucion = []
    Ganancias = []

    for x in range (0, int(NSERVERS)):
        Solucion.append([])

    for c in range(0,len(Caches)):
        listaEnd = Caches[c]
        for (end, latenciaCache) in listaEnd:
            if(len(Peticiones[end]) > 0):
                latenciaCD = Endpoints[end][0]
                (idVideo, numPeticiones) = Peticiones[end][0]   #cogemos el video que mas requests tiene
                ganancia = (latenciaCD - latenciaCache)*numPeticiones
                Ganancias.append((end, int(ganancia)))
        Ganancias = sorted(Ganancias, key=lambda g: g[1], reverse=True)

        tengoEspacio = True
        espacio = CAPACIDAD
        while(tengoEspacio and len(Ganancias) > 0):

            (end, _) = Ganancias.pop(0)
            # saco el video seleccionado
            idVideo = Peticiones[end][0][0]
            if(Videos[idVideo] <= espacio):
                Peticiones[end].pop()
                if (not(idVideo in Solucion[c])):
                    Solucion[c].append(idVideo)
                    espacio = espacio - Videos[idVideo]
                # tomo el siguiente video del endpoint
                if (len(Peticiones[end]) > 0):
                    (idVideo, numPeticiones) = Peticiones[end][0]
                    ganancia = (latenciaCD - latenciaCache) * numPeticiones
                    Ganancias.append((end, int(ganancia)))
                    Ganancias = sorted(Ganancias, key=lambda g: g[1], reverse=True)
            else:
                if (len(Ganancias) == 0):
                    tengoEspacio = False

    print Solucion
    formatSolucion()
    write (file_out)

if __name__ == '__main__':
    run()


