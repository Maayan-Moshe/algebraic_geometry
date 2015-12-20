# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 13:02:29 2014

@author: mmoshe
"""

from Monomial import Monomial
from Polynomial import Polynomial
import numpy as np
import unittest

class TestsPolynomial(unittest.TestCase):
    
    x = Monomial(3, np.array((0,0,0)))
    y = Monomial(3, np.array((3,2,1)))
    z = x*y
        
    def test_two_different_monoms(self):
        
        poly = Polynomial([self.x, self.y])
        self.assertTrue(poly.terms[0] > poly.terms[1])
        
    def test_two_same_monoms(self):
        
        poly = Polynomial([self.z, self.y, self.z])
        self.assertEqual(len(poly.terms), 1)
        
    def test_add_two_polys(self):
        
        poly0, poly1 = self.__get_polys_for_op()
        add_poly = poly0 + poly1
        self.assertEqual(len(add_poly.terms), 2)
        self.assertEqual(add_poly.terms[0].coeff, 27)
        self.assertEqual(add_poly.terms[1].coeff, 3)
        
    def test_sub_two_polys(self):
        
        poly0, poly1 = self.__get_polys_for_op()
        sub_poly = poly0 - poly1
        self.assertEqual(len(sub_poly.terms), 2)
        self.assertEqual(sub_poly.terms[0].coeff, -21)
        self.assertEqual(sub_poly.terms[1].coeff, 3)
        
    def test_mul_two_polys(self):
        
        poly0, poly1 = self.__get_polys_for_op()
        sub_poly = poly0 * poly1
        self.assertEqual(len(sub_poly.terms), 2)
        self.assertEqual(sub_poly.terms[0].coeff, 72)
        self.assertEqual(sub_poly.terms[1].coeff, 72)
        
    def __get_polys_for_op(self):
        
        poly0 = Polynomial([self.x, self.y])
        poly1 = Polynomial([self.z, self.y, self.y + self.z, Monomial()])
        return poly0, poly1

def run_single_test(testname):
    suite = unittest.TestSuite()
    suite.addTest(TestsPolynomial(testname))
    unittest.TextTestRunner(verbosity=2).run(suite)

def TheTestSuite():
    return unittest.TestLoader().loadTestsFromTestCase(TestsPolynomial)

def run_all_tests():
    unittest.TextTestRunner(verbosity=2).run(TheTestSuite())

if __name__ == '__main__':
    run_all_tests()
#    run_single_test('test_mul_two_polys')
    
    