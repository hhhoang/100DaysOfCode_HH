# Everyone knows passphrases. One can choose passphrases from poems, songs, movies names and so on but frequently they can be guessed due to common cultural references. You can get your passphrases stronger by different means. One is the following:
# 1) choose a text in capital letters including or not digits and non alphabetic characters,
# 2) shift each letter by a given number but the transformed letter must be a letter (circular shift),
# 3) replace each digit by its complement to 9,
# 4) keep such as non alphabetic and non digit characters,
# 5)downcase each letter in odd position, upcase each letter in even position (the first character is in position 0),
# 6) reverse the whole result.
# https://www.codewars.com/kata/559536379512a64472000053/train/python

import string

def play_pass(s, n):
    alphabet = list(string.ascii_uppercase)
    number = list(map(str, list(range(10))))
    s_list = ''.join(str(e).upper() for e in list(s))
    new_list = []
    index = 0
    for i in s_list:
        if i in alphabet:
            b = alphabet.index(i) + n
            new_char = alphabet[b % 26]
            if index % 2 == 0:
                new_char = new_char.upper()
            else:
                new_char = new_char.lower()
        elif i in number:
            new_char = str(9 - int(i))
        else:
            # special character
            new_char = i
			
        new_list.insert(0, new_char)
        index += 1
		
    print(new_list)
    result_string = ''.join(str(i) for i in new_list)
    return result_string

print("Actual:   " + play_pass("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2))
print("Expected: 4897 NkTrC Hq fT67 GjV Pq aP OqTh gOcE CoPcTi aO")
