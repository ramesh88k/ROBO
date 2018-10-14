import numpy as np
import cvxpy as cvx
import pandas as pd
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
import mosek

from ROBO.functions import *
from ROBO.loadvariables import loadinifile

vv = loadinifile()

class cvxopt:
    def __init__(self):
        self.vv = loadinifile()

    def initiate_variables(self):
        self.theta = cvx.Variable((self.vv.N_bar+1,self.vv.nAssets))
        self.w = cvx.Variable(self.vv.N_bar)

    def


opt = cvxopt()
opt.initiate_variable()

