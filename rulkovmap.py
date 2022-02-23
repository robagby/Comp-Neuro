import numpy as np
import matplotlib.pyplot as plt


class RulkovMap(object):


    def __init__(self, alpha, u, sigma):
        self.alpha = alpha
        self.u     = u
        self.sigma = sigma


    def run(self, x0, y0, t):
        x = np.array([x0 for _ in range(t+1)])
        y = np.array([y0 for _ in range(t+1)])
        for n in range(t):
            x[n+1] = (self.alpha / (1.+x[n]**2)) + y[n]
            y[n+1] = y[n] - self.u*(x[n] - self.sigma)

        self.x = x[:-1]
        self.t = np.arange(t)


    def plot(self):
        plt.figure()
        plt.title('Rulkov Map')
        plt.plot(self.t, self.x)
        plt.ylabel('X')

        plt.show()