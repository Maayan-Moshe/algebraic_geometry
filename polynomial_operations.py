# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 11:58:40 2015

@author: mmoshe
"""
from Monomial import Monomial
from Polynomial import Polynomial
import numpy as np

def get_S_polynomial(poly0, poly1):
    
    mono0 = poly0.terms[0]
    mono1 = poly1.terms[0]
    gamma_ex = np.maximum(mono0.exponent, mono1.exponent)
    mono_gamma = Monomial(1, gamma_ex)
    a0 = Polynomial([mono_gamma.div(mono0)])
    a1 = Polynomial([mono_gamma.div(mono1)])
    S_poly = (a0*poly0) - (a1*poly1)
    return S_poly

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