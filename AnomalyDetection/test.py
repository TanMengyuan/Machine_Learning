import numpy as np
import matplotlib.pyplot as plt

def Gauss(x, mu_, sigma_):
    return (1 / np.sqrt(2 * np.pi)) * np.exp(- np.square(x - mu_) / (2 * np.square(sigma_)))

np.random.seed(1)
x_data = 10 * np.random.randn(100000)
x_data = np.append(x_data, 80)
plt.hist(x_data, bins=40, normed=0)
plt.show()
mu = np.mean(x_data)
sigma = np.sqrt(np.var(x_data))
# print(x_data)
# print(mu, sigma)
for each in x_data:
    print(Gauss(each, mu, sigma))