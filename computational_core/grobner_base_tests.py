# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 13:02:29 2014

@author: mmoshe
"""

from ideal_basis import IdealBasis
from grobner_base import get_Grobner_base_extended, get_Grobner_base_minimized, \
        get_Grobner_base_reduced
from Monomial import Monomial as Mon
from Polynomial import Polynomial
from monomial_operations import monomial_grlex
import unittest

class TestsGrobnerBase(unittest.TestCase):

    def test_get_Grobner_base__extended_ex0(self):
        
        base = get_base_for_Ex0()
        g_base = get_Grobner_base_extended(base)
        add_exp_base = get_expected_base_Ex0()
        expected_base = IdealBasis([base.basis[0], base.basis[1]] + add_exp_base)
        self.__check_bases_are_equal(g_base, expected_base)
        
    def test_get_Grobner_base_minimized_ex0(self):
        
        base = get_base_for_Ex0()
        g_base = get_Grobner_base_minimized(base)
        expected_base = IdealBasis(get_expected_base_Ex0())
        self.__check_bases_are_equal(g_base, expected_base)
        
    def test_get_Grobner_base_reduced_ex0(self):
        
        base = get_base_for_Ex0()
        g_base = get_Grobner_base_reduced(base)
        expected_base = get_expected_reduced_base()
        self.__check_bases_are_equal(g_base, expected_base)
        
    def test_reduce_minimal_grobner_base(self):
        
        Mon.monom_comparator = monomial_grlex
        orig_p0 = Polynomial([Mon(1, (2,0)), Mon(-7, (1,1))])
        orig_p1 = Polynomial([Mon(2, (1,1))])
        orig_p2 = Polynomial([Mon(2, (0,2)), Mon(-1, (1,0))])
        orig_base = IdealBasis([orig_p0, orig_p1, orig_p2])
        g_base = get_Grobner_base_reduced(orig_base)
        expected_base = get_expected_reduced_base()
        self.__check_bases_are_equal(g_base, expected_base)
        
    def __check_bases_are_equal(self, base0, base1):
        
        self.assertEqual(len(base0.basis), len(base1.basis))
        for index in range(len(base0.basis)):
            self.assertEqual(base0.basis[index], base1.basis[index])
        
def get_base_for_Ex0():
    
    Mon.num_of_variables = 2
    Mon.monom_comparator = monomial_grlex
    poly0 = Polynomial([Mon(1, (3,0)), Mon(-2, (1,1))])
    poly1 = Polynomial([Mon(1, (2,1)), Mon(-2, (0,2)), Mon(1, (1,0))])
    base = IdealBasis([poly0, poly1])
    return base
    
def get_expected_base_Ex0():
    
    exp_p2 = Polynomial([Mon(1, (2,0))])
    exp_p3 = Polynomial([Mon(2, (1,1))])
    exp_p4 = Polynomial([Mon(2, (0,2)), Mon(-1, (1,0))])
    return [exp_p2, exp_p3, exp_p4]
    
def get_expected_reduced_base():
    
    exp_p0 = Polynomial([Mon(1, (2,0))])
    exp_p1 = Polynomial([Mon(1, (1,1))])
    exp_p2 = Polynomial([Mon(1, (0,2)), Mon(-0.5, (1,0))])
    expected_base = IdealBasis([exp_p0, exp_p1, exp_p2])
    return expected_base
        
def run_single_test(testname):
    suite = unittest.TestSuite()
    suite.addTest(TestsGrobnerBase(testname))
    unittest.TextTestRunner(verbosity=2).run(suite)

def TheTestSuite():
    return unittest.TestLoader().loadTestsFromTestCase(TestsGrobnerBase)

def run_all_tests():
    unittest.TextTestRunner(verbosity=2).run(TheTestSuite())

if __name__ == '__main__':
    run_all_tests()
#    run_single_test('test_reduce_minimal_grobner_base')
    
    