# crates are moved one at a time
# get a pushing and a popping

# regex time!
import re

# global containers 
# containers = [[] for i in range(9)]

# convert initial container state into lists
def linesplitter(line, containers):
    # global containers
    for base in range(0, 9):
        left = base * 4
        right = left + 3
        char = line[left+1:right-1]
        if char == ' ':
            continue
        else:    
        # print(base, char) 
            # global containers
            containers[base].append(char)
        # print(containers)

def makemove(amt, start, end, containers):
    # global containers
    # print("makemove \n", containers)
    # print(amt, start, end)
    # print(containers[0])
    cargo = []
    start -= 1
    end -= 1
    for x in range(amt):
        cargo = containers[start][:amt]
        cargo = cargo.reverse()
        containers[end].insert(0, cargo)
        del containers[start][:amt]




# pull every one or two digit number out of the line
moveregex = re.compile('\d{1,2}')
# store the moves
moves = []

def main():
    containers = [[] for i in range(9)]

    with open('day05_data.txt') as file:
        for line in file:
            # container splitter
            if line[0:4] != 'move':
                linesplitter(line, containers)
            else:
                # move splitter
                moves.append(moveregex.findall(line))
        # print("open:", containers)
                
    for move in moves:
        # global containers
        # print("makemove", containers[0])
        x = int(move[0])
        y = int(move[1])
        z = int(move[2])
        makemove(x, y, z, containers)

    print(containers)



main()