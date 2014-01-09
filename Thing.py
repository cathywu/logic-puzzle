from Grid import *

FORWARD = 0
RIGHT = 1
LEFT = -1
BACK = 2

class Thing:
    def __init__(self, name, symbol, delay=-1):
        self.name = name
        self.symbol = symbol
        self.delay = delay 
        self.hasMoved = False

    def spawn(self, grid, startPos, startDir=NORTH):
        self.grid = grid
        grid.addThing(self, startPos)
        self.direction = startDir
        self.clock = 0

    def tick(self):
        if self.clock == self.delay:
            self.clock = 0
            self.move()
            self.hasMoved = True
        else:
            self.clock += 1

    def moved(self):
        ret = self.hasMoved
        self.hasMoved = False
        return ret

    def move(self):
        pass

    def collide(self, thing):
        pass

    def turn(self, direction):
        self.direction = (self.direction + direction) % 4

    def relativeMove(self, relative):
        absolute = [(self.direction + r) % 4 for r in relative]
        self.grid.moveThing(self, absolute)

class Mirror(Thing):
    def __init__(self):
        Thing.__init__(self, "mirror", 'm')

class Chess(Thing):
    def __init__(self):
        Thing.__init__(self, "chess", unichr(9823))

class Feather(Thing):
    def __init__(self):
        Thing.__init__(self, "feather", 'F')

class Rabbit(Thing):

    def __init__(self):
        Thing.__init__(self, "rabbit", "r", 1)
        self.lastTurn = RIGHT
        self.isMovable = True

    def move(self):
        if self.lastTurn == RIGHT:
            d = self.direction
            self.relativeMove([LEFT, RIGHT, FORWARD, BACK])
            if (self.direction - d) % 4 == LEFT % 4:
                self.lastTurn = LEFT
        else:
            d = self.direction
            self.relativeMove([RIGHT, LEFT, FORWARD, BACK])
            if (self.direction - d) % 4 == RIGHT % 4:
                self.lastTurn = RIGHT

class Alice(Thing):
    def __init__(self):
        Thing.__init__(self, "alice", "A", 0)
        self.rabbit = None
        self.isMovable = True

    def move(self):
        self.delay = 0
        if self.rabbit is None:
            self.relativeMove([FORWARD, RIGHT, LEFT, BACK])
            self.symbol = ["^", ">", "v", "<"][self.direction]
        else: # Move closer NS if possible, else move closer EW if possible, else stay still
            p = self.grid.positionOf(self)
            r = self.grid.positionOf(self.rabbit)

            dx = r[0] - p[0]
            dy = r[1] - p[1]

            step = []
            if dx > 0:
                step += [SOUTH]
            elif dx < 0: 
                step += [NORTH]
            if dy > 0: 
                step += [EAST]
            elif dy < 0:
                step += [WEST]

            self.grid.moveThing(self, step)
            self.symbol = ["^", ">", "v", "<"][self.direction]
    
    def collide(self, thing):
        if thing.name == "mirror": # Run backwards 
            self.turn(BACK)
            self.relativeMove([FORWARD])
            # self.relativeMove([FORWARD])

        if thing.name == "chess": # Nap for one tick
            self.delay = 1

        if thing.name == "feather": # Sneeze
            p = self.grid.positionOf(self)
            d = self.direction

            # Step forwards
            self.relativeMove([FORWARD, RIGHT, LEFT, BACK])

            # Drop rabbit 
            if self.rabbit is None:
                self.rabbit = Rabbit()
                self.rabbit.spawn(self.grid, p, d)
                # self.rabbit.turn(BACK)

                '''
                # Throw rabbit backwards
                self.rabbit.relativeMove([FORWARD, RIGHT, LEFT, BACK])
                if (self.direction - d) % 4 == LEFT % 4:
                    self.lastTurn = LEFT
                '''

                # Rabbit hops
                self.rabbit.move()

        if thing.name == "rabbit": # pick up rabbit
            self.grid.removeThing(thing)
            self.rabbit = None
