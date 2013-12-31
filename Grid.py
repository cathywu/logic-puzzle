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

    def addThing(self, thing, (x, y)):
        self.blocks[x][y] = thing

    def getThing(self,(x,y)):
        return self.blocks[x][y]

    def hasThing(self,(x,y)):
        return not self.getThing([x,y]) is None

    def add_vwall(self, x, y):
        self.vwalls[x,y] = 1

    def is_vwall(self,x,y):
        return self.vwalls[x,y]

    def add_hwall(self, x, y):
        self.hwalls[x,y] = 1

    def is_hwall(self,x,y):
        return self.hwalls[x,y]

    def addNWall(self, (x,y)):
      self.add_hwall(x, y)
    def addSWall(self, (x,y)):
      self.add_hwall(x+1, y)
    def addWWall(self, (x,y)):
      self.add_vwall(x, y)
    def addEWall(self, (x,y)):
      self.add_vwall(x, y+1)

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

            # print self.blocks[i,:]
            # print ' '.join(['X' if bool(x) is not None else 'yyyy' for x in self.blocks[i,:]])
        print "+" + "+".join(["=" if w else " " for w in self.hwalls[self.x]]) + "+"

if __name__ == '__main__':
    g = Grid(4, 10)
    g.addNWall([0,0])
    g.addSWall([0,0])
    g.addWWall([0,0])
    g.addEWall([0,0])
    g.draw_grid()
