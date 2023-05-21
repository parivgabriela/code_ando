#!/usr/bin/env python3
# -*- coding: utf-8 -*-
topics = ["Programming", "Maths", "Capitals"]
#todo build a der with the relation betbeen the data
print("Welcome to the Quiz!")
print("Select your topic:")
for indice in range(len(topics)):
    print(f"{indice+1}-{topics[indice]}")

input_topic = int(input("Option: "))