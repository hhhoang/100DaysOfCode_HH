# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python
# Given a string of words, you need to find the highest scoring word.
# Each letter of a word scores points according to it's position in the alphabet: a = 1, b = 2, c = 3 etc.
# You need to return the highest scoring word as a string.
# If two words score the same, return the word that appears earliest in the original string.
# All letters will be lowercase and all inputs will be valid.

import string

def high(x):
    alphabet = list(string.ascii_lowercase)
    highest_value = 0
    highest_letter = ""
    letters = x.split(" ")
    for letter in letters:
        letter_value = 0
        for char in letter:
            if char in alphabet:
                value = alphabet.index(char)+1
                letter_value += value
        if letter_value > highest_value:
            highest_value = letter_value
            highest_letter = letter
    return highest_letter
