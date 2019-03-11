# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 16:38:02 2019

@author: xcledjwfr
"""


from sklearn.linear_model import LinearRegression
x= [[6, 2], [8, 1], [10, 0], [14, 2], [18, 0]]
y = [[7], [9], [13], [17.5], [18]]
model=LinearRegression()
model.fit(x,y)

print(model.score(x,y))