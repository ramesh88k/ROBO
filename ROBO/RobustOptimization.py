import numpy as np
import cvxpy as cvx
import pandas as pd
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
import mosek

from ROBO.functions import *
from ROBO.loadvariables import loadinifile

class RobustOpti:
    def __init__(self):
        self.vv = loadinifile()
        self.constraints = []

    def initiate_variables(self):
        self.theta = cvx.Variable((self.vv.N_bar+1,self.vv.nAssets))
        self.w = cvx.Variable(self.vv.N_bar)

    def add_initial_value_constraint(self,p0):
        self.constraints += [p0*self.theta[0,:] == self.vv.asset_initial_value]
    def add_contribution_constraint(self):
        self.constraints += [self.w>=0]

    def add_all_constraints(self):
        self.add_contribution_constraint()
        self.add_initial_value_constraint()

    def run_optimization(self,solver = 'MOSEK'):
        objective = cvx.Minimize(sum(self.w))
        p = cvx.Problem(objective,self.constraints)
        if solver == 'GUROBI':
            self.result = p.solve(solver = cvx.GUROBI)
        else:
            self.result = p.solve(solver = cvx.MOSEK)


opt = RobustOpti()
opt.initiate_variables()
opt.add_contribution_constraint()
# print(opt.theta[0,:].shape)


opt.add_initial_value_constraint(np.ones(43))
opt.run_optimization()

print(opt.result)
print(opt.theta.value)
print('n')
# print(type(opt.constraints))

print('test2')
print('asdas')