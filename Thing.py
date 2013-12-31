STOP = 0
NORTH = 1
EAST = 2
SOUTH = 3
WEST = 4

class Thing:
    def __init__(self, name, delay):
        self.name = name
        self.delay = delay + 1

    def spawn(self, grid, startpos, startdir):
        self.grid = grid
        grid.addThing(startpos)
        self.curdir = startdir
        self.clock = 0

    def tick(self):
        if self.clock % self.delay == 0:
            self.move()

        self.clock += 1

    def move(self):
        pass

    def step(self):
        curpos = self.grid.getPos(self)
        if self.curdir == NORTH:
            curpos[0] += 1
        elif self.curdir == EAST:
            curpos[1] += 1
        elif self.curdir == SOUTH:
            curpos[0] -= 1
        elif self.curdir == WEST:
            curpos[1] -= 1
        else: # STOP or error

class Mirror(Thing):
    def __init__(self):
        Thing.__init__(self, "mirror", 0)

class Alice(Thing):
    def __init__(self):
        Thing.__init__(self, "alice", 0)

    def move(self):
        
