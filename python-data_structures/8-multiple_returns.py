#!/usr/bin/python3
def multiple_returns(sentence):
    firtC = sentence[0] if len(sentence) > 0 else None
    i = len(sentence)
    return i, firtC
