import numpy as np

class Grid:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.blocks = np.zeros((self.x,self.y))
        self.walls = np.zeros((self.x+1,self.y+1))

    def add_obstacle(self, x, y):
        self.blocks[x,y] = 1

    def is_obstacle(self,x,y):
        return self.blocks[x,y]

    def add_wall(self, x, y):
        self.walls[x,y] = 1

    def is_wall(self,x,y):
        return self.walls[x,y]

