#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" Bubble sort
1. Without early termination
Compare two adjacent items in a list
    * if out of order - swap
Continue till the end of the list;
The last element occupies its correct position,
thus excluded from the next pass
Repeat for n-passes

2. With early termination
Compare two adjacent items in a list
    * if out of order - swap
Continue till the end of the list;
The last element occupies its correct position,
thus excluded from the next pass
Terminate if there's been no swaps

Time complexity:
    * best      O(n) (with early stop)
    * average   O(n^2)
    * worst     O(n^2)
"""

# authorship information; metadata
__author__ = "Magdalena Gawlinska"
__copyright__ = ""
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Magdalena Gawlinska"
__email__ = ""
__status__ = "Prototype"

from random import randint

def bubble_sort(to_sort: list):
    for i in range(len(to_sort)):
        for j in range(len(to_sort) - i - 1):
            if to_sort[j] < to_sort[j + 1]:
                continue
            to_sort[j], to_sort[j + 1] = (to_sort[j + 1], to_sort[j])
        print(f"Bubble sort. Pass: {i + 1} list: {to_sort}")

def bubble_sort_early_stop(to_sort: list):
    for i in range(len(to_sort)):
        count_swap = 0
        for j in range(len(to_sort) - i - 1):
            if to_sort[j] < to_sort[j + 1]:
                continue
            to_sort[j], to_sort[j + 1] = (to_sort[j + 1], to_sort[j])
            count_swap += 1
        if count_swap == 0:
            break
        print(f"Bubble sort with early stop. Pass: {i + 1} list: {to_sort}")

list_lenght = 10
factor = 10

to_sort = [randint(0, list_lenght * factor) for x in range(list_lenght)]

bubble_sort(to_sort)

to_sort = [randint(0, list_lenght * factor) for x in range(list_lenght)]

bubble_sort_early_stop(to_sort)

