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
            self.image_view = self.create_image_view(env)
            #self.display()
    

    def _init_view(self, env):

            def update_view_cell_types(minigrid, env):

                    def update_view_cell_type(neighbour, minigrid, env):

                            def env_coords_to_view_coords(
                                    env,
                                    neighbour_coords
                                    ):
                                agent_position = np.asarray(env.agent_position)
                                env_coords = np.asarray(neighbour_coords)
                                view_coords = np.subtract(
                                                    agent_position,
                                                    env_coords
                                                    )
                                return tuple(map(tuple, view_coords))


                            def encode_cell_type(cell_type):

                                    return cell_type_encoding[cell_type]

                            neighbour_coords = neighbour.coordinates
                            view_coords = env_coords_to_view_coords(
                                                env, neighbour_coords
                                                )
                            cell_type = env.get_cell_tpye_from_coords(
                                                neighbour_coords
                                                )
                            minigrid[view_coords] = encode_cell_type(cell_type)

                    centre = env.get_cell_from_coords(env.agent_position)
                    for neighbour in centre.neighbours:
                            if not neighbour.is_wall_separated:
                                update_view_cell_type(neighbour,
                                                        minigrid, env)

            minigrid = np.zeros((3*3))*2
            update_view_cell_types(minigrid, env)

            return minigrid

            
 
    def create_image_view(self, env):
            ####################################
            #distribute_values(self._agent_view_by_cell)
            image_base = np.uint8(env.colormap(self._agent_view_by_cell)*255)
            im = Image.fromarray(image_base)
            #im.show()
            return im

    def display(self):
            im = self.image_view
            im.resize((200, 200)).show()
