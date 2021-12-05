class Neighbour:
    def __init__(self,
            coordinates,
            origin,
            #neighbours,
            separate_cells,
            is_wall_separated=None):

        self.coordinates = coordinates
        self.is_wall_separated = separate_cells(coordinates, origin)

class Cell:
    def __init__(
            self,
            coordinates,
            maze_size,
            separate_cells,
            type_=None
            ):
    
        self.coordinates = coordinates
        self.type_ = type_
        self._separate_cells = separate_cells
        self._maze_size = maze_size
        self.init_neighbours()

    def update_type_(self, new_type_):
            self.type_ = new_type_

    def init_neighbours(self):

            def get_neighbour_coordinates(self):

                    def is_in_range(neighbour):
                            return ((0, 0) <= neighbour < self._maze_size)

                    def remove_out_of_range_coordinates(coords):
                            coords = list(filter(is_in_range, coords))

                    y, x = self.coordinates
                    neighbour_coords = []
                    for j in range(y-1, y+2):
                        for i in range(x-1, x+2):
                            neighbour_coords.append((y, x))
                    remove_out_of_range_coordinates(neighbour_coords)

                    return neighbour_coords

            origin = self.coordinates
            separate_cells = self._separate_cells
            neighbours = []
            neighbour_coordinates = get_neighbour_coordinates(self)
            for coords in neighbour_coordinates:
                    neighbour = Neighbour(
                        coords,
                        origin,
                        separate_cells)
                    neighbours.append(neighbour)

            self.neighbours = neighbours
