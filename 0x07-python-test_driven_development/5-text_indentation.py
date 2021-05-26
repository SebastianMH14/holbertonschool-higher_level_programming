#!/usr/bin/python3
"""function that prints a text with 2
new lines after each of these characters:
., ? and :"""


def text_indentation(text):
    """text must be a string, otherwise
    raise a TypeError exception with the
    message text must be a string"""
    if type(text) != str:
        raise TypeError("text must be a string")

    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')

    identent_text = "\n".join(i.strip() for i in text.split('\n'))

    print(identent_text, end="")
