# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 16:24:36 2017

@author: ankit
"""
import sys
#f = open('housepriceinput.txt','r')
fn = input().split()
#print(fn)
f = int(fn[0])
n = int(fn[1])
#print(type(n),n)
xtrain = []
nrow =[]
for i in range(0,n):
    row = input().split()
    for number in row:
        number = float(number)
        nrow.append(number)
    xtrain.append(nrow)
        
print(xtrain)
ytrain=[]
for idx,row in enumerate(xtrain):
    ytrain.append(row.pop())

print('YYYYYYYYYYY',ytrain)
nrow= []
xtest=[]
fn = input().strip().split()
for i in range(0,fn):
    row = input().split()
    for number in row:
        number = float(number)
        nrow.append(number)
    xtest.append(nrow)
print('xtest',xtest)