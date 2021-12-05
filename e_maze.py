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

            self.grid = Grid(self.size, self.separate_cells)


    def separate_cells(self, cell1, cell2):
            walls = [
                ((1, 0), (1, 1)),
                ((1, 1), (1, 2)),
                ((2, 0), (2, 1)),
                ((2, 1), (2, 2)),
                ]
            if ((cell1, cell2) in walls
                    or (cell2, cell1) in walls
                    or cell1 == cell2):
                return True
            else:
                return False
