#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence:
        ln = len(sentence)
        if ln == 0:
            return ln, None
        return ln, sentence[0]
