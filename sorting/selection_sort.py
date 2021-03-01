#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" Selection sort
1. Find a maximum value in the array using linear search
2. Swap the maximum value with the last unsorted element
3. Consider the last element sorted
4. Repeat for the unsorted elements

Time complexity:
    * best      O(n^2)
    * average   O(n^2)
    * worst     O(n^2)
"""

__author__ = "Magdalena Gawlinska"
__copyright__ = ""
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Magdalena Gawlinska"
__email__ = ""
__status__ = "Prototype"

from random import randint

def linear_search(array):
    max_element = array[0]
    idx = 0
    for i in range(len(array)):
        if array[i] > max_element:
            max_element = array[i]
            idx = i
    return idx

def selection_sort(array):
    for i in range(len(array)):
        if i == 0:
            idx = linear_search(array[None:None])
        else:
            idx = linear_search(array[:-i])
        array[-i-1], array[idx] = (array[idx], array[-i-1])

        print(f"Selection sort. Pass: {i + 1} list: {array}")

list_length = 10
factor = 10

to_sort = [randint(0, list_length * factor) for x in range(list_length)]

print(f"Array: {to_sort}")

selection_sort(to_sort)