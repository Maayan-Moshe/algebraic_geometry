# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 10:10:56 2015

@author: mmoshe
"""

from Monomial import Monomial

class Polynomial:
    
    def __init__(self, terms = list()):
        
        self.terms = sorted(terms, reverse=True)
        remove_zeros_from_mon_list(self.terms)
        remove_duplicates_from_mon_list(self.terms)
        
    def is_dividable_by_leading_term(self, other):
        
        return self.terms[0].is_dividable(other.terms[0])
        
    def divide_by_leading_term(self, other):
        
        assert self.is_dividable_by_leading_term(other)
        mon_ans = self.terms[0]/other.terms[0]
        return Polynomial([mon_ans])
        
    def is_empty(self):
        
        return len(self.terms) == 0
        
    def get_polynomial_lead_term(self):
        
        return Polynomial([self.terms[0]])
        
    def __mul__(self, other):
        
        ans_terms = list()
        for s_trm in self.terms:
            for o_trm in other.terms:
                ans_terms.append(s_trm * o_trm)
        return Polynomial(ans_terms)
    
    def __add__(self, other):
        
        ans = list()
        index0 = 0
        index1 = 0
        while index0 < len(self.terms) and index1 < len(other.terms):
            index0, index1 = add_term(self.terms, other.terms, 
                                      index0, index1, ans)
        ans += self.terms[index0:]
        ans += other.terms[index1:]
        return Polynomial(ans)
        
    def __sub__(self, other):
        
        return self + (-other)
        
    def __neg__(self):
        
        ans_terms = list()
        for trm in self.terms:
            ans_terms.append(-trm)
        return Polynomial(ans_terms)
        
    def __str__(self):
        
        ans = ''
        for trm in self.terms:
            ans += str(trm) + '+'
        return ans[:-1]
        
    def __repr__(self):
        
        return self.__str__()
        
    def __eq__(A, B):
        
        if len(A.terms) != len(B.terms):
            return False
        for index in xrange(len(A.terms)):
            if not Monomial.equal_val(A.terms[index], B.terms[index]):
                return False
        return True
        
def add_term(A, B, index0, index1, ans):
    
    if Monomial.monom_comparator(A[index0], B[index1]) >0:
        ans.append(A[index0])
        index0 += 1
    elif Monomial.monom_comparator(A[index0], B[index1]) == 0:
        ans.append(A[index0] + B[index1])
        index0 += 1
        index1 += 1
    else:
        ans.append(B[index1])
        index1 += 1
    return index0, index1
    
def remove_zeros_from_mon_list(monomial_list):
    
    z_c = 0
    for index in xrange(len(monomial_list)):
        ind = index - z_c
        if monomial_list[ind].coeff == 0:
            monomial_list.pop(ind)
            z_c += 1
        
def remove_duplicates_from_mon_list(monomial_list):
    
    z_c = 0
    for index in xrange(len(monomial_list) - 1):
        ind = index - z_c
        if Monomial.monom_comparator(monomial_list[ind], monomial_list[ind + 1]) == 0:
            monomial_list[ind + 1] += monomial_list[ind]
            monomial_list.pop(ind)
            z_c += 1