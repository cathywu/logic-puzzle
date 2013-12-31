from Grid import *
from Thing import Alice, Mirror

g = Grid(10,15)
a = Alice()
m = Mirror()
g.addThing(a, (3,13))
g.addThing(m, (2,13))

print g.positionOf(a)

g.draw_grid()
g.moveThing(a, [NORTH, EAST, SOUTH, WEST])
g.draw_grid()
g.moveThing(a, [NORTH, EAST, SOUTH, WEST])
g.draw_grid()
g.moveThing(a, [NORTH, EAST, SOUTH, WEST])
g.draw_grid()
g.moveThing(a, [NORTH, EAST, SOUTH, WEST])
g.draw_grid()
g.moveThing(a, [NORTH, EAST, SOUTH, WEST])
g.draw_grid()

print g.positionOf(a)
print g.positionOf(m)
