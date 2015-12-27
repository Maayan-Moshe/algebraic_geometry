# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 17:01:47 2015

@author: mmoshe
"""

from ideal_basis import IdealBasis
from polynomial_operations import get_S_polynomial

def get_Grobner_base(ibasis):
    
    pre_g_basis = ibasis
    post_g_basis = _enrich_Groebner_basis(ibasis)
    while len(post_g_basis.basis) > len(pre_g_basis.basis):
        pre_g_basis = post_g_basis
        post_g_basis = _enrich_Groebner_basis(pre_g_basis)
    return post_g_basis

def _enrich_Groebner_basis(ibasis):
    
    g_basis = IdealBasis(list(ibasis.basis))
    orig_len = len(g_basis.basis)
    for index0 in range(orig_len):
        for index1 in range(index0):
            _enrich_Groebner_basis_S_residual(g_basis, index0, index1)
    return g_basis
    
def _enrich_Groebner_basis_S_residual(g_basis, index0, index1):
    
    S_poly = get_S_polynomial(g_basis.basis[index0], g_basis.basis[index1])
    _, res = g_basis.divide_polynomial_by_basis(S_poly)
    if not res.is_empty():
       g_basis.basis.append(res)