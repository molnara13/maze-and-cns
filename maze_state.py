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


    def __init__(self, env):
            self._agent_view_by_cell = self._init_view(env)
            self.create_image_view(env)
            #self.display()
    

    def _init_view(self, env):

            def update_view_cell_types(minigrid, env):

                    def update_view_cell_type(minigrid, env):

                            def env_coords_to_view_coords():
                                    pass

                            def encode_cell_type(cell_type):

                                    return cell_type_encoding[cell_type]

                            connection_coords = connecion.neighbour_coordinates
                            view_coords = env_coords_to_view_coords(
                                                    connection_coords)

                            minigrid(view_coords) = encode_cell_type(
                                                        env.get_cell_tpye_from_coords(
                                                            connection_coords
                                                            )
                                                        )

                    centre = env.maze.grid(env.agent_position)
                    for connection in centre.connections:
                            if not connecion.wall_separated:
                                update_view_cell_type(connection,
                                                        minigrid, env)

            minigrid = np.zeros((3*3))*2
            update_view_cell_types(minigrid, env)


            return minigrid

            
 
    def create_image_view(self, env):
            ####################################
            #distribute_values(self._agent_view_by_cell)
            image_base = np.uint8(env.colormap(self._agent_view_by_cell)*255)
            im = Image.fromarray(image_base)
            self.image_view = im
            #im.show()

    def display(self):
            im = self.image_view
            im.resize((200, 200)).show()
