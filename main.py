#!/usr/bin/python

#It's Pizza Time

#Files
file_in = "data/small.in"
file_out = "data/out.txt"

#Global vars

# N x M (char, n slice), 0
global Matrix
# Slice Array, index = n slice in Matrix
global Slices
global Solution
global Row
global Col
global Min
global Max

#Functions
def read(file_name):
    f = open(file_name, 'r')
    global Row, Col, Min, Max, Matrix
    Row, Col, Min, Max = f.readline().strip().split()
    Row, Col, Min, Max = int(Row), int(Col), int(Min), int(Max)
    #Comprehension list, magia oscura
    Matrix = [[(ch , 0) for ch in line.strip()] for line in f]

def write(file_name, Solution):
    f = open(file_name, 'w')
    f.write(Solution)

# Busca la siguiente celda para comenzar un trozo
def siguiente_inicio(r1,c1):
    global Matrix
    if(r1==(Row-1) and c1==(Col-1)):


    _,used = Matrix[r1+1,]
    return -1, -1

# Mira si ese trozo supera el tamano permitido
def maximoAlcanzado(r1,c1,r2,c2):
    global Max
    size = (r2-r1)*(c2-c1)
    if (size>Max):
        return True
    else:
        return False

# Mira si la celda es tomate
def esTomate(r2,c2):
    global Matrix
    food, _ =  Matrix[r2][c2]
    if (food == "T"):
        return True
    else:
        return False

def run():
    global Row, Col, Matrix, Solution
    r1, c1, r2, c2 = 0
    trozoActual = 1

    read(file_in)

    # Hasta que nos salgamos del tablero
    while (r1 >= 0 and r2 >= 0):

        # Límite de la iteración horizontal
        maxCol = Col

        # Cantidad de tomates y setas
        tomates = 0
        setas = 0

        # Mejor trozo por el momento
        r2Mejor = -1
        c2Mejor = -1

        for r2 in range(r1, Row):
            for c2 in range(r2, maxCol):

                # Si nos pasamos del máximo, salimos
                if maximoAlcanzado(r1, c1, r2, c2):
                    break

                # Si ya está en un trozo, salimos y actualizamos el límite de la iteración horizontal
                if estaEnTrozo(r2, c2):
                    maxCol = c2 - 1
                    break

                # Actualizamos el valor de tomates o setas
                if esTomate(r2, c2):
                    tomates = tomates + 1
                else
                    setas = setas + 1

                # Si alcanzamos el mínimo, actualizamos el trozo
                if minimoAlcanzado(tomates, setas):
                    r2Actual, c2Actual = mejorOpcion(r1, c1, r2Mejor, c2Mejor, r2, c2)
                    break

        for i in range(r1, r2):
            for j in range(c1, c2):
                Matrix[i][j] = (_, trozoActual)

        r1, c1 = siguiente_inicio(r1, c1) # Devuelve -1, -1 si se sale

    write(file_out, Solution)

if __name__ == '__main__':
    run()


