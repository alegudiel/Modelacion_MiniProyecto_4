from cmath import inf
import random
import math
# multiples servidores

# Time of arrival of the next request
def funcExp(lamVal):
    return  - float((1/lamVal)*math.log(random.random()))

def services(cantServers):
    valueLambda = 100
    lambdaArriving = 100 # 6000 requests per hour
    T = 3600 # Simulation Time
    t = 0 # Initial time
    Na = 0 # Number of arrivals
    Ta = funcExp(lambdaArriving) # Time of arrival
    Td = [0]*cantServers # Time of departure
    A = [] # Arrival
    D = []  #Departure
    S = [] # Servers

    # solicitudes que llegan y son atendidas por los servidores
    serverProcessing = [0]*cantServers
    requestsDone = [0]*(cantServers+1)

    while t < T or requestsDone[0] > 0:           
        minTime = min(Td)
        minOuts = Td.index(minTime)           
        
        if Ta < Td[minOuts] and Ta< T:   
            t = Ta                     
            Na += 1               
            Ta = Ta + funcExp(lambdaArriving)
            A.append(t)                   
            
            if requestsDone[0] == 0:            
                S.append(t)             
                requestsDone[0] += 1             
                requestsDone[1] = Na             
                Td[0] = t + funcExp(valueLambda)  
            
            # si hay servidores libres se asigna a uno de ellos la solicitud
            elif(requestsDone[0] < cantServers):
                serverAvailable = requestsDone.index(0) - 1
                requestsDone[0] += 1
                requestsDone[serverAvailable+1] = Na
                Td[serverAvailable] = t + funcExp(valueLambda)
                S.append(t)
            
            # si no tenemos servidores libres, se agrega a la cola
            else:                       
                requestsDone[0] += 1           
            
        else:                           
            t = Td[minOuts]              
            serverProcessing[minOuts] += 1             
            D.append(t)                 
            
            # si hay solicitudes en la cola, se asigna a un servidor
            # tenemos un tiempo alto pq no conocemos el tiempo de llegada de la siguiente solicitud
            if requestsDone[0] <= cantServers:            
                requestsDone[0] -= 1             
                Td[minOuts] = 100000   
                requestsDone[minOuts + 1] = 0     
            
            # si esta todo ocupado, la cola se mantiene
            else:                       
                requestsDone[0] -= 1
                Td[minOuts] = t + funcExp(valueLambda)
                requestsDone[minOuts+1] = max(requestsDone) + 1
                S.append(t) 
            
    for i in range (len(serverProcessing)):
        print ("\t"+"Server "+str(i+1)+":", serverProcessing[i], "requests.")
    
    total=0
    for j in range(len(A)):
        oper=S[j]-A[j]
        total=total+oper

    aver = total/len(A)
    
    print("Number of requests: ", Na)
    print("Total time: ", sum(Td))
    print ("Last departure: ", D[-1])
    print ("Average time in queue: ", aver)


cantServers = int(input("Ingrese la cantidad de servidores: "))
services(cantServers)