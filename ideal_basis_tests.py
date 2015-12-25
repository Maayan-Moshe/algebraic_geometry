# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 13:02:29 2014

@author: mmoshe
"""

from polynomial_operations import get_single_var_poly, get_const_poly
from ideal_basis import IdealBasis
import numpy as np
import unittest

class TestsIdealBasis(unittest.TestCase):
    
    x = get_single_var_poly(0)
    y = get_single_var_poly(1)
    z = get_single_var_poly(2)
        
    def test_divide_polynomial_by_basis_lin(self):

        base = IdealBasis([self.x, self.y, self.z])
        poly = get_const_poly(3)*self.x + get_const_poly(-2)*self.y + \
                    get_const_poly(0)*self.z + get_const_poly(1)
        division_ans, residual = base.divide_polynomial_by_basis(poly)
        expected_res = get_const_poly(1)
        self.assertEqual(residual, expected_res)
        self.assertEqual(get_const_poly(3), division_ans[0])
        self.assertEqual(get_const_poly(-2), division_ans[1])
        self.assertEqual(get_const_poly(0), division_ans[2])
        
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
    
    