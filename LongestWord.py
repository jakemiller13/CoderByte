# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 15:21:17 2018

@author: jmiller
"""

def LongestWord(sen):
    word = ''
    new_word = ''
    for letter in sen:
        if letter.isalpha():
            new_word += letter
            if len(new_word) > len(word):
                word = new_word
        else:
            new_word = ''
    return word