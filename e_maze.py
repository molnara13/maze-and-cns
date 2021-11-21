from maze import Maze
from grid import Grid

class E_Maze(Maze):


    def __init__(self):
            #Maze.__init__(self)
            self.size = (3, 3)
            self.start = (2, 1)
            self.goal = (0, 0)
            self.init_grid()

    def init_grid(self):

            self.grid = Grid(self.size, self.separate)


    def separate(self, start, end):
            walls = [
                ((1, 0), (1, 1)),
                ((1, 1), (1, 2)),
                ((2, 0), (2, 1)),
                ((2, 1), (2, 2)),
                ]
            if ((start, end) in walls) or ((end, start) in walls):
                return True
            else:
                return False
