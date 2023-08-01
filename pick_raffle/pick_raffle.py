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

def len_file(path):
    lines = 0
    with open(path) as f:
        for line in f:
            #count line by line to work with large files
            lines = lines +1
    return lines

def select_winners_from_file(filename, cant_winners):
    number_winners = select_n_winners_from(cant_winners, len_file(filename)-1)
    winners = []
    data_winner = {}
    with open(filename, 'r') as f:
        #avoid header
        next(f)
        for index, line in enumerate(f):
            if index in number_winners:
                clean_line = line.replace('\n', '')
                data_winner[index] = clean_line
    #save the order
    for number in number_winners:
        winners.append(data_winner[number])

    return winners

def select_random_number(max):
    #
    rand_number = randrange(max)
    return rand_number

def select_n_winners_from(n, max):
    list_winners = []
    index = 0
    while len(list_winners) != n:
        number = select_random_number(max)
        if not number in list_winners:
            index = index + 1
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

def main_random_file():
    filename = input("Enter filename: ") #"names.csv"
    cant_winners = validate_number("Cant of winners: ", len_file(filename))
    list_winners = select_winners_from_file(filename, cant_winners)
    print("Winners\n")
    for index, winner in enumerate(list_winners, start=1):
        print(f"{index} Place: {winner}\n")

#main_random_file()