# -*- coding: utf-8 -*-
"""
Created on Thu May 30 13:25:06 2019

@author: jmiller
"""

def TimeConvert(num): 
    h = num // 60
    m = num % 60
    num = str(h) + ':' + str(m)
    return num