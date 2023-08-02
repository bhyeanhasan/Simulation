import math
import matplotlib.pyplot as plt


def poisson_distribution(lambd, x):
    # lambd = average_rate_of_event
    # x = number_of_event_occurring
    return (math.exp(-lambd) * (lambd ** x)) / math.factorial(x)


for x in [5, 10, 15]:
    for i in range(11):
        val = poisson_distribution(x, i)
        plt.bar(i, val)
        print(val)
    plt.show()
