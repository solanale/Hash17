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

#Functions
def read(file_name):
    
    with open(file_name, 'r') as f:
        
        data = np.array([[int(d) for d in l.split()] for l in f])
    
    return data



def main():

    # Leer fichero
    data = read(file_in)
    
    R, C, F, N, B, T = data[0]
    print(R, C, F, N, B, T)
    
    #for ride in range(1, data.shape[0]):
        
    #print(data)
    
    

if __name__ == '__main__':
    main()


