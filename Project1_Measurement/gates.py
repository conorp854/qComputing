###
# 1 qubit gates
# All 2x2 matrices
#

import numpy as np

test = 5

def hadamard():
    return (1/np.sqrt(2))*np.array([[1, 1],[1, -1]])

def identity():
    return np.identity(2)

def pauliX():
    return np.array([[0, 1],[1, 0]])

def pauliY():
    return np.array([[0 -1*1j], [1j, 0]])

def pauliZ():
    return np.array([[1, 0], [0, -1]])

def cnot(control = 0, target = 1, numQubits = 2):

    zero_projector = np.array([[1, 0], [0, 0]])
    one_projector  = np.array([[0, 0], [0, 1]])

    cnot_zero = None
    cnot_one  = None

    for index in range(numQubits):

        if(index == target):
            if(cnot_zero is None and cnot_one is None):
                cnot_zero = identity()
                cnot_one = pauliX()
            else:
                cnot_zero = np.kron(cnot_zero, identity())
                cnot_one = np.kron(cnot_one, pauliX())

        elif(index == control):
            if(cnot_zero is None and cnot_one is None):
                cnot_zero = zero_projector
                cnot_one = one_projector
            else:
                cnot_zero = np.kron(cnot_zero, zero_projector)
                cnot_one = np.kron(cnot_one, one_projector)
                
        else:
            if(cnot_zero is None and cnot_one is None):
                cnot_zero = identity()
                cnot_one  = identity()
            else:
                cnot_zero = np.kron(cnot_zero, identity())
                cnot_one  = np.kron(cnot_one, identity())

    return cnot_zero + cnot_one

def circuitSlice(gateArray):
    qSlice = gateArray[0]

    for gate in gateArray[1::]:
        qSlice = np.kron(qSlice, gate)

    return qSlice

def runCircuit(stateVector, sliceArray):
    finalState = stateVector

    for circuitSlice in sliceArray:
        finalState = np.matmul(finalState, circuitSlice)

    return finalState
