#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    _len = len(sentence)
    Fcharacter = sentence[0]
    return ((_len), (Fcharacter))
