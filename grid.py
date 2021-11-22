from cell import Cell

class Grid:

    def __init__(self, size, separate=None, clues=None, goal=None):
            self.size = size
            self._separate = separate
            self._clues = clues
            self._goal = goal
            self.init_cells()

    def init_new_cell(self, indices):

            cell_type = self.get_cell_type_from_indices(indices)
            cell = Cell(indices, cell_type)
            if self._separate:
                cell.generate_connections(self.size, self._separate)

    def get_cell_type_from_indices(self, indices):

            if indices == self._goal:
                cell_type = "goal"
            elif (self._clues) and (indices in self._clues):

                cell_type = "clue"
            else:
                cell_type = "unvisited"

            return cell_type

    def init_cells(self):

            n, k = self.size
            cells = [[] for i in range(n)]
            for i in range(n):
                for j in range(k):
                    cell = self.init_new_cell((i, j))
                    cells[i].append(cell)
            self.cells = cells



