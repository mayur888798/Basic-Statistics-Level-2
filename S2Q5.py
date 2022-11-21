# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 19:24:10 2022

@author: mayur
"""

import numpy as np
import pandas as pd
import scipy as sp
from scipy import stats
from scipy.stats import norm

#Now, Mean Profits from the two different divisions of a company, wich are independent of each other
# Mean Profits = Mean1 + Mean2

Mean=5+7
Mean
print('Mean Profit is in Rs.', Mean*45,'Million')


#Now, the Variance of the profits from the two different divisions of the same company
#  Variance(SD^2) =  SD1^1 + SD2^2

SD=np.sqrt((9)+(16))
SD
print('Standard Deviation is Rs.', SD*45, 'Million')


#Now,
#A. Specify a Rupee Range(Centered on the mean) such that it contains 95% probability for the annual profit of the company.

RRange=stats.norm.interval(0.95,540,225)
RRange
print('Range in Rupees is', RRange, 'in Millions')


#B. Specify the 5th perentile of profit (in rupees) for the company

# To cimpute the 5th perentile, we use the formula  X=Mu+Z(sigma)
#Since, from Z table, the 5th percemtile is = -1.645

X=540+(-1.645)*(225)
X

X=np.round(X,)
X
print('the 5th perentile of the profit is',X,'Million Rupees')


#C. Which of the two divisions has a larger Probability of making a loss in a given year

#Probaility of Division 1 making a loss (PLD1)

PLD1=stats.norm.cdf(0,5,3)
PLD1

#Now,
#Probability of Division 2 making loss (PLD2)

PLD2 = stats.norm.cdf(0,7,4)
PLD2