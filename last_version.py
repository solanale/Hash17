#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
import numpy as np

files = [
    ("data/a_example.in", "data/a_lost_out.in"),
    ("data/b_should_be_easy.in", "data/b_lost_out.in"),
    ("data/c_no_hurry.in", "data/c_lost_out.in"),
    ("data/d_metropolis.in", "data/d_lost_out.in"),
    ("data/e_high_bonus.in", "data/e_lost_out.in"),
]

global R, C, F, N, B, T

# Read data
def read(file_name):
    
    global R, C, F, N, B, T
    
    with open(file_name, 'r') as f:
        
        R, C, F, N, B, T = np.array(f.readline().split()).astype(int)
        
        data = np.array([[int(d) for d in l.split()] for l in f])
    
    return data

# Write to files
def print_rides(file_out, vehicles):
    
    with open(file_out, 'w') as f: 
        
        for v in range(vehicles.shape[0]):
            
            f.write("{} ".format(vehicles[v][0]))
            
            for ride in range(1, vehicles[v][0] + 1):
                f.write("{} ".format(vehicles[v][ride]))
            
            f.write("\n")

# Heuristic function
def lost_in_transfer(data, pos, actual_time):
    
    time_to_go = abs(pos[0] - data[0]) + abs(pos[1] - data[1])
    wait = max(0, data[4] - (actual_time + time_to_go))
    bonus = B if actual_time + time_to_go <= data[4] else 0
    route = abs(data[0] - data[2]) + abs(data[1] - data[3])
    
    on_time = actual_time + time_to_go + wait + route <= data[5]
    lost_points = time_to_go + wait - bonus
    used_time = time_to_go + wait + route
    
    return on_time, lost_points, used_time

# Principal function
def run(file_in, file_out):
    
    global R, C, F, N, B, T
    
    # Read file
    data = read(file_in)
    
    # for the vehicles rides
    vehicles = np.array(
        [[0 for n in range(N + 1)] for v in range(F)]).astype(int)
    
    # free rides
    free = [True for i in range(data.shape[0])]
    
    # fill each vehicle
    for vehicle in range(F):
        
        has_time = True
        pos = (0, 0)
        time = 0
        while has_time:
            
            # take first free ride
            found = False
            actual_ride = 0
            while not found and actual_ride < data.shape[0]:
                if free[actual_ride]:
                    found, lost_points, actual_time = lost_in_transfer(
                                                        data[actual_ride],
                                                        pos,
                                                        time)
                actual_ride += 1
                
            # Try to improve selection
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
                
                # asign best ride to vehicle
                vehicle_rides = vehicles[vehicle][0]
                vehicles[vehicle][vehicle_rides + 1] = actual_ride
                vehicles[vehicle][0] += 1
                pos = (data[actual_ride][2], data[actual_ride][3])
                time += actual_time
                free[actual_ride] = False
    
    print_rides(file_out, vehicles)

# For each file
def main():
    
    for file_in, file_out in files:
        run(file_in, file_out)

if __name__ == '__main__':
    main()


