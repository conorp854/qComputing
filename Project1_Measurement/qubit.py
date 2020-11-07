# Qubit Simulation
###
# Choose number of qubits
# Create an equal superposition stateVector
# Create circuit slices and put into circuit array
# Run circuit on stateVector
# Perform N measurements
###
import numpy as np
import stateVector as sV
import measure as measure
import gates as gates

debug_flag = 0

np.random.seed(0)
outputShape = 1

numQubits = 3
psi = sV.stateVector(numQubits)

print(gates.cnot(1, 0, 2))

circuit = []
circuit.append(gates.circuitSlice([gates.hadamard(), gates.hadamard(), gates.hadamard()]))
circuit.append(gates.circuitSlice([gates.pauliX(), gates.identity(), gates.identity()]))
circuit.append(gates.cnot(0, 2, numQubits))

finalPsi = gates.runCircuit(psi, circuit)
print(finalPsi)
#measuredStates = measure.measure(finalPsi, basis = 'computational', numMeasurements = 10000)
#
#print(measuredStates)
#print("Normalised Measured States")
#print(measuredStates/(np.sum(measuredStates)))