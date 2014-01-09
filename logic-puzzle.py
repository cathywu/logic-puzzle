#!/bin/python

from Grid import *
from Thing import *
import time, sys

g = Grid(6, 9)
g.addWall180([2,3], EAST)
g.addWall180([4,3], EAST)
g.addWall180([4,2], EAST)
g.addWall180([3,1], SOUTH)
g.addWall180([0,3], SOUTH)
g.addWall180([1,2], SOUTH)
g.addWall180([1,2], WEST) 

a = Alice()
m = Mirror()
c = Chess()
f = Feather()

a.spawn(g, (5,0))
m.spawn(g, (1,4))
# m.spawn(g, (2,5))
#c.spawn(g, (0,5))
f.spawn(g, (0,8))

print g.positionOf(a)

try:
  tick = float(sys.argv[1])
except:
  tick = 0.5

g.draw_grid()
for i in range(100):
  g.tick()
