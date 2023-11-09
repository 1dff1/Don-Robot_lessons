def compress(sentence):
    position_list = list()
    sentence_list = sentence.lower().split()
    sentence_set_list = list()
    result = str()

    for x in sentence_list:
        if x not in sentence_set_list:
            sentence_set_list.append(x)

    for i in sentence_list:
        position_list.append(sentence_set_list.index(i))

    for el in position_list:
        result += str(el)
    return result


compress("The number 0 is such a strange number Strangely it has zero meaning")
