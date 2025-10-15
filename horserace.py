import random

first_condition = lambda x: x not in getKeys(type_of_game)
second_condition = lambda x : (not x.isdigit()) or (int(x) < 12 or int(x) > 20)
message = 'Choisis entre tierce, quarte, quinte : '
message2 = 'Combien de chevaux entre 12 et 20'

vitesse_evolution = {
    0: {1: 0, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2},
    1: {1: 0, 2: 0, 3: 1, 4: 1, 5: 1, 6: 2},
    2: {1: 0, 2: 0, 3: 1, 4: 1, 5: 1, 6: 2},
    3: {1: -1, 2: 0, 3: 0, 4: 1, 5: 1, 6: 1},
    4: {1: -1, 2: 0, 3: 0, 4: 0, 5: 1, 6: 1},
    5: {1: -2, 2: -1, 3: 0, 4: 0, 5: 0, 6: 1},
    6: {1: -2, 2: -1, 3: 0, 4: 0, 5: 0, 6: "DQ"}
}

type_of_game = {'tierce': 3, 'quarte': 4, 'quinte': 5}

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

def getKeys(data: dict):
    return list(data.keys())

def position(vitesse, distance_actuelle):
    return distance_actuelle + distance_par_vitesse[vitesse]

def post_speed(horse,get_speed):
    horse['vitesse'] += get_speed

def post_distance(horse):
    horse['distance'] = position(horse['vitesse'], horse['diistance'])


def delete_disqualified(disqualified,array):
    for i in sorted(disqualified, reverse=True):
        del array[i]

def put_speed_distance(horses):
    disqualified = []
    for i, horse in enumerate(horses):
        horse_speed = horses['vitesse']
        get_speed = get_speed(horse_speed)

        if get_speed == 'DQ':
            print(f'le cheval : {horse['cheval']} est disqualifié')
            disqualified.append(i)
            continue
        post_speed()
        post_distance()
    delete_disqualified(disqualified,horses)

def generate_horses(horses_number):
    return [{'cheval': i + 1, 'vitesse': 0, 'distance': 0, 'status' : True} for i in range(horses_number)]

def get_ranking(horses):
    return sorted(horses, key=lambda ch: ch['distance'], reverse=True)

def list_horses_happen(ranking):
    horses_dict = [ch for ch in ranking if ch['distance'] >= 2400]
    return horses_dict

def update_horses(horse_happened, final_horse_ranking,horses):
    for ch in horse_happened:
        if ch not in final_horse_ranking:
            final_horse_ranking.append(ch)
            horses.remove(ch)
            print(f"Cheval {ch['cheval']} a franchi la ligne , ({ch['distance']}m)")

def display_horse_race_stat(ranking, horses):
    for ch in ranking:
        if ch in horses:
            print(f"Cheval {ch['cheval']} | Vitesse: {ch['vitesse']} | Distance: {ch['distance']}m")

def race(horses,selected_user_game, horse_number):
    final_horse_ranking = []
    for round in range(50):
        print('=' * 60)
        print(f"Tour {round + 1}")
        put_speed_distance(generate_horses(horse_number))

        ranking = get_ranking(horses)
        horses_happened = list_horses_happen(ranking)

        update_horses(horses_happened, final_horse_ranking, horses)
        display_horse_race_stat(ranking, horses)

        if len(final_horse_ranking) >= selected_user_game:
            print('=' * 60)
            print('COURSE TERMINÉE !')
            break

user_type_of_game = user_input(message, first_condition)
horses_nbr = user_input(message2, second_condition)