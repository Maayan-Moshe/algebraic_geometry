# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from monomial_operations import monomial_lex

class Monomial:
    
    num_of_variables = 3
    monom_comparator = monomial_lex
    field_type = float
    
    def __init__(self, coeff = 0, exponent = np.zeros((num_of_variables,), dtype=np.int)):
        
        self.coeff = self.field_type(coeff)
        self.exponent = np.array(exponent, dtype = np.int)
        
    def is_dividable(self, other):
        
        return np.min(self.exponent - other.exponent) >= 0
        
    def __mul__(self, other_mon):
        
        ans_coeff = self.coeff * other_mon.coeff
        ans_exp = self.exponent + other_mon.exponent
        return Monomial(ans_coeff, ans_exp)
        
    def div(self, other_mon):
        
        assert self.is_dividable(other_mon)
        ans_coeff = self.coeff / other_mon.coeff
        ans_exp = self.exponent - other_mon.exponent
        return Monomial(ans_coeff, ans_exp)
        
    def __add__(self, other):
        
        assert np.linalg.norm(self.exponent - other.exponent) == 0
        return Monomial(self.coeff + other.coeff, self.exponent)
        
    def __sub__(self, other):
        
        return self + (-other)
        
    def __neg__(self):
        
        return Monomial(-self.coeff, self.exponent)
        
    def __str__(self):
        
        return str(self.coeff) + '*x^' + str(self.exponent)
        
    def __repr__(self):
        
        return self.__str__()
        
    def __gt__(A, B):
        
        return Monomial.monom_comparator(A, B) == 1
        
    def __lt__(A, B):
        
        return Monomial.monom_comparator(A, B) == -1
        
    def equal_val(A, B):
        
        if Monomial.monom_comparator(A, B) == 0 and A.coeff == B.coeff:
            return True
        return False