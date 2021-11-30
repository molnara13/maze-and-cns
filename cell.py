class Connection:
    def __init__(self,
            coordinates,
            neighbours,
            wall_separated=None):

        y, x = coordinates
        self.neighbours = neighbours
        self.wall_separated = wall_separated

    def update_separation(self, wall_separated):
            self.wall_separated = wall_separated

class Cell:
    def __init__(
            self,
            coordinates,
            cell_type=None,
            connections=None):
    
        self.coordinates = coordinates
        self.cell_type = cell_type
        self.connections = connections

    def update_cell_type(self, new_cell_type):
            self.cell_type = new_cell_type

    def generate_connections(self, maze_size, separate_cells):

            def remove_out_of_range_neighbours(size, neighbours):

                    def is_out_of_range(size, neighbour):
                            return (not (0, 0) <= neighbour < size)

                    for neighbour in neighbours:
                        if is_out_of_range(size, neighbour):
                            neighbours.remove(neighbour)

            def new_connection(self, neighbour):
                    connection = Connection(self.coordinates, neighbour)
                    self.connections.append(connection)
            
            def get_neighbours(self):
                    y, x = self.coordinates
                    neighbours = [(y, x-1), (y-1, x), (y+1, x), (y, x+1)]
                    remove_out_of_range_neighbours(maze_size, neighbours)

                    return neighbours

            def init_connections(self):
                    self.connections = []
                    neighbours = get_neighbours(self)
                    for neighbour in neighbours:
                            new_connection(self, neighbour)

            def update_neighbour_separations(self, separate_cells):
                    for connection in self.connections:

                            cell1 = self.coordinates
                            cell2 = connection.neighbours
                            wall_separated = separate_cells(cell1, cell2)
                            connection.update_separation(wall_separated)

            init_connections(self)
            update_neighbour_separations(self, separate_cells)
