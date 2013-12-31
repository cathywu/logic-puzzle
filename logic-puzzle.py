from Grid import *
from Thing import *
import time

g = Grid(10,15)
a = Alice()
m = Mirror()
c = Feather()
a.spawn(g, (5,13))
m.spawn(g, (1,14))
c.spawn(g, (2,13))

print g.positionOf(a)

g.draw_grid()
for i in range(100):
  g.tick()
  g.draw_grid()
  time.sleep(.2)


print g.positionOf(a)
print g.positionOf(m)
