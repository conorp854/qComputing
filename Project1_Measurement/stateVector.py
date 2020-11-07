### StateVector
# Takes in number of qubits
# Normalises
# Only for all superposition state at the moment
import numpy as np

def stateVector(numQubits = 3, debug_flag = 0):
    numStates = 2**numQubits

    normalisation_factor = 1/np.sqrt(numStates)

    return normalisation_factor*np.array(np.ones((numStates,), dtype=complex))


