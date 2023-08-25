import numpy as np


def exponential_probability(rate_parameter, time):
    lambda_ = 1 / rate_parameter
    return 1 - np.exp(-lambda_ * time)


# Given rate parameter (average time between waves)
average_time_between_waves = 100

# Given time (in this case, 120 days)
time_for_next_wave = 120

# Calculate the probability for the given time using the Exponential distribution
probability = exponential_probability(average_time_between_waves, time_for_next_wave)

print(f"The probability that it will take more than 120 days for the next wave to occur is: {probability:.4f}")

# Simulate Exponential distributions with different rate parameters
rate_parameters = [0.5, 1.0, 2.0, 4.0]
for rate_parameter in rate_parameters:
    samples = np.random.exponential(scale=1 / rate_parameter, size=1000)
    mean_time = np.mean(samples)
    print(f"Simulated mean time between waves (rate parameter = {rate_parameter}): {mean_time:.2f} days")
