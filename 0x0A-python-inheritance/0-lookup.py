#!/usr/bin/python3
"Lookup function definition module"


def lookup(obj):
    """Return a list of obj's methods and attributes"""
    return dir(obj)
