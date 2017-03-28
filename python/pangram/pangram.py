def is_pangram(pangram):
    alphabet = []
    def append_alphabet():
        idx = 65
        while idx < 91:
            letter = str(unichr(idx))
            alphabet.append(letter)
            idx += 1
    append_alphabet()
    pangram_list = list(pangram.upper())
    for letter in alphabet:
        if letter not in pangram_list and letter != ' ':
            return False
    return True




print is_pangram("The quick brown fox jumps over the lazy dog")
