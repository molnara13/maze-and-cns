from maze_environment import MazeEnvironment as env
from agent import Agent
from torchvision import transforms

class MazeAgent(Agent):

    def __init__(self, self_aware=None, number_of_averaged=None):
            super().__init__(self_aware, number_of_averaged)

    def process_image_input(self, im):
            transform = transforms.Compose([transforms.ToTensor()])
            image_as_tensor = transform(im)
            return image_as_tensor
