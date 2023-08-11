import random
import numpy as np
import matplotlib.pyplot as plt


def MM1(maximum_number_of_customers, mean_arrival_time, mean_service_time):
    customer = []
    wait_time = []
    system_idle_time = 0
    time = 0.0
    number_of_process = maximum_number_of_customers

    for i in range(number_of_process):
        arrival = np.random.exponential(1 / mean_arrival_time) * 60
        service = np.random.exponential(1 / mean_service_time) * 60
        data = [arrival, service]
        customer.append(data)

    customer.sort(key=lambda x: x[0])
    print(customer)

    for i in range(number_of_process):

        if time < customer[i][0]:  # System delay calculate kore nilam
            system_idle_time += abs(time - customer[i][0])
            time = customer[i][0]

        if time > customer[i][0]: # Wait time calculation
            wait_time.append(abs(time - customer[i][0]))
        else:
            wait_time.append(0)

        time = time + customer[i][1]

    average_wait = sum(wait_time) / number_of_process
    print("Average Delay in Queue ", round(average_wait, 2), " Seconds")
    average_sytem_idle = ((time - system_idle_time) / time) * 100
    print("System utilization ", round(average_sytem_idle, 2), " %")
    print("Time Simulation Ended ", round(time, 2), " Seconds")

    plt.barh(y=[i for i in range(number_of_process)], width=wait_time, left=[i[0] for i in customer])
    plt.show()


MM1(5, 53.33, 17.5)
