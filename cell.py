class Neighbour:
    def __init__(self,
            location,
            origin,
            #neighbours,
            separate_cells,
            is_wall_separated=None):

        self.location = location
        self.is_wall_separated = separate_cells(location, origin)

class Cell:
    def __init__(
            self,
            location,
            maze_size,
            separate_cells,
            type_=None
            ):
    
        self.location = location
        self.type_ = type_
        self._separate_cells = separate_cells
        self._maze_size = maze_size
        self.init_neighbours()

    def update_type_(self, new_type_):
            self.type_ = new_type_

    def init_neighbours(self):

            def get_neighbour_locations(self):

                    def is_in_range(neighbour):
                            return ((0, 0) <= neighbour < self._maze_size)

                    def remove_out_of_range_location(locations):
                            locations = list(filter(is_in_range, locations))

                    y, x = self.location
                    neighbour_locationss = []
                    for j in range(y-1, y+2):
                        for i in range(x-1, x+2):
                            neighbour_locationss.append((y, x))
                    remove_out_of_range_location(neighbour_locationss)

                    return neighbour_locationss

            origin = self.location
            separate_cells = self._separate_cells
            neighbours = []
            neighbour_locations = get_neighbour_locations(self)
            for locations in neighbour_locations:
                    neighbour = Neighbour(
                        locations,
                        origin,
                        separate_cells)
                    neighbours.append(neighbour)

            self.neighbours = neighbours
