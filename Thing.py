from Grid import *

FORWARD = 0
RIGHT = 1
LEFT = -1
BACK = 2

class Thing:
    def __init__(self, name, symbol, delay):
        self.name = name
        self.symbol = symbol
        self.delay = delay + 1

    def spawn(self, grid, startPos, startDir=NORTH):
        self.grid = grid
        grid.addThing(self, startPos)
        self.direction = startDir
        self.clock = 0

    def tick(self):
        if self.clock % self.delay == 0:
            self.move()

        self.clock += 1

    def move(self):
        pass

    def relativeMove(self, relative):
        absolute = [(self.direction + r) % 4 for r in relative]
        d = self.grid.moveThing(self, absolute)
        if d:
            self.direction = d

    def turnRight(self):
        self.curDir = (self.curDir + 1) % 4

    def turnLeft(self):
        self.curDir = (self.curDir - 1) % 4

class Mirror(Thing):
    def __init__(self):
        Thing.__init__(self, "mirror", "/", 0)

class Alice(Thing):
    def __init__(self):
        Thing.__init__(self, "alice", "A", 0)

    def move(self):
        self.relativeMove([FORWARD, RIGHT, LEFT, BACK])

