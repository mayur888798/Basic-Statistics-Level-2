# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 20:13:28 2022

@author: mayur
"""

import numpy as np
import pandas as pd

x=pd.Series([24.23,25.53,25.41,24.14,29.62,28.25,25.81,24.39,40.26,32.95,91.36,25.99,39.42,26.71,35.00])
x

name=['Allied Signal','Bankers Trust','General Mills','ITT Industries','J. P. Morgan & Co.','Lehman Brothers','Marriott','MCI','Merrill Lynch','Microsoft','Morgan Staneley','Sun Microsystems','Travelers','US Airwyas','Warner-Lambert']

#Mean
x.mean()

#Variance

#Standard Variance
x.std()


#Plots
#Histogram
import matplotlib.pyplot as plt
plt.plot(df['Name of company'])

#Box Plot
import seaborn as sns
sns.boxplot(x)

#Piechart
plt.figure(figsize=(6,8))
plt.pie(x,labels=name,autopct='%1.0f%%')
plt.show()