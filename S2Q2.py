# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 01:08:40 2022

@author: mayur
"""

import scipy as sp
from scipy import stats
from scipy.stats import norm

#A. More employees at the processsing center are older than 44 than between 38 and 44.

# Probability for those employees who are older than 44 years.
#P(X)
1-stats.norm.cdf(44,loc=38,scale=6)

#For employyes between 38 to 44 years of age
stats.norm.cdf(44,38,6)-stats.norm.cdf(38,38,6)



#B. A training program for employees under the age of 30 years at the centre would be expected about 36 employees
# Probability of employees under the age of 30
#P(X<30)
p30=stats.norm.cdf(30,38,6)
p30
#Now, the Number of the employees atending the training program from 400 number of employees
#400*P(X<30)

400*p30