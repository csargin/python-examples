def unique_english_letters(word):
    letter_dict = {}

    for letter in word:
        if letter not in letter_dict.keys():
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1
    return letter_dict


print(unique_english_letters("mississippi"))
