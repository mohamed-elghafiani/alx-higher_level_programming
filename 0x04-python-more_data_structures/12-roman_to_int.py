#!/usr/bin/python3

romans = {
    "I": 1, "II": 2, "III": 3, "V": 5, "IV": 4, "VI": 6, "VII": 7,
    "VIII": 8, "X": 10, "IX": 9, "XX": 20, "XXX": 30, "L": 50, "XL": 40,
    "LX": 60, "LXX": 70, "LXXX": 80, "C": 100, "XC": 90, "CC": 200,
    "CCC": 300, "D": 500, "CD": 400, "DC": 600, "DCC": 700, "DCCC": 800,
    "M": 1000, "CM": 900, "MM": 2000, "MMM": 3000
}


def roman_to_int(roman_string):
    roman_int = 0
    if not roman_string:
        return roman_int

    for key in reversed(romans.keys()):
        if key in roman_string:
            roman_int += romans[key]
            roman_string = roman_string.replace(key, "")

    return roman_int
