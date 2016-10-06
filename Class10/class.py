
roster = ["posada", "wendy", "triana"]

import random

def call_three(roster):

    number_list = random.sample(range(1, len(roster)), 3)
    for number in number_list:
        print(roster[number])

call_three(roster)

#modify so you don't have repeating names