"""
    Any file handling functions needed for the advent-of-code
"""


def open_file(filename):
    """
        Open file and return contents as string
    """
    mystr = ''
    with open(filename) as file:
        for line in file:
            mystr += line

    return mystr
