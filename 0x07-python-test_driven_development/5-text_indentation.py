#!/usr/bin/python3
""" text indentation module """

def remove_spaces(start, end, text):
    while text[start] == " " or text[end] == " ":
        if text[start] == " ":
            start += 1

        if text[end] == " ":
            end -= 1

    return (start, end)
def text_indentation(text):
    """ text indentation function """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    start = 0
    end = 0

    for i, c in enumerate(text):
        if c in ".?:":
            end = i

            start, end = remove_spaces(start, end, text)

            print(text[start:end+1])
            print("")
            start = end + 1
        if i == (len(text) - 1) and c not in ".?:":
            start, end = remove_spaces(start, end, text)
            print(text[start:], end="")
