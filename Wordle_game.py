###############################################
# Date: 9/27/25
# HW:1
# Name: Omar Ali
###############################################
#
# q2_wordle_game.py
#


def load_solutions(path="wordle-solutions-08MAY2022.txt"):
# load the 2309 solution words
    f = open(path)
    sols = [line.strip() for line in f]
    f.close()
    return sols

def load_dict5(path="large.txt", extra_missing=None):
# load big dictionary and keep 5-letter words
# extend with known missing words from the prompt
    f = open(path)
    all_words = [line.strip() for line in f]
    f.close()
    words5 = [w for w in all_words if len(w)==5]
    if extra_missing:
        words5.extend(extra_missing)
    return words5

MISSING = ['abled', 'admin', 'cyber', 'email', 'inbox', 'nerdy', 'ramen']

def hint(word, the_word):
# print uppercase guess, then x/?/letter as in the assignment
    print(word.upper())
    for i in range(5):
        if word[i] == the_word[i]:
            print(word[i].upper(), end='')
        elif word[i] not in the_word:
            print('x', end='')
        else:
            print('?', end='')
    print()

import random

def pick_solution(solutions):
# choose a random solution (random.sample(...)[0])
    return random.sample(solutions, 1)[0]

def is_valid_guess(w, dict5):
# guess must be 5 letters and in the dictionary
    return len(w)==5 and w.isalpha() and w.lower() in dict5

def play():
# main loop: up to 6 valid tries
# invalid words do not consume a try
# show previous valid guesses each round
# print message on win; reveal word on loss
    solutions = load_solutions()
    dict5 = load_dict5(extra_missing=MISSING)
    the_word = pick_solution(solutions)

    tries = 0
    previous = []
    messages = ["Genius!", "Wonderful!", "Great!", "Smooth!", "Not bad!", "Yay!"]

    while tries < 6:
        if previous:
            print("\nPrevious valid guesses:")
            for g in previous:
                print(g.upper())

        guess = input("\n[{}] Enter a 5-letter word: ".format(tries+1)).strip().lower()
        if not is_valid_guess(guess, dict5):
            print("Invalid word; does not count. Try again.")
            continue

        previous.append(guess)
        hint(guess, the_word)

        if guess == the_word:
            print(messages[tries])
            return
        tries += 1

    print("Try next time. The word was:", the_word.upper())

if __name__ == "__main__":
    play()




# Results Below 
"""
Example run 1:
[1] Enter a 5-letter word: Broke
BROKE
xxxxx

Previous valid guesses:
BROKE

[2] Enter a 5-letter word: heart
HEART
xxAxT

Previous valid guesses:
BROKE
HEART

[3] Enter a 5-letter word: PLANT
PLANT
PLANT
Great!


Example run 2:
[1] Enter a 5-letter word: robot
ROBOT
?xBxx

Previous valid guesses:
ROBOT

[2] Enter a 5-letter word: URBAN
URBAN
x?Bxx

Previous valid guesses:
ROBOT
URBAN

[3] Enter a 5-letter word: FIBER
FIBER
xxBER

Previous valid guesses:
ROBOT
URBAN
FIBER

[4] Enter a 5-letter word: Rober
Invalid word; does not count. Try again.

Previous valid guesses:
ROBOT
URBAN
FIBER

[4] Enter a 5-letter word: Ember
EMBER
?xBER

Previous valid guesses:
ROBOT
URBAN
FIBER
EMBER

[5] Enter a 5-letter word: CYBER
CYBER
CYBER
Not bad!
"""

