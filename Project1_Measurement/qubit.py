# Qubit Simulation
###
# Measures the equal amplitude 3 qubit state 100,000 times
# 3 qubits gives a superposition of 8 states: 000 001 010 011 100 101 110 111
#
#
#
#
###
import numpy as np
import stateVector as sV
import measure as measure

debug_flag = 0

np.random.seed(0)
outputShape = 1

hadamard = (1/np.sqrt(2))*np.array([[1, 1],[1, -1]])
identity = np.identity(2)

circuit = np.kron(hadamard, identity)
print(circuit)

numQubits = 2
psi = sV.stateVector(numQubits)
print(psi)
psi = np.matmul(psi, circuit)
print(psi)

measuredStates = measure.measure(psi, basis = 'computational', numMeasurements = 10000)

print(measuredStates)
print("Normalised Measured States")
print(measuredStates/(np.sum(measuredStates)))