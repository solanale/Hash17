#!/usr/bin/python

#Files
file_in = "data/example.in"
file_out = "data/out2.txt"

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
    for linea in Matrix:
        print linea
    print Slices
    f.write(str(len(Slices)) + "\n")
    for slice in Slices:
        (n1,n2,n3,n4) = slice
        f.write(str(n1)+" "+str(n2)+" "+str(n3)+" "+str(n4)+"\n")

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


