#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
import numpy as np

#Files
files = [
    ("data/a_example.in", "data/a_out2.in"),
    ("data/b_should_be_easy.in", "data/b_out2.in"),
    ("data/c_no_hurry.in", "data/c_out2.in"),
    ("data/d_metropolis.in", "data/d_out2.in"),
    ("data/e_high_bonus.in", "data/e_out2.in"),
]

global R, C, F, N, B, T

#Functions
def read(file_name):
    
    global R, C, F, N, B, T
    
    with open(file_name, 'r') as f:
        
        R, C, F, N, B, T = np.array(f.readline().split()).astype(int)
        
        data = np.array([[int(d) for d in l.split()] for l in f])
    
    return data

def print_rides(file_out, vehicles):
    
    with open(file_out, 'w') as f: 
        
        for v in range(vehicles.shape[0]):
            
            print(vehicles[v][0], end=" ")
            f.write("{} ".format(vehicles[v][0]))
            
            for ride in range(1, vehicles[v][0] + 1):
                print(vehicles[v][ride], end=" ")
                f.write("{} ".format(vehicles[v][ride]))
                
            print("")
            f.write("\n")

def ride_value(data, pos, time):
    
    correct = False
    
    wait = max(0, data[4] - time)
    
    route = abs(data[0] - data[2]) + abs(data[1] - data[3])
    start = abs(pos[0] - data[0]) + abs(pos[1] - data[1])
    dist = route + start
    
    return time + wait + dist <= data[5], wait + dist

def run(file_in, file_out):
    
    global R, C, F, N, B, T
    
    # Read file
    data = read(file_in)
    
    #print(R, C, F, N, B, T)
    
    # for the vehicles rides
    vehicles = np.array(
        [[0 for n in range(N + 1)] for v in range(F)]).astype(int)
    
    data2 = np.zeros((data.shape[0], data.shape[1] + 1), dtype=int)
    for i in range(data.shape[0]):
        data2[i] = np.append(data[i], [i])
    
    data = data2[data2[:,4].argsort()]
    
    free = [True for i in range(data.shape[0])]
    
    for vehicle in range(F):
        has_time = True
        pos = (0, 0)
        time = 0
        while has_time:
            
            # take first free
            found = False
            actual_ride = 0
            while not found and actual_ride < data.shape[0]:
                if free[actual_ride]:
                    found, actual_time = ride_value(data[actual_ride],
                                                    pos,
                                                    time)
                actual_ride += 1
                
            
            if not found:
                has_time = False
            else:
                actual_ride -= 1
                for ride in range(actual_ride + 1, data.shape[0]):
                    if free[ride]:
                        ok, ride_time = ride_value(data[ride],
                                                   pos,
                                                   time)
                        if ok and ride_time < actual_time:
                            actual_ride = ride
                            actual_time = ride_time
                
                # asign ride to vehicle
                vehicle_rides = vehicles[vehicle][0]
                vehicles[vehicle][vehicle_rides + 1] = data[actual_ride][6]
                vehicles[vehicle][0] += 1
                pos = (data[actual_ride][2], data[actual_ride][3])
                time += actual_time
                free[actual_ride] = False
    
    print_rides(file_out, vehicles)

def main():
    
    for file_in, file_out in files:
        run(file_in, file_out)

if __name__ == '__main__':
    main()


