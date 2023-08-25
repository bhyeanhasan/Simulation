import math
import numpy as np
import matplotlib.pyplot as plt


def normal_random_number(mean, deviation):
    return mean + deviation * np.random.randn()


rnn = []
mean = 100
standard_deviation = 20

for i in range(200):
    x = normal_random_number(mean, standard_deviation)
    rnn.append(x)

plt.hist(rnn, bins=20, density=True)

x = np.linspace(min(rnn), max(rnn), 200)
unimodal_curve = (1 / (standard_deviation * np.sqrt(2 * np.pi))) * np.exp(
    -((x - mean) ** 2) / (2 * standard_deviation ** 2))

# Plot the multimodal density curves
mean2 = 80
standard_deviation2 = 20
multimodal_curve = (1 / (standard_deviation * np.sqrt(2 * np.pi))) * np.exp(
    -((x - mean) ** 2) / (2 * standard_deviation ** 2)) + (1 / (standard_deviation2 * np.sqrt(2 * np.pi))) * np.exp(
    -((x - mean2) ** 2) / (2 * standard_deviation2 ** 2))

plt.plot(x, unimodal_curve, label='Unimodal', color='red')
plt.plot(x, multimodal_curve, label='Multimodal', color='black')
plt.show()
