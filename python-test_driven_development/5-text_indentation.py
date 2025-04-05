#!/usr/bin/python3

def text_indentation(text):
    """This function prints a text with 2 new lines after each of these characters: '.', '?', and ':'.
    An error message is displayed if text is not a string."""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    i = 0

    while i < len(text):
        result += text[i]
        if text[i] in ".?:":
            result += "\n\n"
            i += 1
            # Skip any spaces after the punctuation
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
    print(result, end="")
