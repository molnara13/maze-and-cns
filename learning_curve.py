"""Make a learing curve.

"""
import matplotlib.pyplot as plt
import numpy as np


def learning_curve(agent, data_list, color, plot_stride, alpha='', gamma='',):

    plot_title = (agent
                    + '(Alpha: '
                    + str(alpha)
                    + ', Gamma: '
                    + str(gamma) + ')')

    plt.plot(data_list, color=color)
    plt.title(plot_title)
    plt.xlabel('Number of episodes (1000)')
    plt.ylabel('Average rewards')
    plt.show()