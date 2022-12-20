# crates are moved one at a time
# get a pushing and a popping

# regex time!
import re

# pull every one or two digit number out of the line
moveregex = re.compile('\d{1,2}')

# class line_machine:
#     """ class docstring """

    # def __init__(self):
    #     self.containers = [[] for i in range(9)]          # Instance Variable
    #     self.moves = []


    # def lineSplitter(self, line):
    #     """convert initial container state into lists"""
    #     for base in range(0, 9):
    #         left = base * 4
    #         right = left + 3
    #         char = line[left+1:right-1]
    #         if char == ' ':
    #             continue
    #         else:    
    #             self.containers[base].append(char)
    #         # print(containers)

    # def make_move(self, amt, start, end):
    #     """move the containers around"""
    #     cargo = []
    #     start -= 1
    #     end -= 1
    #     for x in range(amt):
    #         # print(amt)
    #     #for amt in range:
    #         cargo = self.containers[start][:amt]
    #         cargo = cargo.reverse()
    #         self.containers[end].insert(0, cargo)
    #         del self.containers[start][:amt]

    # def move_maker(self):
    #     """ make all of the moves """
    #     local_containers = self.containers.copy()
    #     # print(f'Containers: {self.containers}')
        # print(f'local_containers: {local_containers}')
        # print(f'self.moves = {self.moves}')
        # print(f'type: {type(local_containers)}')
        
        # for move in self.moves:
        #     amt = int(move[0])
        #     start = int(move[1]) - 1
        #     end = int(move[2]) - 1
        #     for x in range(amt):
        #         cargo = local_containers[start][:amt]
        #         cargo = cargo.reverse()
        #         local_containers[end].insert(0, cargo)
        #         del local_containers[start][:amt]

        # return local_containers
    
def main():
    """ Ties it all together """


    containers = [[] for i in range(9)]          # Instance Variable
    moves = []

    with open('day05_data.txt') as file:
        for line in file:
            # container splitter
            if line[0:4] == 'move':
                # move splitter
                moves.append(moveregex.findall(line))
            else:
                # print("open:", containers)
                for base in range(0, 9):
                    left = base * 4
                    right = left + 3
                    char = line[left+1:right-1] 
                    if char != ' ':
                        containers[base].append(char)

    for move in moves:
        amt = int(move[0])
        start = int(move[1]) - 1
        end = int(move[2]) - 1
        for x in range(amt):
            cargo = containers[start][:amt]
            cargo = cargo.reverse()
            containers[end].insert(0, cargo)
            del containers[start][:amt]
    # print(f'MOVES: {moves}')
    print(f'CONTAINERS: {containers}')
    # self.moveMaker()      

    # print(f'{self.move_maker()}')
    # print(self.containers)
    #  return self.containers



main()
