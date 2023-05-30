#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv

topics = ["Programming", "Maths", "Capitals"]
with open('questions.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(f'categories {row["categories"]}, questions {row["questions"]}')
#todo build a der with the relation betbeen the data
print("Welcome to the Quiz!")
print("Select your topic:")
for indice in range(len(topics)):
    print(f"{indice+1}-{topics[indice]}")

input_topic = int(input("Option: "))