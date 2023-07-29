import random
from random import randrange

def read_file(path_file):
    with open(path_file) as fl:
        list_file = fl.readlines()
    return list_file

def select_random_element_list(a_list):
    element = random.choice(a_list)
    print(f"elemento elegido {element}")

def select_random_number(max):
    #
    rand_number = randrange(max)
    return rand_number

def select_n_winners_from(n, max):
    list_winners = []
    for element in range(n):
        number = select_random_number(max)
        if not number is list_winners:
            list_winners.append(number)
    return list_winners

def select_random_from_list():
    #overwriten path
    path = 'names.csv'
    list_file = read_file(path)
    list_numbers = select_n_winners_from(3,len(list_file))
    winner_1 = list_file[list_numbers[0]]
    winner_2 = list_file[list_numbers[1]]
    winner_3 = list_file[list_numbers[2]]

    print(f"Winners\n\nFirst Place: {winner_1}\nSecond Place: {winner_2}\nThrid Place: {winner_3}")


select_random_from_list()