from Grid import *

FORWARD = 0
RIGHT = 1
LEFT = -1
BACK = 2

class Thing:
    def __init__(self, name, symbol, delay):
        self.name = name
        self.symbol = symbol
        self.delay = delay 

    def spawn(self, grid, startPos, startDir=NORTH):
        self.grid = grid
        grid.addThing(self, startPos)
        self.direction = startDir
        self.clock = 0

    def tick(self):
        if self.clock == self.delay:
            self.clock = 0
            self.move()
        else:
            self.clock += 1

    def move(self):
        pass

    def collide(self, thing):
        pass

    def turn(self, direction):
        self.direction = (self.direction + direction) % 4

    def relativeMove(self, relative):
        absolute = [(self.direction + r) % 4 for r in relative]
        self.grid.moveThing(self, absolute)

    def turnRight(self):
        self.curDir = (self.curDir + 1) % 4

    def turnLeft(self):
        self.curDir = (self.curDir - 1) % 4

class Mirror(Thing):
    def __init__(self):
        Thing.__init__(self, "mirror", 'm', 0)

class Chess(Thing):
    def __init__(self):
        Thing.__init__(self, "chess", unichr(9823), 0)

class Alice(Thing):
    def __init__(self):
        Thing.__init__(self, "alice", "A", 0)

    def move(self):
        self.delay = 0
        self.relativeMove([FORWARD, RIGHT, LEFT, BACK])
        self.symbol = ["^", ">", "v", "<"][self.direction]
    
    def collide(self, thing):
        if thing.name == "mirror": # Run backwards 
            self.turn(BACK)
            self.move()
            self.move()

        if thing.name == "chess": # Nap for one tick
            self.delay = 1
