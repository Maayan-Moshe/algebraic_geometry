# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 11:58:40 2015

@author: mmoshe
"""
from Monomial import Monomial
from Polynomial import Polynomial
import numpy as np

def get_S_polynomial(poly0, poly1):
    
    gamma_ex = np.maximum(poly0.get_multidegree(), poly1.get_multidegree())
    poly_gamma = Polynomial([Monomial(1, gamma_ex)])
    a0 = poly_gamma.divide_by_leading_term(poly0)
    a1 = poly_gamma.divide_by_leading_term(poly1)
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