# Applications of Neuroscience Ideas at Maze Tasks
### Author: Anna Ágnes Molnár
This project is inspired by the article 'A Learning Gap Between Neuroscience and Reinforcement Learning' (Wauthier et al., 2021). The authors of this paper expand the T-maze rodent experiment into an E-maze task and implement it into an Atari-like game environment, where they experiment with state-of-the-art reinforcement learning agents. They conclude that model-free approaches fail at this task and more experiments are neccessary with model-based approaches, particularly with methods based on computational models of the human memory and/or reward system.

The authors outline the following difficulties of the task:
- sparse rewards
- large state space
- the agent-environment interaction can be described as a Markov decision process that is only partially observable

I would also like to add that some of the training practices described in this article are unusual. The number of steps in maze tasks are usually not this limited - typically, agents have the option to correct themselves. It can be expected that a single reward immediately before the end of an episode will not encourage learning for model-free agents as it has no feedback about the overall course of the episode. The agent needs to be able to make a connection between the clues and the reward, which means that either some form of premediated exploration or a model is neccessary with this tpye of rewarding. Another possibility is to change the rewarding system, which the authors do suggest.

In order to have an environment with flexible complexity, I am going to create a different maze environment whose resolution can be modified. I am going to start the training on a very small resolution environment to separate the measures of the difficulties of this task.

Possible versions of the maze:
-T-maze
-E-maze without windows
-E-maze with windows
-E-maze with reward clues

I also intend to use more complicated reward systems which is probably key in the effectiveness of biological agents at similar tasks. To mimic the learning process of biological agents, revisiting branches might be allowed.

Alternate reward systems:
-instead of finding the exit or circle (later:goal), negative rewards (punishments) might be introduced for time spent in the maze
-managing to have the goal in sight can be rewarded

Alternate reward systems suggested by the authors:
-intrinsic rewards

Methods tried by the authors:
Model-free:
-DQN
-Rainbow
-PPO
-RND
Model-based:
-Dreamer V2

Neuroscience ideas for new methods:
-Bayesian brain
-Active inference
-Adversarial brain

Neuroscience ideas for memory implementation:
-Hopfield networks
-Kanerva machines

## Resources:
A Learning Gap Between Neuroscience and Reinforcement Learning' (Wauthier et al., 2021) arXiv:2104.10995
