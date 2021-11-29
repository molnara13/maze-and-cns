from grid import Grid
    
class Maze:

    def __init__(
            self,
            size=None,
            start=None,
            goal=None,
            clues=None):

        self.size = size
        self.start = start
        self.goal = goal
        self.clues = clues
        self.init_grid()

    def init_grid(self):
            pass
        
    def get_grid_cell_from_coordinates(self, coords):
        return self.grid.get_cell_from_coordinates(coords)

