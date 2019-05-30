# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 15:40:06 2019

@author: jmiller
"""

def SimpleSymbols(input_str):
    for letter in range(len(input_str)):
        if input_str[letter].isalpha():
            if letter == 0:
                return 'false'
            if input_str[letter - 1] == '+' and input_str[letter + 1] == '+':
                pass
            else:
                return 'false'
    return 'true'
        