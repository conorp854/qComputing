# Qubit Simulation
import numpy as np

debug_flag = 0

np.random.seed(0)
outputShape = 1

normalisation_factor = 1/np.sqrt(8)
psi = normalisation_factor*np.array([1,1,1,1,1,1,1,1])

measured_states = np.zeros((8))
for repeat in range(100000):
    probability_of_state = 0
    r = np.random.uniform(0,1,size=outputShape)
    for index in range(psi.size):
        if debug_flag: print("Current State: " + str(bin(index)))

        probability_of_state = probability_of_state + np.abs(psi[index])**2

        if debug_flag: print("Probability Of State: " + str(probability_of_state))
        if r < probability_of_state:
            if debug_flag: print("Measured State: " + str(bin(index)))
            measured_states[index] = measured_states[index] + 1
            break
        if debug_flag: print()

print()
print("Normalised Measured States")
print(measured_states/(np.sum(measured_states)))