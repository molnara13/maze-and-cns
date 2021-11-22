"""

"""

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
                
    def get_agent_position_cell_type(self):
            coordinates = self.agent_position
            cells = self.maze.grid.cells
            return cells(coordinates).cell_type

    def generate_state(self):
            pass

    def display_state(self):
            pass

    def update(self, action):

        def bump(action):
                pass

        if not bump(action):
            self.set_cell_type_to_visited(action)
            self.update_agent_position(action)
            self.generate_state()

    def update_agent_position(self, action):
        self.agent_position = action

    def set_cell_type_to_visited(self, action):
            cell = self.maze.grid.cells[action]
            cell.update_cell_type("visited")

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
