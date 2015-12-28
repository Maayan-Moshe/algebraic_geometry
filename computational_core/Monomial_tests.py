# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 13:02:29 2014

@author: mmoshe
"""

from Monomial import Monomial
import numpy as np
import unittest

class TestsMonomial(unittest.TestCase):
        
    def test_monomial(self):
        
        x = Monomial(3, np.array((0,0,0)))
        y = Monomial(3, np.array((3,2,1)))
        z = x*y
        np.testing.assert_array_equal(z.exponent, np.array((3,2,1)))
        self.assertEqual(z.coeff, 9)
        self.assertTrue(z > x)
        self.assertFalse(z > y)
        self.assertFalse(x > z)
        self.assertFalse(y < z)

def run_single_test(testname):
    suite = unittest.TestSuite()
    suite.addTest(TestsMonomial(testname))
    unittest.TextTestRunner(verbosity=2).run(suite)

def TheTestSuite():
    return unittest.TestLoader().loadTestsFromTestCase(TestsMonomial)

def run_all_tests():
    unittest.TextTestRunner(verbosity=2).run(TheTestSuite())

if __name__ == '__main__':
    run_all_tests()
#    run_single_test('test_get_four_points_for_interpolation')
    
    