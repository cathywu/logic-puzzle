import numpy as np

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
        self.blocks = [[None for i in range(y)] for j in range(x)]
        self.vwalls = np.zeros((self.x,self.y+1))
        self.hwalls = np.zeros((self.x+1,self.y))

        for i in range(x):
          self.addWWall((i,0))
        for i in range(x):
          self.addEWall((i,y-1))
        for i in range(y):
          self.addNWall((0,i))
        for i in range(y):
          self.addSWall((x-1,i))

    def addThing(self, thing, (x, y)):
        self.blocks[x][y] = thing

    def getThing(self,(x,y)):
        return self.blocks[x][y]

    def hasThing(self,(x,y)):
        return not self.getThing([x,y]) is None

    def addWallRightOf(self, x, y):
        self.vwalls[x,y] = 1

    def addWallBelow(self, x, y):
        self.hwalls[x,y] = 1

    def addNWall(self, (x,y)):
      self.addWallBelow(x, y)
    def addSWall(self, (x,y)):
      self.addWallBelow(x+1, y)
    def addWWall(self, (x,y)):
      self.addWallRightOf(x, y)
    def addEWall(self, (x,y)):
      self.addWallRightOf(x, y+1)

    def getNWall(self, (x,y)):
      return self.hwalls[x, y]
    def getSWall(self, (x,y)):
      return self.hwalls[x+1, y]
    def getWWall(self, (x,y)):
      return self.vwalls[x, y]
    def getEWall(self, (x,y)):
      return self.vwalls[x, y+1]

    def getWalls(self, (x, y)):
        return [self.getNWall((x,y)), self.getEWall((x,y)), self.getSWall((x,y)), self.getWWall((x,y))]

    def draw_grid(self):
        for r, row in enumerate(self.blocks):
            print "+" + "+".join(["=" if w else " " for w in self.hwalls[r]]) + "+"

            walls = ["|" if w else " " for w in self.vwalls[r]]
            cells = [" " if t is None else t.symbol for t in row]
            rowstring = walls + cells
            rowstring[::2] = walls
            rowstring[1::2] = cells
            print "".join(rowstring)

        print "+" + "+".join(["=" if w else " " for w in self.hwalls[self.x]]) + "+"

if __name__ == '__main__':
    g = Grid(4, 10)
    g.addEWall([0,0])
    g.addEWall([1,0])
    g.addEWall([2,0])
    g.draw_grid()

    print g.getWalls((0,1))

