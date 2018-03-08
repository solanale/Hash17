#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
import numpy as np

files = [
    ("data/a_example.in", "data/a_lost_v2_out.in"),
    ("data/b_should_be_easy.in", "data/b_lost_v2_out.in"),
    ("data/c_no_hurry.in", "data/c_lost_v2_out.in"),
    ("data/d_metropolis.in", "data/d_lost_v2_out.in"),
    ("data/e_high_bonus.in", "data/e_lost_v2_out.in"),
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

# Second version
def ride_value(data, pos, time):
    
    start = abs(pos[0] - data[0]) + abs(pos[1] - data[1])
    wait = max(0, data[4] - (time + start))
    route = abs(data[0] - data[2]) + abs(data[1] - data[3])
    
    return time + start + wait + route <= data[5], start + wait + route

# Third version
def lost_in_transfer_v1(data, pos, actual_time):
    
    time_to_go = abs(pos[0] - data[0]) + abs(pos[1] - data[1])
    wait = max(0, data[4] - (actual_time + time_to_go))
    bonus = B if actual_time + time_to_go <= data[4] else 0
    route = abs(data[0] - data[2]) + abs(data[1] - data[3])
    
    on_time = actual_time + time_to_go + wait + route <= data[5]
    lost_points = time_to_go + wait - bonus
    next_time = time_to_go + wait + route
    
    return on_time, lost_points, next_time

# Worst --> They don't give bonus if you don't finish
def lost_in_transfer_v2(data, pos, actual_time):
    
    time_to_go = abs(pos[0] - data[0]) + abs(pos[1] - data[1])
    wait = max(0, data[4] - (actual_time + time_to_go))
    bonus = B if actual_time + time_to_go <= data[4] else 0
    route = abs(data[0] - data[2]) + abs(data[1] - data[3])
    
    on_time = actual_time + time_to_go + wait + route <= data[5]
    if on_time:
        lost_points = time_to_go + wait - bonus
    else:
        lost_points = time_to_go + wait + route - bonus
    
    used_time = time_to_go + wait + route
    out_of_time = actual_time + used_time <= T
    
    return out_of_time, lost_points, used_time

def run(file_in, file_out):
    
    global R, C, F, N, B, T
    
    # Read file
    data = read(file_in)
    
    #print(R, C, F, N, B, T)
    
    # for the vehicles rides
    vehicles = np.array(
        [[0 for n in range(N + 1)] for v in range(F)]).astype(int)
    
    #data = data[data[:,4].argsort()]
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
                    found, lost_points, actual_time = lost_in_transfer(
                                                        data[actual_ride],
                                                        pos,
                                                        time)
                actual_ride += 1
                
            
            if not found:
                has_time = False
            else:
                actual_ride -= 1
                for ride in range(actual_ride + 1, data.shape[0]):
                    if free[ride]:
                        ok, ride_lost_points, ride_time = lost_in_transfer(
                                                            data[ride],
                                                            pos,
                                                            time)
                        if ok and ride_lost_points < lost_points:
                            actual_ride = ride
                            actual_time = ride_time
                            lost_points = ride_lost_points
                
                # asign ride to vehicle
                vehicle_rides = vehicles[vehicle][0]
                vehicles[vehicle][vehicle_rides + 1] = actual_ride
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


