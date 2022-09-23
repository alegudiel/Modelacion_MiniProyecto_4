from cmath import inf
import random
import math

# Values of each provider, in seconds
prov1 = { "lambdaArriving": 40, "lambdaProcesing": 100 }
prov2 = { "lambdaArriving": 40, "lambdaProcesing": 10 }


T = 0 # Simulation Time
Na = 0 # Number of arrivals
Nd = 0 # Number of departures
N = 0 # Number of requests on time T
Ta = 0 # Time of arrival
Td = 0 # Time of departure
noServers = 1 # Number of servers

# Times of arrival and departure on i
A = []
D = []

# Time of arrival of the next request
def funcExp(lamVal):
    return -float((1/lamVal)*math.log(random.random()))

t0 = random.random()
Ta = t0
Td = 0
t = 0
while t < 3600:
    u = random.random()
    T = T - (1/3600)*math.log(u)
    
    print("valor ta", Ta, Td, N, T)

    # Case 1: Arrival when it's not closed
    if (Ta <= Td and Ta <= T):
        # Request arrived, Time is running
        t = Ta
        Na += 1
        N += 1
        t_t = Ta - (1/3600) * math.log(random.random())
        Ta = t_t
        if (N == 1):
            print("Arrived")
            Td = t + funcExp(3600)
        
        A.append(Ta)
        
    if (Td < Ta and Td <= T):
        # Request finished, Time is running
        t = Td
        N -= 1
        Nd += 1
        if (N == 0):
            print("We don't know")
            Td = inf
        else:
            Td = t + funcExp(3600)

        D.append(Td)

    if (min(Ta, Td) > T and N > 0):
        # Request arrived but has to wait
        t = Td
        N -= 1
        Nd += 1
        
        if(N > 0):
            Td = t + funcExp(3600)

        else:
            D.append(Td)

        
    if (min(Ta, Td) > T , N == 0):
        # Request arrived after time, no request ton queue
        Tp = max(t - T, 0)
        # print("Termino " , len(D))
        # print("Termino " , len(A))
        # break

