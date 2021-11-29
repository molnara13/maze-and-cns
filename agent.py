from environment import Environment as env
import numpy as np
from learning_curve import learning_curve

class Agent:

    def __init__(
            self,
            self_aware=False,
            number_of_averaged=1000):

            self.self_aware = self_aware
            self.scores = []
            self.score_means = []
    
    def play_episode(self, env):
            done = False
            score = 0
            s = env.state
            while not done:
                action = self.choose_action(s)
                s_, reward, done  = env.step(action)
                self.learn(s, action, reward, s_)
                score += reward
                s = s_
            self.add_score(score)

    def add_score(self, score):
            self.scores.append(score)

    def update_score_means(self, number_of_averaged):
            score_mean = np.mean(self.scores[-number_of_averaged:])
            self.score_means.append(score_mean)

    def check(self):
            print('episode: ', i, 'score_mean: ', score_mean)

    def summarize(self):
            learning_curve(
                agent='Q-learning',
                data_list=self.score_means,
                alpha=self.alpha,
                gamma=self.gamma,
                color='green')

    def choose_action(self, state):
            pass

    def learn_action(self, action):
            pass



