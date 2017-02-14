# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 18:27:34 2017

@author: exmachina
"""
import sys
#import numpy as np
#from sklearn import linear_model
#import matplotlib.pyplot as plt
#data =  np.loadtxt('trainingdata.txt', delimiter = ',')
#X = data[:, 0]
#Y = data[:, 1]
#X = X.reshape(-1, 1)
#Y = Y.reshape(-1, 1)
#model = linear_model.LinearRegression()
#model.fit(X,Y)
time = float(input().strip())
#out = model.predict(time)
#out = out[0][0]
if time<4:
    print(2*time)
else:
    print("{0:.2f}".format(8))
#plt.scatter(X,Y)
#plt.plot(X, model.predict(X),'ro')
#plt.show()
