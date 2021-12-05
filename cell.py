class Neighbour:
    def __init__(self,
            coordinates,
            #neighbours,
            is_wall_separated=None):

        self.coordinates = coordinates
        self.is_wall_separated = is_wall_separated

    def update_separation(self, is_wall_separated):
            self.is_wall_separated = is_wall_separated

class Cell:
    def __init__(
            self,
            coordinates,
            type_=None,
            neighbours=[]):
    
        self.coordinates = coordinates
        self.type_ = type_
        self.neighbours = neighbours

    def update_type_(self, new_type_):
            self.type_ = new_type_

    def generate_neighbours(self, maze_size, separate_cells):

            def remove_out_of_range_neighbours(size, neighbours):

                    def is_out_of_range(size, neighbour):
                            return (not (0, 0) <= neighbour < size)

                    for neighbour in neighbours:
                        if is_out_of_range(size, neighbour):
                            neighbours.remove(neighbour)

            def new_neighbour(self, neighbour):
                    neighbour = Neighbour(self.coordinates)
                    self.neighbours.append(neighbour)
            
            def get_neighbours(self):
                    y, x = self.coordinates
                    neighbours = [(y, x-1), (y-1, x), (y+1, x), (y, x+1)]
                    remove_out_of_range_neighbours(maze_size, neighbours)

                    return neighbours

            def init_neighbours(self):
                    self.neighbours = []
                    neighbours = get_neighbours(self)
                    for neighbour in neighbours:
                            new_neighbour(self, neighbour)

            def update_neighbour_separations(self, separate_cells):
                    for neighbour in self.neighbours:

                            cell1 = self.coordinates
                            cell2 = neighbour.coordinates
                            is_wall_separated = separate_cells(cell1, cell2)
                            neighbour.update_separation(is_wall_separated)

            init_neighbours(self)
            update_neighbour_separations(self, separate_cells)
