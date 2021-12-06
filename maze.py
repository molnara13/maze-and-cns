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
        
    def get_cell_from_location(self, location):
            return self.grid.get_cell_from_location(location)

    def get_neighbour_cells(self, cell_location, filter_):
            return self.grid.get_neighbour_cells(cell_location, filter_)

