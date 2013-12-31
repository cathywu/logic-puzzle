from Grid import Grid
from Thing import Alice, Mirror

g = Grid(10,15)
g.addThing(Alice(), (3,4))
g.addThing(Mirror(), (8,8))
g.draw_grid()
