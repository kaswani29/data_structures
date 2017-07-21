from collections import Counter

def anagram_checker(string):

    char_hash = {}

    for char in string:

        if char in char_hash:
            char_hash[char] +=1
        else:
            char_hash[char] = 1

    odd_counter = 0
    length_count = len(string)%2

    for value in char_hash.values():
        if value%2 ==1:
            odd_counter +=1
    if odd_counter == length_count:
        return True
    return False

anagram_checker('ivcic')
