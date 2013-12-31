NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

class Thing:
    def __init__(self, name, symbol, delay):
        self.name = name
        self.symbol = symbol
        self.delay = delay + 1

    def spawn(self, grid, startPos, startDir):
        self.grid = grid
        grid.addThing(startPos)
        self.curDir = startDir
        self.clock = 0

    def tick(self):
        if self.clock % self.delay == 0:
            self.move()

        self.clock += 1

    def move(self):
        pass

    def step(self):
        curPos = self.grid.getPos(self)
        if self.curDir == NORTH:
            curPos[0] += 1
        elif self.curDir == EAST:
            curPos[1] += 1
        elif self.curDir == SOUTH:
            curPos[0] -= 1
        elif self.curDir == WEST:
            curPos[1] -= 1
        else: # STOP or error
            pass
        # TODO: check to make sure move is valid, else handle appropriately
        # TODO: Update Grid with new location of Thing

    def turnRight(self):
        self.curDir = (self.curDir + 1) % 4

    def turnLeft(self):
        self.curDir = (self.curDir - 1) % 4

class Mirror(Thing):
    def __init__(self):
        Thing.__init__(self, "mirror", "/", 0)

    def spawn(self, grid, startPos):
        Thing.spawn(self, grid, startPos, STOP)

class Alice(Thing):
    def __init__(self):
        Thing.__init__(self, "alice", "A", 0)

    def move(self):
        pass
