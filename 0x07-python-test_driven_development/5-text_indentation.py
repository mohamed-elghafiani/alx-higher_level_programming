#!/usr/bin/python3

"""This module contains the implimentation of the function `text_indentation`

Basic usage:
  text = "How are you doing? I'm fine thanks."
  text_indentation(text)
"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters:
        ., ? and :

    Args:
      text: A string

    Raises:
      TypeError: If text is of type other than string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.replace("? ", "?")
    text = text.replace(": ", ":")
    text = text.replace(". ", ".")
    text = text.replace("?", "?\n\n")
    text = text.replace(".", ".\n\n")
    text = text.replace(":", ":\n\n")

    print(text)
