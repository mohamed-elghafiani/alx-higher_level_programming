#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence:
        ln = len(sentence)
        return ln, sentence[0]
    else:
        return 0, None
