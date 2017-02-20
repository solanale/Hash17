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


def encontrar_trozo():
    print "a"


def siguiente_inicio():
    print "a"

def guardar_mejor():
    print "a"

def run():
    global Row, Col, Matrix, Solution
    r1, c1, r2, c2 = 0

    read(file_in)

    while (r1 >= 0 and r2 >= 0):
        maxCol = Col
        tomates = 0
        setas = 0
        for r2 in range(r1, Row):
            for c2 in range(r2, maxCol):
                if maximoAlcanzado(r1, c1, r2, c2):
                    break
                if estaEnTrozo(r2, c2):
                    maxCol = c2 - 1
                    break
                if esTomate(r2, c2):
                    tomates = tomates + 1
                else
                    setas = setas + 1
                if minimoAlcanzado(r1, c1, r2, c2):


        r1, c1 = siguiente_inicio(r1, c1) # Devuelve -1, -1 si se sale

    write(file_out, Solution)

if __name__ == '__main__':
    run()


