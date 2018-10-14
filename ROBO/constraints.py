import cvxpy as cvx
import numpy as np
import pandas as pd
import configparser

from ROBO.loadvariables import loadinifile

vv = loadinifile()

print(vv.weight_Bonds_min)

# # imports variables in Variable.ini as dict to config
# config = configparser.ConfigParser()
# config.read('../config/variable.ini')
#
#
# print(config['weights']['weight_Bonds_min'])
# print(config['default']['N'])
