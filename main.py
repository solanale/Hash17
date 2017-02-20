#!/usr/bin/python

#It's Pizza Time

#Files
file_in = "data/small.in"
file_out = "data/out.txt"

#Global vars

# N x M (char, n slice), 0
global Matrix
# Slice Array, index = n slice in matrix
global Slices
global Solution
global Row
global Col
global Min
global Max

#Functions
def read(file_name):
    f = open(file_name, 'r')
    global Row, Col, Min, Max, matrix
    Row, Col, Min, Max = f.readline().strip().split()
    Row, Col, Min, Max = int(Row), int(Col), int(Min), int(Max)
    #Comprehension list, magia oscura
    matrix = [[(ch , 0) for ch in line.strip()] for line in f]

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
    global matrix, Solution

    Solution = "3\n" \
               "0 0 2 1\n" \
               "0 2 2 2\n" \
               "0 3 2 4\n"
    read(file_in)

    #

    write (file_out,Solution)

if __name__ == '__main__':
    run()


