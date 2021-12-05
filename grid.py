from cell import Cell

class Grid:

    def __init__(self, size, separate_cells=None, clues=None, goal=None):
            self.size = size
            self._separate_cells = separate_cells
            self._clues = clues
            self._goal = goal
            self.init_cells()

    def get_cell_type_from_location(self, location):

            if location == self._goal:
                cell_type = "goal"
            elif (self._clues) and (location in self._clues):

                cell_type = "clue"
            else:
                cell_type = "unvisited"

            return cell_type

    def init_cells(self):

            n, k = self.size
            cells = [[] for i in range(n)]
            for i in range(n):
                for j in range(k):
                    cell_type = self.get_cell_type_from_location((i, j))
                    cell = Cell(
                        (i, j),
                        self.size,
                        self._separate_cells,
                        cell_type
                        )

                    cells[i].append(cell)
            self.cells = cells
            
    def get_cell_from_location(self, location):
            y, x = location
            return self.cells[y][x]

    def get_neighbour_cells(self, cell_location, filter_=True):

            cell = self.get_cell_from_location(cell_location)
            neighbours = cell.neighbours
            filtered_neighbours = list(filter(filter_, neighbours))
            neighbour_cells = [
                self.get_cell_from_location(neighbour.location)
                for neighbour in filtered_neighbours
                ]

            return neighbour_cells



