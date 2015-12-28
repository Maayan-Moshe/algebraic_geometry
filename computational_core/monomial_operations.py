# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 13:31:20 2015

@author: mmoshe
"""

import numpy as np

def monomial_lex(monom0, monom1):
    
    diff = monom0.exponent - monom1.exponent
    for a in diff:
        if a > 0:
            return 1
        if a < 0:
            return -1
    return 0
    
def monomial_grlex(monom0, monom1):
    
    diff = monom0.exponent - monom1.exponent
    sum_diff = np.sum(diff)
    if sum_diff > 0:
        return 1 
    if sum_diff < 0:
        return -1
    return monomial_lex(monom0, monom1)
    
    