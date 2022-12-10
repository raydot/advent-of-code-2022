mystr = ''
myarr = []

def splitString(string):
    length = len(string)
    left = string[0:length // 2]
    right = string[length // 2:length]
    return[left, right]

def findDupe(lists):
    for  item in lists[0]:
        if item in lists[1]:
            return item

def returnValue(item):
    itemval = ord(item)
    if itemval >= 97 and itemval <= 122: # lower case
        return itemval - 96
    else: # upper case
        return itemval - 38


with open('day03_data.txt') as file:
     for line in file:
       mystr += line

myarr = mystr.split('\n')

score = 0

for item in myarr:
    score += returnValue(findDupe(splitString(item)))

print(score)

"""
print(myarr[2])
print(len(myarr[2]))
print(splitString(myarr[2]))
print(findDupe(splitString(myarr[2])))
print(returnValue(findDupe(splitString(myarr[2]))))
"""

# PART 2

# myarr[] is still good from the last exercise

index = 0
grouping = 0
holder = []
final = []

for item in myarr:
    # print(item)
    holder.append(item)
    index += 1
    if index % 3 == 0:
        # grouping += 1
        # print ('\n')
        # print(holder)
        final.append(holder)
        holder = []

score = 0
print("initial score:", score)
total = 0

for item in final:
    print(item)
    total += 1
    for char in item[0]:
        if ((char in item[1]) and (char in item[2])):
            score += returnValue(char)
            print(item, char, returnValue(char), score)
            break

print(score, total)
# rint(final[0])