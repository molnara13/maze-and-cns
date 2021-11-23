import numpy as np
from PIL import Image
from matplotlib import cm

class State:
    

    def __init__(self, env):

            self._agent_view_by_cell = self._init_view(env)
            self.create_image_view()

    def _init_view(self, env):
            pass

    def create_image_view(self):
            state_array = self._agent_view_by_cell
            image_base = np.uint8(env.colormap(image_base)*255)
            im = Image.fromarray(image_base)
            
            return im

    def display(self):
            pass
