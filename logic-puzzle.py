#!/bin/python

from Grid import *
from Thing import *
import time, sys

g = Grid(6, 9)
# g.delWall([0,4], NORTH)
# g.addWallQuad([2,0], EAST)
# g.addWallQuad([4,0], EAST)
# g.addWallQuad([2,1], SOUTH)
# g.addWallQuad([1,2], SOUTH)
# g.addWallQuad([3,2], SOUTH)
g.addWall180([2,3], EAST) # wormhole
g.addWall180([4,3], EAST) # wormhole
g.addWall180([4,2], EAST) # wormhole
g.addWall180([3,1], SOUTH) # wormhole
# g.addWall180([1,1], EAST) # wormhole
# g.addWall180([4,2], NORTH) # wormhole
g.addWall180([0,3], SOUTH) # wormhole
g.addWall180([1,2], SOUTH) # wormhole
g.addWall180([1,2], WEST) # wormhole

a = Alice()
m = Mirror()
c = Chess()
f = Feather()

a.spawn(g, (5,0))
# a.turn(BACK)
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
