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
            pass

    def create_image_view(self, env):
            image_base = np.uint8(env.colormap(self._agent_view_by_cell)*255)
            im = Image.fromarray(image_base)
            self.image_view = im

    def display(self):
            im = self.image_view
            im.resize((200, 200)).show()
