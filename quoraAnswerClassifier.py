# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 14:42:34 2017

@author: exmachina
"""

from sklearn.ensemble import RandomForestClassifier as rf
from sklearn.feature_extraction import DictVectorizer as dv

#for hackerrank comment line 12 , 13 and 14 and replace 'y.pop(0)' with 'input()'
y = []
with open('quoraAnswerClassifier.txt') as f:
    y =  f.readlines()
n,m = [int(i) for i in y.pop(0).strip().split()]
train_label = []
_train = []

for i in range(n):
    a = y.pop(0).strip().split()
    a.pop(0)
    train_label.append(a.pop(0))
    b = [x.split(':') for x in a]
    _train.append({int(e[0]):float(e[1]) for e in b})

train = dv().fit_transform(_train).toarray()

model =  rf()
model.fit(train, train_label)

test_name = []
_test = []

for i in range(int(y.pop(0).strip())):
    a = y.pop(0).strip().split()
    test_name.append(a.pop(0))
    b = [x.split(':') for x in a]
    _test.append({int(e[0]):float(e[1]) for e in b})

test = dv().fit_transform(_test).toarray()
test_lable = model.predict(test)

for x,z in zip(test_name, test_lable):
    print(x,z)