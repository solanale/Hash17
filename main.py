#!/usr/bin/python

#It's Pizza Time

#Files
file_in = "data/small.in"
file_out = "data/out.txt"

#Global vars

# N x M (char, n slice), 0
global matrix
# Slice Array, index = n slice in matrix
global slices
global solution
global row
global col
global l
global h

#Functions
def read(file_name):
    f = open(file_name, 'r')
    global row, col, l, h, matrix
    row, col, l, h = f.readline().strip().split()
    row, col, l, h = int(row), int(col), int(l), int(h)
    #Comprehension list, magia oscura
    matrix = [[(ch , 0) for ch in line.strip()] for line in f]

def write(file_name, solution):
    f = open(file_name, 'w')
    f.write(solution)

def run():
    global matrix, solution

    solution = "3\n" \
               "0 0 2 1\n" \
               "0 2 2 2\n" \
               "0 3 2 4\n"
    read(file_in)

    # Do things

    write (file_out,solution)

if __name__ == '__main__':
    run()


