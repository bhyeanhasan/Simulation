import numpy as np
from matplotlib import pyplot as plt


def exponential_inverse_trans(n=1, mean=1):
    U = np.random.rand(n)
    X = -mean * np.log(1 - U)
    actual = np.random.exponential(scale=mean, size=n)

    plt.figure(figsize=(12, 9))
    plt.hist(X, bins=50, alpha=0.5, label="Generated r.v.")
    plt.title("Generated vs Actual %i Exponential Random Variables" % n)
    plt.legend()
    plt.show()
    return X


cont_example1 = exponential_inverse_trans(n=100, mean=4)
cont_example2 = exponential_inverse_trans(n=500, mean=4)
cont_example3 = exponential_inverse_trans(n=1000, mean=4)