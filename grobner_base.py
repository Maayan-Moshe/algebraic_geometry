# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 17:01:47 2015

@author: mmoshe
"""

from ideal_basis import IdealBasis
from polynomial_operations import get_S_polynomial
from Monomial import Monomial
from Polynomial import Polynomial
import numpy as np

def get_Grobner_base_reduced(ibasis):
    
    min_g_base = get_Grobner_base_minimized(ibasis)
    reduced_base = _reduce_minimal_grobner_base(min_g_base)
    return reduced_base
    
def get_Grobner_base_minimized(ibasis):
    
    g_basis_ex = get_Grobner_base_extended(ibasis)
    min_g_base = _minimize_Grobner_base(g_basis_ex)
    return min_g_base

def get_Grobner_base_extended(ibasis):
    
    pre_g_basis = ibasis
    post_g_basis = _enrich_Groebner_basis(ibasis, start_index = 0)
    while len(post_g_basis.basis) > len(pre_g_basis.basis):
        start_index = len(pre_g_basis.basis)
        pre_g_basis = post_g_basis
        post_g_basis = _enrich_Groebner_basis(pre_g_basis, start_index)
    return post_g_basis
    
def _reduce_minimal_grobner_base(min_g_base):
    
    exp_list, exp_dict = _get_exp_list_dict(min_g_base)
    base_mat = _get_base_matrix(min_g_base, exp_list, exp_dict)
    ech_mat = _get_ech_mat_from_upper_mat(base_mat)
    reduced_base = _get_reduced_base_from_echelon_mat(ech_mat, exp_list)
    return reduced_base
    
def _get_reduced_base_from_echelon_mat(ech_mat, exp_list):
    
    red_base = list()
    for row in range(ech_mat.shape[0]):
        row_mons = list()
        for col in range(ech_mat.shape[1]):
            row_mons.append(Monomial(ech_mat[row, col], exp_list[col]))
        red_base.append(Polynomial(row_mons))
    reduced_base = IdealBasis(red_base)
    return reduced_base
    
def _get_base_matrix(min_g_base, exp_list, exp_dict):
    
    base_mat = np.zeros((min_g_base.length(), len(exp_list)))
    for row in range(min_g_base.length()):
        for mon in min_g_base.basis[row].terms:
            col = exp_dict[tuple(mon.exponent)]
            base_mat[row, col] = mon.coeff
    return base_mat
    
def _get_ech_mat_from_upper_mat(upp_mat):
    
    ech_mat = np.copy(upp_mat)
    for base_row in range(ech_mat.shape[0] - 1, -1, -1):
        _correct_col_by_row(ech_mat, base_row)
    return ech_mat
    
def _correct_col_by_row(ech_mat, base_row):
    
    left_col = np.nonzero(ech_mat[base_row, :])[0][0]
    ech_mat[base_row, :] /= ech_mat[base_row, left_col]
    non_zero_rows = np.nonzero(ech_mat[:base_row, left_col])[0]
    for upp_row in non_zero_rows:
        ech_mat[upp_row, :] -= ech_mat[upp_row, left_col]*ech_mat[base_row, left_col]
    
def _get_exp_list_dict(min_g_base):
    
    exponent_set = set()
    for bpoly in min_g_base.basis:
        _add_exp_from_poly_to_set(exponent_set, bpoly)
    exp_list = _get_sorted_exp_list_from_set(exponent_set)
    exp_dict = dict()
    for index in range(len(exp_list)):
        exp_dict[exp_list[index]] = index
    return exp_list, exp_dict
    
def _add_exp_from_poly_to_set(exponent_set, poly):
    
    for mon in poly.terms:
        exponent_set.add(tuple(mon.exponent))
        
def _get_sorted_exp_list_from_set(exp_set):
    
    mon_list = [Monomial(1, x) for x in exp_set]
    mon_list.sort(reverse = True)
    exp_list = [tuple(x.exponent) for x in mon_list]
    return exp_list
    
def _minimize_Grobner_base(grobner_base):
    
    min_g_base = IdealBasis(list(grobner_base.basis))
    min_g_base.sort_by_lead_term()
    counter = 0
    for index0 in range(len(min_g_base.basis)):
        counter = _minimize_Grobner_base_by_index(min_g_base, index0, counter)
    return min_g_base

def _minimize_Grobner_base_by_index(grobner_base, index0, counter):
    
    for index1 in range(index0 + 1, len(grobner_base.basis)):
        poly0 = grobner_base.basis[index0-counter]
        poly1 = grobner_base.basis[index1-counter]
        if poly0.is_dividable_by_leading_term(poly1):
            grobner_base.basis.pop(index0-counter)
            counter += 1
            return counter
    return counter

def _enrich_Groebner_basis(ibasis, start_index):
    
    g_basis = IdealBasis(list(ibasis.basis))
    for index0 in range(start_index, len(g_basis.basis)):
        for index1 in range(index0):
            _enrich_Groebner_basis_S_residual(g_basis, index0, index1)
    return g_basis
    
def _enrich_Groebner_basis_S_residual(g_basis, index0, index1):
    
    S_poly = get_S_polynomial(g_basis.basis[index0], g_basis.basis[index1])
    _, res = g_basis.divide_polynomial_by_basis(S_poly)
    if not res.is_empty():
       g_basis.basis.append(res)