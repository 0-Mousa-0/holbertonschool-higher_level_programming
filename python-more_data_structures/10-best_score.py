#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        key = None
        best = None

        for i in a_dictionary:
            if best is None or a_dictionary[i] > best:
                best = a_dictionary[i]
                key = i
        return key
