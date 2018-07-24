#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 13:28:21 2018

@author: kusal
"""

from random import randint
import time

#------------------------------------Binary search algorithm------------------------

def binary_search(arr, start, end, element):
    if(start <= end):
        rand_integer = int((start + end) / 2)
        if arr[rand_integer] == element:
            return rand_integer
        else:
            if element < arr[rand_integer]:
                return binary_search(arr, start, rand_integer - 1, element)
            else:
                return binary_search(arr, rand_integer + 1, end, element)
    else:
        return -1

#---------------------------Randomized binary search algorithm----------------------
def randomized_binary_search(arr, start, end, element):
    if(start<=end):
        rand_integer = randint(start, end)
        if arr[rand_integer] == element:
            return rand_integer
        else:
            if element < arr[rand_integer]:
                return randomized_binary_search(arr, start, rand_integer - 1, element)
            else:
                return randomized_binary_search(arr, rand_integer + 1, end, element)
    else:
        return -1

#------------------------------------Initialization of Arrays----------------------
def initialize_array(size):
    i = 0
    n = 0
    array = []
    members_array = []
    temp = []
    non_members_count = 0
    members_count = 0

    member_gap = size / 700

    while (i<size):
        if randint(0, 1):
            array.append(n)
            if members_count < 700 and i % member_gap == 0:
                members_array.append(n)
                members_count += 1
            i += 1
        else:
            temp.append(n)
            non_members_count += 1
        n += 1

    while (non_members_count<300):
        if randint(0, 1):
            temp.append(n)
            non_members_count += 1
        n += 1
    non_member_gap = int(len(temp) / 300)
    non_members_array = [temp[i * non_member_gap] for i in range(300)]

    return array, non_members_array, members_array


for i in range(3):
    array_size = 10 ** (5+i)
    print("Input Array " + str(10)+'^'+str(5+i)+ "...................")
    
    array, non_members, members = initialize_array(array_size)

    start_time = time.time()
    for j in members:
        binary_search(array, 0, array_size - 1, j)

    for j in non_members:
        binary_search(array, 0, array_size - 1, j)
    end_time = time.time()

    print("Binary Search : Time(microseconds) : " + str(
        1000000 * (end_time - start_time) / 1000))
    print("")

    start_time = time.time()
    for j in members:
        randomized_binary_search(array, 0, array_size - 1, j)

    for j in non_members:
        randomized_binary_search(array, 0, array_size - 1, j)
    end_time = time.time()

    print("Randomized Binary Search : Time(microseconds) : " + str(
        1000000 * (end_time - start_time) / 1000))
    print("")