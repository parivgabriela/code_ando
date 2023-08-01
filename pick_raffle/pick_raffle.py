import random
from random import randrange
from validators import validate_number


def len_file(path):
    """return the len of a file this don't useses all memory
    read line by line and count it

    Args:
        path (str): given a path to read the file

    Returns:
        int: return the len of the given file
    """
    lines = 0
    with open(path) as f:
        for line in f:
            #count line by line to work with large files
            lines = lines +1
    return lines

def select_winners_from_file(filename, cant_winners):
    """from a file and the numbers or winners this return the names of winners in a list

    Args:
        filename (str): path to the file of the names
        cant_winners (int): number of winners

    Returns:
        list: return in order the winners
    """
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
    """given a max return the random number

    Args:
        max (int): max number of the random

    Returns:
        int: random number
    """
    rand_number = randrange(max)
    return rand_number

def select_n_winners_from(n, max):
    """given a cant of numbers and the max of a number return a list with the winner positions

    Args:
        n (int): cant of winners
        max (int): max of a number

    Returns:
        list: list of the winner numbers
    """
    list_winners = []
    index = 0
    while len(list_winners) != n:
        number = select_random_number(max)
        if not number in list_winners:
            index = index + 1
            list_winners.append(number)
    return list_winners

def select_random_from_list(list_file, cant_winners):
    """return list of winner in a file

    Args:
        list_file (list): list with the participants
        cant_winners (int): cant of winners

    Returns:
        list: list of names winners
    """
    list_winners = []
    list_numbers = select_n_winners_from(cant_winners,len(list_file))
    for winner in range(cant_winners):
        list_winners.append(list_file[list_numbers[winner]])

    return list_winners


def main_random_file():
    # main program to test in terminal
    filename = input("Enter filename: ") #"names.csv"
    cant_winners = validate_number("Cant of winners: ", len_file(filename))
    list_winners = select_winners_from_file(filename, cant_winners)
    print("Winners\n")
    for index, winner in enumerate(list_winners, start=1):
        print(f"{index} Place: {winner}\n")

#main_random_file()