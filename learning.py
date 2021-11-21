"""

"""

#from deep_q_maze_agent import DeepQMazeAgent
from maze_agent import MazeAgent
from maze_environment import MazeEnvironment

if __name__ == "__main__":
    """Play a given number of episodes.

    Track the learning process and plot the learning curve."""

    #agent = DeepQMazeAgent()
    agent = MazeAgent()

    number_of_averaged = 100
    episode_count = 1000
 
    for i in range(episode_count):

        env = MazeEnvironment()
        agent.play_episode(env)
        
        if i % number_of_averaged == 0:
            agent.update_score_means(number_of_averaged)
            agent.check()

    agent.summarize()
    