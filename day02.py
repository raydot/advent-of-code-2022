

"""
 PART 1:
 The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
 A ROCK         X ROCK
 B PAPER        Y PAPER
 C SCISSORS     Z SCISSORS
"""

def whoWins(line):
    score = 0
    output = line.split(' ')
    result = [output[0], output[1].replace('\n', '')]


    if (result[0] == 'A'):
        match result[1]:
            case "X": 
                score += 4
            case "Y":
                score += 8
            case "Z":
                score += 3

    if (result[0] == 'B'):
        match result[1]:
            case "X": 
                score += 1
            case "Y":
                score += 5
            case "Z":
                score += 9

    if (result[0] == 'C'):
        match result[1]:
            case "X": 
                score += 7
            case "Y":
                score += 2
            case "Z":
                score += 6

    return score

total = 0
lines = 0

with open('day02_data.txt') as file:
     for line in file:
        total += whoWins(line)

print (total)



"""
PART 2:
"Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"
"""

total = 0

def whoWins2(line):
    score = 0
    split = line.split(' ')
    final = [split[0], split[1].replace('\n', '')]


    if (final[0] == 'A'): # rock
        match final[1]:
            case "X": # lose
                score += 3
            case "Y": # draw
                score += 4
            case "Z": # win
                score += 8

    if (final[0] == 'B'): # paper
        match final[1]:
            case "X": 
                score += 1
            case "Y":
                score += 5
            case "Z":
                score += 9

    if (final[0] == 'C'): # scissors
        match final[1]:
            case "X": 
                score += 2
            case "Y":
                score += 6
            case "Z":
                score += 7

    return score

with open('day02_data.txt') as file:
     for line in file:
        total += whoWins2(line)

print (total)