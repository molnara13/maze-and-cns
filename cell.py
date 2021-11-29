class Connection:
    def __init__(self,
            coordinates,
            neighbour_coordinates,
            wall_seperated=None):

        y, x = coordinates
        self.neighbour_coordinates = neighbour_coordinates
        self.wall_seperated = wall_seperated

    def update_separation(self, wall_seperated):
            self.wall_seperated = wall_seperated

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

    def generate_connections(self, maze_size, separate):

            def remove_out_of_range_neighbours(size, neighbours):

                    def is_out_of_range(size, neighbours):
                            return (not (0, 0) <= neighbour_coordinates < size)

                    for neighbour_coordinates in neighbours:
                        if is_out_of_range(size, neighbour_coordinates):
                            neighbours.remove(neighbour_coordinates)

            def new_connection(self, neighbour):
                    connection = Connection(self.coordinates, neighbour)
                    self.connections.append(connection)
            
            def get_neighbour_coordinates(self):
                    y, x = self.coordinates
                    neighbours = [(y, x-1), (y-1, x), (y+1, x), (y, x+1)]
                    remove_out_of_range_neighbours(maze_size, neighbours)

                    return neighbours

            def init_connections(self):
                    self.connections = []
                    neighbours = get_neighbour_coordinates(self)
                    for neighbour in neighbours:
                            new_connection(self, neighbour)

            def update_neighbour_separations(self, separate):
                    for connection in self.connections:

                            connection_start = self.coordinates
                            connection_end = connection.neighbour_coordinates
                            wall_separated = separate(
                                                connection_start,
                                                connection_end)
                            connection.update_separation(wall_separated)

            init_connections(self)
            update_neighbour_separations(self, separate)
