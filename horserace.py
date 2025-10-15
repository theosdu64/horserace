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

type_of_game = {'tierce': 3, 'quarte': 4, 'quinte': 5}


def getKeys(data: dict):
    """
    Retourne les clés du dictionnaire en liste
    
    param data le dictionnaire
    """
    return list(data.keys())


first_condition = lambda x: x not in getKeys(type_of_game)
second_condition = lambda x: (not x.isdigit()) or (int(x) < 12 or int(x) > 20)

message = 'Choisis entre tierce, quarte, quinte : '
message2 = 'Combien de chevaux entre 12 et 20 : '


def user_input(message, condition):
    """
    Genere un input personalisable
    
    param message le message affiché
    param condition la fonction de validation
    """
    first_input = input(message)
    while condition(first_input):
        print("Entrée invalide, réessaie.")
        first_input = input(message)
    return first_input


def generate_horses(horses_number):
    """
    Genere une list de dict de chevaux

    param horses_number le nombre de chevaux
    """
    return [{'cheval': i + 1, 'vitesse': 0, 'distance': 0, 'status': True} for i in range(horses_number)]


def rand():
    """
    Genere un nombre entre 1 et 6
    """
    return random.randint(1, 6)


def position(distance_actuelle, vitesse):
    """
    Retourne la distance mise à jour du cheval

    param distance_actuelle la distance actuelle
    param vitesse la vitesse du cheval
    """
    return distance_actuelle + distance_par_vitesse[vitesse]


def get_speed(current_speed):
    """
    Retourne le gain de vitesse selon le jet de dé
    
    param current_speed la vitesse actuelle
    """
    return vitesse_evolution[current_speed][rand()]


def post_speed(horse, speed_gain):
    """
    Met à jour la vitesse du cheval
    
    param horse le dictionnaire du cheval
    param speed_gain le gain de vitesse
    """
    horse['vitesse'] += speed_gain


def post_distance(horse):
    """
    Met à jour la distance du cheval
    
    param horse le dictionnaire du cheval
    """
    horse['distance'] = position(horse['distance'], horse['vitesse'])


def delete_disqualified(disqualified, horse):
    """
    Supprime les chevaux disqualifiés
    
    param disqualified la liste des indices à supprimer
    param horse la liste des chevaux
    """
    for i in sorted(disqualified, reverse=True):
        del horse[i]


def put_speed_distance(horses):
    """
    Met à jour la vitesse et distance de tous les chevaux
    
    param horses la liste des chevaux
    """
    disqualified = []
    for i, horse in enumerate(horses):
        horse_speed = horse['vitesse']
        speed_gain = get_speed(horse_speed)

        if speed_gain == 'DQ':
            print(f"Cheval {horse['cheval']} est disqualifié")
            disqualified.append(i)
            continue

        post_speed(horse, speed_gain)
        post_distance(horse)

    delete_disqualified(disqualified, horses)


def get_ranking(horses):
    """
    Retourne le classement des chevaux par distance
    
    param horses la liste des chevaux
    """
    return sorted(horses, key=lambda ch: ch['distance'], reverse=True)


def list_horses_happen(ranking):
    """
    Retourne les chevaux ayant franchi la ligne
    
    param ranking le classement des chevaux
    """
    return [ch for ch in ranking if ch['distance'] >= 2400]


def update_horses(horses_happened, final_ranking, horses):
    """
    Met à jour le classement final et retire les chevaux arrivés
    
    param horses_happened les chevaux arrivés
    param final_ranking le classement final
    param horses la liste des chevaux en course
    """
    for ch in horses_happened:
        if ch not in final_ranking:
            final_ranking.append(ch)
            horses.remove(ch)
            print(f"Cheval {ch['cheval']} a franchi la ligne ({ch['distance']}m)")


def display_horse_race_stat(ranking, horses):
    """
    Affiche les statistiques des chevaux en course
    
    param ranking le classement
    param horses la liste des chevaux
    """
    for ch in ranking:
        if ch in horses:
            print(f"Cheval {ch['cheval']} | Vitesse: {ch['vitesse']} | Distance: {ch['distance']}m")


def display_winner(final_ranking, nb_winners):
    """
    Affiche le classement final
    
    param final_ranking le classement final
    param nb_winners le nombre de gagnants à afficher
    """
    print("Résultats finaux")
    for i, ch in enumerate(final_ranking[:nb_winners]):
        print(f"{i + 1}. Cheval {ch['cheval']} - {ch['distance']}m")


def race(horses, selected_user_game):
    """
    Lance la course de chevaux
    
    param horses la liste des chevaux
    param selected_user_game le nombre de gagnants
    """
    final_ranking = []
    for round in range(50):
        print('=' * 60)
        print(f"Tour {round + 1}")
        put_speed_distance(horses)

        ranking = get_ranking(horses)
        horses_happened = list_horses_happen(ranking)
        update_horses(horses_happened, final_ranking, horses)
        display_horse_race_stat(ranking, horses)

        if len(final_ranking) >= selected_user_game:
            print('=' * 60)
            print('COURSE TERMINÉE')
            break

    display_winner(final_ranking, selected_user_game)



if __name__ == '__main__':
    user_type_of_game = user_input(message, first_condition)
    horses_nbr = user_input(message2, second_condition)

    selected_user_game = type_of_game[user_type_of_game]
    horses_nbr = int(horses_nbr)

    horses = generate_horses(horses_nbr)
    race(horses, selected_user_game)