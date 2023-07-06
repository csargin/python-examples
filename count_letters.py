def count_char_x(word,l=""):
    letter_dict = {}

    for letter in word:
        if letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1
    if l == "":
        return len(letter_dict)
    else:
        return (letter_dict[l])


print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1
print(count_char_x("mississippi"))
# should print 4
