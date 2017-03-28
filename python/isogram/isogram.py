def is_isogram(word):
    letter_list = []
    for letter in word:
        if letter not in letter_list:
            letter_list.append(letter)
        elif letter in letter_list:
            return False
    return True

is_isogram("isogram")
is_isogram("nonisogram")
