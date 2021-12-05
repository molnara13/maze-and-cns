import numpy as np
from PIL import Image

class State:

    cell_type_encoding = {
                "unvisited": 0,
                "visited": 1,
                "wall": 2,
                "negative_clue": 3,
                "positive_clue": 4,
                "goal": 5,
                "occupied_by_agent": 6 
                }


    def __init__(self, agent_position, visible_cells, colormap):
            self._agent_position = agent_position
            self._visible_cells = visible_cells
            self._colormap = colormap
            self._cell_view = self._create_cell_view()
            self.image_view = self._create_image_view()
            #self.display()

    def _create_cell_view(self):

            def set_all_to_wall():
                    return np.zeros((3*3))*2

            def encode_cell_type(cell_type):

                    return cell_type_encoding[cell_type]

            def transform_(self, neighbour_location):
                    agent_position = np.asarray(self._agent_position)
                    environment_location = np.asarray(neighbour_location)
                    view_location = np.subtract(
                                        agent_position,
                                        environment_location
                                        )
                    return tuple(map(tuple, view_location))

            view_array = set_all_to_wall()
            for cell in self._visible_cells:
                    cell_location = cell.coordinates
                    cell_type = cell.type_
                    y, x = transform_(self, cell_location)
                    view_array[y][x] = encode_cell_type(cell_type)

            return view_array
            
 
    def _create_image_view(self):
            image_base = np.uint8(self._colormap(self._cell_view)*255)
            im = Image.fromarray(image_base)
            return im

    def display(self):
            im = self.image_view
            im.resize((200, 200)).show()
