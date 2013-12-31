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

class Feather(Thing):
    def __init__(self):
        Thing.__init__(self, "feather", 'F', 0)

class Rabbit(Thing):
    def __init__(self):
        Thing.__init__(self, "rabbit", "r", 1)

    def move(self):
        self.relativeMove([FORWARD, RIGHT, LEFT, BACK])

class Alice(Thing):
    def __init__(self):
        Thing.__init__(self, "alice", "A", 0)
        self.rabbit = None

    def move(self):
        self.delay = 0
        if self.rabbit is None:
            self.relativeMove([FORWARD, RIGHT, LEFT, BACK])
            self.symbol = ["^", ">", "v", "<"][self.direction]
        else: # TODO: move towards rabbit
            self.relativeMove([FORWARD, RIGHT, LEFT, BACK])
            self.symbol = ["^", ">", "v", "<"][self.direction]
    
    def collide(self, thing):
        if thing.name == "mirror": # Run backwards 
            self.turn(BACK)
            self.move()
            self.move()

        if thing.name == "chess": # Nap for one tick
            self.delay = 1

        if thing.name == "feather": # Sneeze
            p = self.grid.positionOf(self)
            d = self.direction

            self.move()

            self.rabbit = Rabbit()
            self.rabbit.spawn(self.grid, p, d)
            self.rabbit.turn(BACK)
            self.rabbit.move()

        if thing.name == "rabbit": # pick up rabbit
            self.grid.removeThing(thing)
            self.rabbit = None
