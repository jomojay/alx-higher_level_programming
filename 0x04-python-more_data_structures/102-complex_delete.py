#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        de_l = []
        for k, v in a_dictionary.items():
            if v == value:
                de_l.append(k)
        for i in range(len(de_l)):
            del a_dictionary[de_l[i]]
    return a_dictionary
