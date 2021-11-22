from cell import Cell

class Grid:

    def __init__(self, size, separate=None, clues=None, goal=None):
            self.size = size
            self._separate = separate
            self._clues = clues
            self._goal = goal
            self.init_cells()

    def init_new_cell(self, indices):
            cell = Cell(indices, "unvisited")
            if self._separate:
                cell.generate_connections(self.size, _self.separate)


    def init_cells(self):

            n, k = self.size
            cells = [[] for i in range(n)]
            for i in range(n):
                for j in range(k):
                    cell = self.init_new_cell((i, j))
                    cells[i].append(cell)
            self.cells = cells



