import cvxpy as cvx
import numpy as np
import pandas as pd
import sympy as sp
from sympy import symbols
from sympy.tensor.array import derive_by_array

from ROBO.loadvariables import loadinifile



class allfunctions:
    def __init__(self):
        self.vv = loadinifile()

    def delta_p_j_bonds(self,j,tau=3.0):
        m=self.vv.m
        z1=self.vv.z1
        z2 = self.vv.z2
        z3 = self.vv.z3
        rho = self.vv.rho

        z1_sp, z2_sp, z3_sp, j_sp = symbols('z1_sp z2_sp z3_sp j_sp', real = True)
        g1 = self.bond_grad(j_sp,z1_sp,z2_sp ,z3_sp)
        g2 = self.bond_hessian(j_sp,z1_sp,z2_sp ,z3_sp)
        g1_value = np.array(g1.subs([(j_sp,j),(z1_sp,z1),(z2_sp,z2),(z3_sp,z3)]))
        g2_value = np.array(g2.subs([(j_sp,j),(z1_sp,z1),(z2_sp,z2),(z3_sp,z3)])).reshape((3, 3))
        first = np.sum((m-np.array([z1,z2,z3]))*g1_value)
        second = np.sum(0.5*rho*g2_value)
        return first+second

    def delta_p_bonds(self):
        result = np.zeros(self.vv.nBonds)
        for j in range(self.vv.nBonds):
            result[j] = self.delta_p_j_bonds(j+1)
        self.bonds_delta = result
        return result

    @staticmethod
    def spot_rate(j, z1, z2, z3, tau=3.0):

        s = z1 + z2 * ((1 - sp.exp(-j / tau)) / (j / tau)) + z3 * ((1 - sp.exp(-j / tau)) / (j / tau) - sp.exp(-j / tau))
        return s
    @staticmethod
    def bond_grad(j, z1, z2, z3,tau=3.0):
        bond_price = 1 / (1 + allfunctions.spot_rate(j, z1, z2, z3,tau)) ** j
        grad = derive_by_array(bond_price, (z1, z2, z3))
        return grad
    @staticmethod
    def bond_hessian(j, z1, z2, z3,tau=3.0):
        # f1 = spot_rate(j,z1, z2, z3)
        bond_price = 1 / (1 + allfunctions.spot_rate(j, z1, z2, z3,tau)) ** j
        hessian = derive_by_array(derive_by_array(bond_price, (z1, z2, z3)), (z1, z2, z3))
        return hessian


#
# myclass1 = allfunctions()
# myclass1.delta_p_bonds()
# print(myclass1.bonds_delta)
# # print(myclass1.delta_p_bonds())
#
# # print(myclass1.delta_p_j_bonds(5))

