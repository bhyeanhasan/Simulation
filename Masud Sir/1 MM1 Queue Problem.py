import random
import numpy as np


def MM1(total_time, mean_arrival_time, mean_service_time):
    inter_arrival_time = []
    service_time = []
    wait_time = []
    system_idle_time = []
    time = 0

    arrival_service_time = {}
    number_of_process = int(np.random.poisson(mean_arrival_time))

    for i in range(number_of_process):
        arrival = np.random.exponential(1 / mean_arrival_time) * 60 * 60
        inter_arrival_time.append(arrival)
        service = np.random.exponential(1 / mean_service_time) * 100
        service_time.append(service)
        arrival_service_time[arrival] = service

    inter_arrival_time.sort()

    for i in range(number_of_process):
        wait = time - inter_arrival_time[i]
        if wait > 0:
            wait_time.append(wait)
        else:
            wait_time.append(0)
            system_idle_time.append(abs(wait))

        print("Process ", i, " arrived at ", inter_arrival_time[i])
        print("Process ", i, " get service at ", inter_arrival_time[i] + wait_time[i])
        print("Process ", i, " wait time ", wait_time[i])
        time = time + arrival_service_time[inter_arrival_time[i]]
        print("Process ", i, " end at ", time)
        print("\n")

    average_wait = sum(wait_time) / number_of_process
    print("Average Wait time ", average_wait)
    average_sytem_idle = ((time - sum(system_idle_time)) / time) * 100
    print("System utilization ", average_sytem_idle, " %")


MM1(120, 53.33, 17.5)
