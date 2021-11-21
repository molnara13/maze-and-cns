"""

"""
from PIL import Image

from environment import Environment
from maze import Maze
from e_maze import E_Maze
from cell import Cell

class MazeEnvironment(Environment):



    def __init__(self, maze_type="e_maze", t=0, state=None):

            super().__init__()
            
            self.t = t
            self.init_maze(maze_type)
            self.agent_position = self.maze.start
            self.state = self.generate_state()

    def init_maze(self, maze_type):
            if maze_type == "e_maze":
                self.maze = E_Maze()

    def generate_state(self):
            pass

    def display_state(self):
            pass

    def update(self, action):

        def bump(action):
                pass

        if not bump(action):
            self.maze.grid.cells[action].update_cell_type("visited")
            self.update_agent_position(action)
            self.generate_state()

    def update_agent_position(self, action):
        self.agent_position = action

    def end_of_episode(self):
        if self.agent_position == goal:
            return True
        else:
            return False

    def give_feedback(self):

            if not self.end_of_episode():
                reward, done = -1, False
            else:
                reward, done = 0, True

            return reward, done

    def step(self, action):



            self.t += 1
            self.update(action)
            state = self.state
            reward, done = self.give_feedback()

            return state, reward, done
