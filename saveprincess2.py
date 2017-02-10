# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 15:29:27 2017

@author: exmachina
"""
def nextMove(n,r,c,grid):
    mariox = (r,c)
    for idx, raa in enumerate(grid):
        if 'p' in raa:
            princess = (idx, raa.index('p'))
#        if 'm' in raa:
#            mario = (idx, raa.index('m'))
#    print(princess, 'mariox', mariox)
    vert = princess[0] - mariox[0]
    horz = princess[1] - mariox[1]
    if vert>0:
        return "DOWN"
    elif vert < 0:
        return "UP"
    elif vert == 0:
        if horz > 0:
            return "RIGHT"
        elif horz < 0:
            return "LEFT"
###############################
n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))
