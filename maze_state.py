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


    def __init__(self, agent_position, subgrid, colormap):
            self._agent_position = agent_position
            self._subgrid = subgrid
            self._colormap = colormap
            self._cell_view = self._create_cell_view()
            self.image_view = self._create_image_view()
            #self.display()

    def _create_cell_view(self):

            def set_all_to_wall():
                    return np.zeros((3*3))*2

            def encode_cell_type(cell_type):

                    return cell_type_encoding[cell_type]

            def transform_(self, neighbour_coords):
                    agent_position = np.asarray(self._agent_position)
                    env_coords = np.asarray(neighbour_coords)
                    view_coords = np.subtract(
                                        agent_position,
                                        env_coords
                                        )
                    print('view_coords', view_coords)
                    return tuple(map(tuple, view_coords))

            view_array = set_all_to_wall()
            for cell in self._subgrid:
                    cell_coords = cell.coordinates
                    cell_type = cell.type_
                    y, x = transform_(self, cell_coords)
                    view_array[y][x] = encode_cell_type(cell_type)

            return view_array
            
 
    def _create_image_view(self):
            image_base = np.uint8(self._colormap(self._cell_view)*255)
            im = Image.fromarray(image_base)
            return im

    def display(self):
            im = self.image_view
            im.resize((200, 200)).show()
