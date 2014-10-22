#!/usr/bin/env python3
#
# Implementation of programming activity 1 (http://liris.cnrs.fr/ideal/mooc/lesson.php?n=013) 

# Number of time steps to perform the experiment for
N_CYCLES = 11

def pickOtherExperiment(currentExperiemnt):
    for e in ['e1', 'e2']:
        if e != currentExperiemnt:
            return e

# anticipate experiment result based on stored interactions, might return None
def anticipate(experiment):
    return interactions.get(experiment)

# store an interaction tuple (experiment, result)
def recordInteraction(experiment, result):
    interactions[experiment] = result

experiment = 'e1'
mood = None
selfSatisfiedDuration = 0

# stored interactions (experiment, result)
interactions = {}

for cycle in range(N_CYCLES):
    if mood == 'BORED':
        selfSatisfiedDuration = 0
        experiment = pickOtherExperiment(experiment)

    anticipatedResult = anticipate(experiment)

    # environment
    if experiment == 'e1':
        result = 'r1'
    else:
        result = 'r2'

    recordInteraction(experiment, result)

    if result == anticipatedResult:
        mood = 'SELF-SATISFIED'
        selfSatisfiedDuration += 1
    else:
        mood = 'FRUSTRATED'
        selfSatisfiedDuration = 0

    if selfSatisfiedDuration > 3:
        mood = 'BORED'

    print(cycle, experiment, result, mood)
