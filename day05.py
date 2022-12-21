# crates are moved one at a time
# get a pushing and a popping

# define regex to pull every one or two digit number out of the line
import re
move_regex = re.compile('\d{1,2}')
 
def main():
    """ Advent of code day 5 """

    # set up the data
    containers = [[] for i in range(9)]          # Instance Variable
    moves = []

    # read everything and split into containers and moves
    with open('day05_data.txt', encoding='UTF-8') as file:
        for line in file:
            # container splitter
            if line[0:4] == 'move':
                # move splitter
                moves.append(move_regex.findall(line))
            else:
                # print("open:", containers)
                for base in range(0, 9):
                    left = base * 4
                    right = left + 3
                    char = line[left+1:right-1] 
                    if char != ' ':
                        containers[base].append(char)

    # apply the moves to the containers
    for move in moves:
        amt = int(move[0])
        start = int(move[1]) - 1
        end = int(move[2]) - 1
        cargo = containers[start][:amt]
        # following line toggles the difference between 
        # exercises one and two.
        # cargo.reverse()
        containers[end][0:0] = cargo
        del containers[start][:amt]
    # print(f'CONTAINERS: {containers}')

    # print it
    outstr = ''
    for item in containers:
        outstr += item[0]

    print(outstr)

main()
