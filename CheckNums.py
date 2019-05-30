# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 14:52:35 2019

@author: jmiller
"""

def CheckNums(num1, num2):
    if num2 > num1:
        return 'true'
    elif num1 == num2:
        return '-1'
    else:
        return 'false'