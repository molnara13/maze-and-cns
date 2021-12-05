"""

"""
from matplotlib import cm

from environment import Environment
from maze import Maze
from e_maze import E_Maze
from cell import Cell
from maze_state import State

class MazeEnvironment(Environment):


    def __init__(
            self,
            maze_type="e_maze",
            t=0,
            colormap=cm.nipy_spectral,
            state=None):

            super().__init__()
            
            self.t = t
            self.init_maze(maze_type)
            self.agent_position = self.maze.start
            self.colormap = colormap
            self.state = State(self)

    def init_maze(self, maze_type):
            if maze_type == "e_maze":
                self.maze = E_Maze()

    def update(self, action):

        def is_collision(action):
                pass

        def update_agent_position(self, action):
                self.agent_position = action

        def set_cell_type_to_visited(self):

                cell = self.get_cell_from_coords(self.agent_position)
                cell.update_cell_type("visited")

        if not is_collision(action):
            self.update_agent_position(action)
            self.set_cell_type_to_visited(self.agent_position)
            self.generate_state()



    def is_episode_ending(self):
        if self.agent_position == goal:
            return True
        else:
            return False

    def give_feedback(self):

            if not self.is_episode_ending():
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
        
    def get_cell_from_coords(self, coords):
            return self.maze.get_cell_from_coords(coords)

    def get_cell_type_from_coords(self, coords):
            cell = self.get_cell_from_coords(coords)
            return cell.type_
