#!/usr/bin/env python3
'''
Module that type annotates sum_list
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
        Function that takes a list input_list of floats as argument and returns
        their sum as float
    '''
    return sum(input_list)
