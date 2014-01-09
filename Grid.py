import numpy as np
from itertools import combinations

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

def nextCell(position, direction):
    if direction == NORTH:
        return [position[0] - 1, position[1]]
    if direction == SOUTH:
        return [position[0] + 1, position[1]]
    if direction == WEST:
        return [position[0], position[1] - 1]
    if direction == EAST:
        return [position[0], position[1] + 1]
    return position

def index2d(myList, v):
    for i, x in enumerate(myList):
      for j, y in enumerate(x):
        if v in y:
            return (i, j)

class Grid:
    '''
      N
    W o--> y , E
      | block[x][y]
      v
      x
      S

    '''

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cells = [[[] for i in range(y)] for j in range(x)]
        self.vwalls = np.zeros((self.x,self.y+1))
        self.hwalls = np.zeros((self.x+1,self.y))

        for i in range(x):
          self.addWall((i,0), WEST)
        for i in range(x):
          self.addWall((i,y-1), EAST)
        for i in range(y):
          self.addWall((0,i), NORTH)
        for i in range(y):
          self.addWall((x-1,i), SOUTH)

        self.things = {}

    def tick(self):
        for t in self.things.keys():
            t.tick()
            if t.moved():
                print t.name
                self.draw_grid()
                raw_input("")

    def addThing(self, thing, (x, y)):
        self.removeThing(thing)
        self.cells[x][y].append(thing)
        self.things[thing] = 1
        for t in self.cells[x][y][:-1]:
            t.collide(thing)
            thing.collide(t)

    def getThings(self,(x,y)):
        return self.cells[x][y]

    def removeThing(self, thing):
        p = self.positionOf(thing)
        self.things.pop(thing, None)
        if p:
            self.getThings(p).remove(thing)
        return p

    def positionOf(self, thing):
        return index2d(self.cells, thing)

    def moveThing(self, thing, directions):
        p = self.positionOf(thing)
        if not p:
            return
        for d in directions:
            if not self.getWall(p, d):
                n = nextCell(p, d)
                thing.direction = d
                self.addThing(thing, n)
                return d
        return None

    def addWallRightOf(self, x, y):
        self.vwalls[x,y] = 1

    def addWallBelow(self, x, y):
        self.hwalls[x,y] = 1

    def delWallRightOf(self, x, y):
        self.vwalls[x,y] = 0

    def delWallBelow(self, x, y):
        self.hwalls[x,y] = 0

    def addWall(self, (x,y), direction):
      if direction == NORTH:
        self.addWallBelow(x, y)
      elif direction == SOUTH:
        self.addWallBelow(x+1, y)
      elif direction == WEST:
        self.addWallRightOf(x, y)
      elif direction == EAST:
        self.addWallRightOf(x, y+1)

    def delWall(self, (x,y), direction):
      if direction == NORTH:
        self.delWallBelow(x, y)
      elif direction == SOUTH:
        self.delWallBelow(x+1, y)
      elif direction == WEST:
        self.delWallRightOf(x, y)
      elif direction == EAST:
        self.delWallRightOf(x, y+1)

    def addWall180(self, (x,y), direction):
        self.addWall((x, y), direction)
        self.addWall((self.x - x - 1, self.y - y - 1), (direction + 2) % 4)

    def addWallQuad(self, (x,y), direction):
        self.addWall180((x, y), direction)
        self.addWall180((y, self.y - x - 1), (direction + 1) % 4)

    def getWall(self, (x,y), direction):
      if direction == NORTH:
        return self.hwalls[x, y]
      elif direction == SOUTH:
        return self.hwalls[x+1, y]
      elif direction == WEST:
        return self.vwalls[x, y]
      elif direction == EAST:
        return self.vwalls[x, y+1]

    def getWalls(self, (x, y)):
        return [self.getWall((x,y), d) for d in [NORTH, EAST, SOUTH, WEST]]

    def draw_grid(self):
        delim = "+"
        for r, row in enumerate(self.cells):
            print delim.join([""] + ["-" if w else " " for w in self.hwalls[r]] + [""]) 

            walls = ["|" if w else " " for w in self.vwalls[r]]
            cells = [" " if not t else t[-1].symbol for t in row]
            rowstring = walls + cells
            rowstring[::2] = walls
            rowstring[1::2] = cells
            print "".join(rowstring)

        print delim.join([""] + ["-" if w else " " for w in self.hwalls[self.x]] + [""]) 

if __name__ == '__main__':
    g = Grid(8, 8)
    #g.addWall([1,0], EAST)
    #g.addWall([2,0], EAST)
    #g.addWall180([1,0], EAST)
    g.addWallQuad([2,0], EAST)
    g.addWallQuad([4,0], EAST)
    g.addWallQuad([2,1], SOUTH)
    g.addWallQuad([1,2], SOUTH)
    g.addWallQuad([3,2], SOUTH)
    g.addWallQuad([3,2], EAST)
    g.draw_grid()

    print g.getWalls((0,1))

