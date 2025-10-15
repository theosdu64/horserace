import random

vitesse_evolution = {
    0: {1: 0, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2},
    1: {1: 0, 2: 0, 3: 1, 4: 1, 5: 1, 6: 2},
    2: {1: 0, 2: 0, 3: 1, 4: 1, 5: 1, 6: 2},
    3: {1: -1, 2: 0, 3: 0, 4: 1, 5: 1, 6: 1},
    4: {1: -1, 2: 0, 3: 0, 4: 0, 5: 1, 6: 1},
    5: {1: -2, 2: -1, 3: 0, 4: 0, 5: 0, 6: 1},
    6: {1: -2, 2: -1, 3: 0, 4: 0, 5: 0, 6: "DQ"}
}

distance_par_vitesse = {
    0: 0,
    1: 23,
    2: 46,
    3: 69,
    4: 92,
    5: 115,
    6: 138
}

def user_input(message, condition):
    first_input = input(message)
    while condition(first_input):
        print("Entrée invalide, réessaie.")
        first_input = input(message)
    return first_input