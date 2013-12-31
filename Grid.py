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
        self.vwalls[x,y] = 1

    def is_hwall(self,x,y):
        return self.hwalls[x,y]

    def getWalls(self, (x, y)):
        return [self.vwals[x,y], self.hwals[
    def draw_grid(self):
        for i in range(self.y):
            print self.blocks[i,:]
            # print ' '.join(['X' if bool(x) is not None else 'yyyy' for x in self.blocks[i,:]])
