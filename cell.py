class Neighbour:
    def __init__(self,
            location,
            origin,
            #neighbours,
            separate_cells
            ):

        self.location = location
        self.is_wall_separated = separate_cells(location, origin)

class Cell:
    def __init__(
            self,
            location,
            get_neighbour_locations,
            separate_cells,
            type_=None
            ):
    
        self.location = location
        self.type_ = type_
        self._separate_cells = separate_cells
        self._get_neighbour_locations = get_neighbour_locations
        self.init_neighbours()

    def update_type_(self, new_type_):
            self.type_ = new_type_

    def init_neighbours(self):

            origin = self.location
            separate_cells = self._separate_cells
            neighbours = []
            neighbour_locations = self._get_neighbour_locations(self.location)

            for neighbour_location in neighbour_locations:
                    neighbour = Neighbour(
                        neighbour_location,
                        origin,
                        separate_cells)
                    neighbours.append(neighbour)

            self.neighbours = neighbours
