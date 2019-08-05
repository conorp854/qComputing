###
#
#
#
#
#

import numpy as np

def measure(stateVector = [1], basis = 'computational', numMeasurements = 1, debug_flag = 0):

    measurements = np.zeros((len(stateVector)))
    outputShape = 1

    for _ in range(numMeasurements):
        probability_of_state = 0
        r = np.random.uniform(0,1,size=outputShape)
        for index in range(stateVector.size):
            if debug_flag: print("Current State: " + str(bin(index)))

            probability_of_state = probability_of_state + np.abs(stateVector[index])**2

            if debug_flag: print("Probability Of State: " + str(probability_of_state))
            if r < probability_of_state:
                if debug_flag: print("Measured State: " + str(bin(index)))
                measurements[index] = measurements[index] + 1
                break
            if debug_flag: print()


    return measurements