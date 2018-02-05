#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Functions and Exceptions"""

class ListDivideException(Exception):
    """ A Divide Exception has occured"""

def listDivide(numbers, divide = 2):

    num = []
    for i in num:
        if i % divide == 0:
            num.append(i)
    return len(num)

def testListDivide():
    test = [([1, 2, 3, 4, 5]),
            ([2, 4, 6, 8, 10]),
            ([30, 54, 63, 98, 100]),
            ([]),
            ([1, 2, 3, 4, 5], 1)
            ]
    for i in test:
        if listDivide != divide:
            raise ListDivideException('Test Failed')
        
    

