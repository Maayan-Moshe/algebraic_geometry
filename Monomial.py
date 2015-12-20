# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

class Monomial:
    
    num_of_variables = 3
    
    def __init__(self, coeff = 0, exponet = np.zeros(num_of_variables)):
        
        self.coeff = coeff
        self.exponet = exponet
        
    def __mul__(self, other_mon):
        
        ans_coeff = self.coeff * other_mon.coeff
        ans_exp = self.exponet + other_mon.exponet
        return Monomial(ans_coeff, ans_exp)
        
    def __add__(self, other):
        
        assert np.linalg.norm(self.exponet - other.exponent) < 1e-8
        return Monomial(self.coeff + other.coeff, self.exponet)
        
    def __str__(self):
        
        return str(self.coeff) + '*x^' + str(self.exponet)
        
    def __repr__(self):
        
        return self.__str__()
        
    def __gt__(A, B):
        
        monomial_lex(A, B) == -1
        
    def __lt__(A, B):
        
        monomial_lex(A, B) == 1
        
def monomial_lex(monom0, monom1):
    
    diff = monom0.exponet - monom1.exponet
    for a in diff:
        if a > 0:
            return 1
        if a < 0:
            return -1
    return 0
        
class Polynomial:
    
    def __init__(self, terms = list()):
        
        import pdb
        pdb.set_trace()
        self.terms = sorted(terms, reverse=True)
    
    def __add__(self, other):
        
        ans = list()
        index0 = 0
        index1 = 0
        while index0 < len(self.terms) and index1 < len(other.terms):
            index0, index1 = add_term(self.terms, other.terms, 
                                      index0, index1, ans, self.monomial_order)
        ans.append(self.terms[index0:])
        ans.append(other.terms[index1:])
        return Polynomial(ans)
        
    def __str__(self):
        
        return str(self.terms)
        
    def __repr__(self):
        
        return self.__str__()
        
def add_term(A, B, index0, index1, ans, monomial_order):
    
    if monomial_order(A[index0], B[index1]) >0:
        ans.append(A[index0])
        index0 += 1
    elif monomial_order(A[index0], B[index1]) == 0:
        ans.append(A[index0] + B[index1])
        index0 += 1
        index1 += 1
    else:
        ans.append(B[index1])
        index1 += 1
    return index0, index1
    