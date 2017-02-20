#!/usr/bin/env python
# -*- coding: utf-8 -*-

#It's Pizza Time

#Files
file_in = "data/example.in"
file_out = "data/out.txt"

#Global vars

# N x M (char, n slice), 0
global Matrix
# Slice Array, index = n slice in Matrix
global Slices
global Solution
global ROW
global COL
global MIN
global MAX

#Functions
def read(file_name):
    f = open(file_name, 'r')
    global ROW, COL, MIN, MAX, Matrix
    ROW, COL, MIN, MAX = f.readline().strip().split()
    ROW, COL, MIN, MAX = int(ROW), int(COL), int(MIN), int(MAX)
    #Comprehension list, magia oscura
    Matrix = [[(ch , 0) for ch in line.strip()] for line in f]

def write(file_name):
    global Slices
    f = open(file_name, 'w')
    print Matrix
    print Slices
    # f.write(Slices)

# Busca la siguiente celda para comenzar un trozo
def siguienteInicio(r1,c1):
    global Matrix
    if(r1==(ROW-1) and c1==(COL-1)):
        # Fin de la matriz
        return -1,-1
    if(c1==(COL-1)):
        (_,used) = Matrix[r1+1][0]
        if (used>0):
            return siguienteInicio(r1+1,0)
        else:
            return (r1+1),c1
    else:
        (_,used) = Matrix[r1][c1+1]
        if (used>0):
            return siguienteInicio(r1,c1+1)
        else:
            return r1,(c1+1)

# Mira si ese trozo supera el tamano permitido
def maximoAlcanzado(r1,c1,r2,c2):
    global MAX
    size = (r2-r1+1)*(c2-c1+1)
    if (size>MAX):
        return True
    else:
        return False

# Mira si la celda es tomate
def esTomate(r2,c2):
    global Matrix
    (food, _) =  Matrix[r2][c2]
    if (food == "T"):
        return True
    else:
        return False

#r2,c2 es la celda a comprobar ahora. En la primera iteracion, r2mejor y c2mejor valen -1.
#Mejor trozo= menor n celdas o igual n de celdas Y mas cuadrado
def mejorOpcion(r1, c1, r2mejor, c2mejor, r2, c2):
    if(r2mejor == -1):
        return r2, c2
    else:
        numCeldasMejor = (r2mejor - r1 + 1) * (c2mejor - c1 + 1)
        numCeldasActual = (r2 - r1 + 1) * (c2 - c1 + 1)
        if(numCeldasActual < numCeldasMejor):
            return r2, c2
        elif(numCeldasActual > numCeldasMejor):
            return r2mejor, c2mejor
        else:
            difMejor = r2mejor - r1 + (c2mejor - c1)
            difActual = r2 - r1 + (c2 - c1)
            if(difActual <= difMejor):
                return r2, c2
            else:
                return r2mejor, c2mejor

def estaEnTrozo(r, c):

    (_, libre) = Matrix[r][c]
    # 0= no esta en ningun trozo
    if(libre == 0):
        return False
    else:
        return True

def minimoAlcanzado(tomates, setas):
    global Matrix, MIN

    if(tomates >= MIN and setas >= MIN):
        return True
    else:
        return False

def run():
    global ROW, COL, Matrix, Slices
    r1, c1, r2, c2 = 0, 0, 0, 0
    trozoActual = 0
    Slices = [0]
    read(file_in)

    # Hasta que nos salgamos del tablero
    while (r1 >= 0 and c1 >= 0):

        # Limite de la iteración horizontal
        maxCOL = COL

        # Mejor trozo por el momento
        r2Mejor = -1
        c2Mejor = -1

        for r2 in range(r1, ROW):

            # Cantidad de tomates y setas
            setas = 0
            tomates = 0

            for c2 in range(c1, maxCOL):

                # Si nos pasamos del maximo, salimos
                if maximoAlcanzado(r1, c1, r2, c2):
                    break

                # Si ya esta en un trozo, salimos y actualizamos el limite de la iteracion horizontal
                if estaEnTrozo(r2, c2):
                    maxCOL = c2 - 1
                    break

                # Actualizamos el valor de tomates o setas
                if esTomate(r2, c2):
                    tomates = tomates + 1
                else:
                    setas = setas + 1

                # Si alcanzamos el mínimo, actualizamos el trozo
                if minimoAlcanzado(tomates, setas):
                    r2Mejor, c2Mejor = mejorOpcion(r1, c1, r2Mejor, c2Mejor, r2, c2)
                    break

        # Si hemos completado un trozo
        if (r2Mejor >= 0 and c2Mejor >= 0):

            # Siguiente trozo
            trozoActual = trozoActual + 1

            # Añadimos el trozo a la solución
            Slices[0] = Slices[0] + 1
            Slices.append((r1, c1, r2Mejor, c2Mejor))

            # Actualizamos el valor de cada celda del trozo
            for i in range(r1, r2Mejor + 1):
                for j in range(c1, c2Mejor + 1):
                    Matrix[i][j] = (Matrix[i][j][0], trozoActual)

        # Tomamos el siguiente inicio
        r1, c1 = siguienteInicio(r1, c1)

    # Volcamos la solución
    write(file_out)

if __name__ == '__main__':
    run()
