import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv('peobore.csv')


class norm1:
    def __init__(self, a1, b1, c1):
        self.a1 = a1
        self.b1 = b1
        self.c1 = c1

    def dist_curve(self):
        plt.plot(self.c1, 1 / (self.b1 * np.sqrt(2 * np.pi)) *
                 np.exp(- (self.c1 - self.a1) ** 2 / (2 * self.b1 ** 2)), linewidth=3, color='y')
        plt.show()

plt.xlabel("mean ")
plt.ylabel("standard deviation")
mu=int(np.mean(data.loc[0:,['borewell']]))
sigma=int(np.std(data.loc[0:,['people']]))

# print(mu)
# print(sigma)

s = np.random.normal(mu, sigma, 1000)



w1, x1, z1 = plt.hist(s, 100, normed=True)  # hist
hist1 = norm1(mu, sigma, x1)


plot1=hist1.dist_curve()
