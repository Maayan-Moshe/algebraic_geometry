# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 11:58:40 2015

@author: mmoshe
"""
from Monomial import Monomial
from Polynomial import Polynomial
import numpy as np

def get_single_var_poly(var_num):
    
    exponent = np.zeros((Monomial.num_of_variables), dtype=np.int)
    exponent[var_num] = 1
    mon = Monomial(1, exponent)
    ans = Polynomial([mon])
    return ans
    
def get_const_poly(coeff):
    
    exponent = np.zeros((Monomial.num_of_variables), dtype=np.int)
    mon = Monomial(coeff, exponent)
    ans = Polynomial([mon])
    return ans