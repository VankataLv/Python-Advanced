def words_sorting(*key_words):
    dictionary = {}
    total_value_dictionary = 0
    for word in key_words:
        value_word = 0
        for letter in word:
            value_word += ord(letter)
        dictionary[word] = value_word
        total_value_dictionary += value_word

    if total_value_dictionary % 2 == 0:
        dictionary = dict(sorted(dictionary.items(), key=lambda x: x[0]))
    else:
        dictionary = dict(sorted(dictionary.items(), key=lambda x: -x[1]))

    result = ""
    for k,v in dictionary.items():
        result += f"{k} - {v}\n"
    return result

# print(
#     words_sorting(
#         'escape',
#         'charm',
#         'mythology'
#   ))

# print(
#     words_sorting(
#         'escape',
#         'charm',
#         'eye'
#   ))

# print(
#     words_sorting(
#         'cacophony',
#         'accolade'
#   ))