# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 13:02:29 2014

@author: mmoshe
"""

from polynomial_operations import get_S_polynomial
from Monomial import Monomial as Mon
from Polynomial import Polynomial
import unittest

class TestsPolynomialOperations(unittest.TestCase):
        
    def test_get_S_polynomial_ex0(self):
        
        poly0, poly1 = get_polys_for_ex0()
        S_poly = get_S_polynomial(poly0, poly1)
        expected_S_poly = Polynomial([Mon(-1, (3,3)), Mon(1, (2,0)), Mon(-1.0/3, (0,3))])
        self.assertEqual(S_poly, expected_S_poly)
        
def get_polys_for_ex0():
    
    Mon.num_of_variables = 2
    poly0 = Polynomial([Mon(1, (3,2)), Mon(-1, (2,3)), Mon(1, (1,0))])
    poly1 = Polynomial([Mon(3, (4,1)), Mon(1, (0,2))])
    return poly0, poly1   
        
def run_single_test(testname):
    suite = unittest.TestSuite()
    suite.addTest(TestsPolynomialOperations(testname))
    unittest.TextTestRunner(verbosity=2).run(suite)

def TheTestSuite():
    return unittest.TestLoader().loadTestsFromTestCase(TestsPolynomialOperations)

def run_all_tests():
    unittest.TextTestRunner(verbosity=2).run(TheTestSuite())

if __name__ == '__main__':
    run_all_tests()
#    run_single_test('test_mul_two_polys')
    
    