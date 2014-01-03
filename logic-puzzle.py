#!/bin/python

from Grid import *
from Thing import *
import time

g = Grid(8, 8)
g.addWallQuad([2,0], EAST)
g.addWallQuad([4,0], EAST)
g.addWallQuad([2,1], SOUTH)
g.addWallQuad([1,2], SOUTH)
g.addWallQuad([3,2], SOUTH)
g.addWallQuad([3,2], EAST)

a = Alice()
m = Mirror()
c = Chess()
f = Feather()

a.spawn(g, (7,7))
a.turn(BACK)
# m.spawn(g, (1,7))
# c.spawn(g, (6,3))
f.spawn(g, (7,3))

print g.positionOf(a)

g.draw_grid()
for i in range(100):
  g.tick()
  g.draw_grid()
  time.sleep(.5)
