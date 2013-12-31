from Grid import *
from Thing import *
import time

g = Grid(10,15)
a = Alice()
m = Mirror()
a.spawn(g, (3,13))
g.addThing(m, (2,13))

print g.positionOf(a)

g.draw_grid()
for i in range(100):
  a.tick()
  g.draw_grid()
  time.sleep(0.1)


print g.positionOf(a)
print g.positionOf(m)
