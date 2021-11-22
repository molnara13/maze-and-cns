import numpy as np
from PIL import Image

class State:
    

    def __init__(self, env):

            self._agent_view_by_cell = self._init_view(env)
            self.create_image_view()
    

    def _init_view(self, env):
            pass

    def create_image_view(self):
            pass

    def display(self):
            pass