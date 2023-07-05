#!/usr/bin/python3

""" This Module contains the definition of the function say_my_name """


def say_my_name(first_name, last_name=""):
    """ say_my_name prints "My name is <first_name> <last_name>

    Args:
      fist_name: A string representing the firt name
      last_name: A string representing the last name

    Raises:
      TypeError: If either first_name or last_name is not a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
