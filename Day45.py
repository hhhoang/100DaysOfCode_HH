# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 15:55:34 2022

@author: e37294
"""
# dictionary to capture relationship between characters and morse code
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

# rule/function to convert a message in English to 
def morse_converter(message):
    morse = ''
    for character in message.upper():
        if character != " ":
            morse += MORSE_CODE_DICT[character]
        else:
            morse += " "
    print(f'Morse code for {message} is {morse}')
    return morse

morse_converter('The enemy is behind you')
    
