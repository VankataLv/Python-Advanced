#Judge 66/100
from collections import deque


def check_word(vowel: str, consonant: str, words_left: dict) -> dict:
    global found_word
    for key in words_left.keys():
        if vowel in key:
            words_left[key] -= 1
            if words_left[key] == 0:
                found_word = key
                break
        if consonant in key:
            words_left[key] -= 1
            if words_left[key] == 0:
                found_word = key
                break
    return words_left


vowels = deque(list(input().split()))
consonants = list(input().split())
words_to_search = {"rose": 4, "tulip": 5, "lotus": 5, "daffodil": 8}
found_word = ""

while len(found_word) == 0 and vowels and consonants:
    words_to_search = check_word(vowels.popleft(), consonants.pop(), words_to_search)

if found_word:
    print(f"Word found: {found_word}")
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
