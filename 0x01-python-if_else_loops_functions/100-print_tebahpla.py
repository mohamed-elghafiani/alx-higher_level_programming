#!/usr/bin/python3

lz_ascii = 122
uz_ascii = 90

for i in range(26):
    if i == 0:
        print("{}".format(chr(lz_ascii - i)), end="")
    elif i % 2 == 0:
        print("{}".format(chr(lz_ascii - i)), end="")
    else:
        print("{}".format(chr(uz_ascii - i)), end="")
