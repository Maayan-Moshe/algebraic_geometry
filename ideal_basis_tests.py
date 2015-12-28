# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 13:02:29 2014

@author: mmoshe
"""

from polynomial_operations import get_single_var_poly, get_const_poly
from ideal_basis import IdealBasis
from Monomial import Monomial as Mon
import unittest

class TestsIdealBasis(unittest.TestCase):
    
    x = get_single_var_poly(0)
    y = get_single_var_poly(1)
    z = get_single_var_poly(2)
        
    def test_divide_polynomial_by_basis_lin(self):

        base = get_base_for_lin_case()
        poly = get_const_poly(3)*base.basis[0] + get_const_poly(-2)*base.basis[1] + \
                    get_const_poly(0)*base.basis[2] + get_const_poly(1)
        division_ans, residual = base.divide_polynomial_by_basis(poly)
        exp_res = get_const_poly(1)
        exp_ans = [get_const_poly(3), get_const_poly(-2), get_const_poly(0)]
        self.__check_ans_res(division_ans, residual, exp_ans, exp_res)
        
    def test_book_example_1(self):
        
        poly, base, x, y, one  = get_poly_base_for_ex1()
        division_ans, residual = base.divide_polynomial_by_basis(poly)
        exp_ans = [y, -one]
        exp_res = get_const_poly(2)
        self.__check_ans_res(division_ans, residual, exp_ans, exp_res)
        
    def test_book_example_2(self):
        
        poly, base, x, y, one  = get_poly_base_for_ex2()
        division_ans, residual = base.divide_polynomial_by_basis(poly)
        exp_ans = [x + y, one]
        exp_res = x + y + one
        self.__check_ans_res(division_ans, residual, exp_ans, exp_res)
        
    def test_sort_by_lead_term(self):
        
        x, y, z = get_xyz_polys()
        base = IdealBasis([z, y, x])
        base.sort_by_lead_term()
        self.assertEqual(base.basis[0], x)
        self.assertEqual(base.basis[1], y)
        self.assertEqual(base.basis[2], z)
    
    def __check_ans_res(self, ans, res, exp_ans, exp_res):
        
        for index in range(len(ans)):
            self.assertEqual(exp_ans[index], ans[index])
        self.assertEqual(res, exp_res)
        
def get_base_for_lin_case():
    
    x, y, z = get_xyz_polys()
    base = IdealBasis([x, y, z])
    return base
    
def get_xyz_polys():
    
    Mon.num_of_variables = 3
    x = get_single_var_poly(0)
    y = get_single_var_poly(1)
    z = get_single_var_poly(2)
    return x, y, z

def get_poly_base_for_ex1():
    
    Mon.num_of_variables = 2
    x = get_single_var_poly(0)
    y = get_single_var_poly(1)
    one = get_const_poly(1)
    base = IdealBasis([x*y + one, y + one])
    poly = x*y*y + one 
    return poly, base, x, y, one  
    
def get_poly_base_for_ex2():
    
    Mon.num_of_variables = 2
    x = get_single_var_poly(0)
    y = get_single_var_poly(1)
    y_2 = y*y
    one = get_const_poly(1)
    base = IdealBasis([x*y - one, y_2 - one])
    poly = x*x*y + x*y_2 + y_2 
    return poly, base, x, y, one  
        
def run_single_test(testname):
    suite = unittest.TestSuite()
    suite.addTest(TestsIdealBasis(testname))
    unittest.TextTestRunner(verbosity=2).run(suite)

def TheTestSuite():
    return unittest.TestLoader().loadTestsFromTestCase(TestsIdealBasis)

def run_all_tests():
    unittest.TextTestRunner(verbosity=2).run(TheTestSuite())

if __name__ == '__main__':
    run_all_tests()
#    run_single_test('test_get_four_points_for_interpolation')
    
    