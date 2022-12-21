"""
    Advent of Code -- Day 06
"""

from file_functions import open_file


def main(length):
    """ Main method, does most of the work"""
    data = open_file("day06_data.txt")
    # data_array = data.split('')
    # return data_array
    # print(len(data))

    for index, char in enumerate(data):
        test = data[index:index+length]
        if check_repeater(test):
            print(f'Non-repeating item {test} found at index {index + length}')
            break


def check_repeater(test):
    """ Check to see if a four-group list contains duplicate letters """
    test_list = []
    for item in test:
        # print(f'{item}, {test_list}, {item in test_list}')
        if (item in test_list):
            return False
        else:
            test_list.append(item)

    return True


# length = length of non-repeating string needed
main(14)
# print(main())
