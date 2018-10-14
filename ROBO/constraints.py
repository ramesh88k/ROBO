import cvxpy as cvx
import numpy as np
import pandas as pd
import configparser

from ROBO.loadvariables import loadinifile

# vv = loadinifile()

# print(vv.weight_Bonds_min)


class allconstraints(object):
    def __init__(self):
        self.vv = loadinifile()
        self.constraints = []

    def add_initial_value_constraint(self,theta,p0):
        self.constraints += [p0*theta[0,:] == self.vv.asset_initial_value]

#comment
