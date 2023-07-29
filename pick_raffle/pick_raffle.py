import random
from random import randrange
from validators import validate_number

def read_file(path_file):
    with open(path_file) as fl:
        next(fl)
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
        if not number in list_winners:
            list_winners.append(number)
    return list_winners

def select_random_from_list(list_file, cant_winners):
    list_winners = []
    list_numbers = select_n_winners_from(cant_winners,len(list_file))
    for winner in range(cant_winners):
        list_winners.append(list_file[list_numbers[winner]])

    return list_winners

def main_random():
    filename = input("Enter filename: ") #"names.csv"
    list_participants = read_file(filename)
    cant_winners = validate_number("Cant of winners: ", len(list_participants))
    list_winners = select_random_from_list(list_participants, cant_winners)
    print("Winners\n")
    for index, winner in enumerate(list_winners, start=1):
        print(f"{index} Place: {winner}\n")
    #print(f"{} Place: {list_winners[0]}\nSecond Place: {list_winners[1]}\nThrid Place: {winner_3}")

main_random()