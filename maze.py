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

    def get_cell_type_from_coords(self, coords):
            retrn self.grid.get_cell_from_coords(coords)

