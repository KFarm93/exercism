def word_count(phrase):
    word_list = phrase.split()
    phrase_dict = {}
    for word in word_list:
        if word in phrase_dict:
            phrase_dict[word] += 1
        else:
            phrase_dict[word] = 1
    return phrase_dict


word_count('olly olly in come free')
