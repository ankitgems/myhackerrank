# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def displayPathtoPrincess(n,grid):
    m = int(input())
    grid = [] 
    for i in range(0, m): 
        grid.append(input().strip())
    
    for idx, raa in enumerate(grid):
        if 'p' in raa:
            princess = (idx, raa.index('p'))
        if 'm' in raa:
            mario = (idx, raa.index('m'))
    print(princess, mario)
    vert = princess[0] - mario[0]
    horz = princess[1] - mario[1]
    verx = ''
    horzx = ''
    if vert >0:
        verx = 'DOWN\n'*vert
    else:
        verx = 'UP\n'*abs(vert)
    if horz >0:
        horzx = 'RIGHT\n'*horz
    else:
        horzx = 'LEFT\n'*abs(horz)
    print(''.join([horzx,verx]))