# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 13:31:20 2015

@author: mmoshe
"""

from Polynomial import Polynomial

class IdealBasis:
    
    def __init__(self, basis):
        
        self.basis = basis

    def divide_polynomial_by_basis(self, poly_to_divide):
        
        division_ans = [Polynomial()]*len(self.basis)
        residual = Polynomial()
        while not poly_to_divide.is_empty():
            poly_to_divide, division_ans, residual = \
                self.__divide_lead_term_by_basis(poly_to_divide, division_ans, residual)
        return division_ans, residual

    def __divide_lead_term_by_basis(self, poly_to_divide, division_ans, residual):
    
        for index in xrange(len(self.basis)):
            poly_to_divide, should_return = divide_one_poly_basis(poly_to_divide, \
                                self.basis[index], division_ans, index)
            if should_return:
                return poly_to_divide, division_ans, residual
        poly_to_divide, residual = add_to_residual(poly_to_divide, residual)
        return poly_to_divide, division_ans, residual

def divide_one_poly_basis(poly_to_divide, base_poly, division_ans, index):        
    
    if poly_to_divide.is_dividable_by_leading_term(base_poly):
        division, poly_to_divide = devide_two_polynomial_lead_term(poly_to_divide, base_poly)
        division_ans[index] += division
        return poly_to_divide, True
    return poly_to_divide, False
    
def add_to_residual(poly_to_divide, residual):
    
    lead_term = poly_to_divide.get_polynomial_lead_term()
    residual += lead_term
    poly_to_divide -= lead_term  
    return poly_to_divide, residual

def devide_two_polynomial_lead_term(numerator, denominator):
    
    division = numerator.divide_by_leading_term(denominator)
    substraction = numerator - division * denominator
    return division, substraction
    
    