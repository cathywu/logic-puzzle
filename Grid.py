import numpy as np

class Grid:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.blocks = np.zeros((self.x,self.y))
        self.vwalls = np.zeros((self.x,self.y+1))
        self.hwalls = np.zeros((self.x+1,self.y))

    def add_obstacle(self, x, y):
        self.blocks[x,y] = 1

    def is_obstacle(self,x,y):
        return self.blocks[x,y]

    def add_vwall(self, x, y):
        self.vwalls[x,y] = 1

    def is_vwall(self,x,y):
        return self.vwalls[x,y]

    def add_hwall(self, x, y):
        self.vwalls[x,y] = 1

    def is_hwall(self,x,y):
        return self.hwalls[x,y]

    def draw_grid(self):
        for i in range(self.y):
            print self.blocks[i,:]
            # print ' '.join(['X' if bool(x) is not None else 'yyyy' for x in self.blocks[i,:]])
