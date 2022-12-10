# should probably find a way to put this in a separate
# file and import.  

mystr = ''

with open('day04_data.txt') as file:
     for line in file:
       mystr += line

# print(mystr)

# split into array
mylist = mystr.split('\n')

# split the splits into two-pair integer arrays
myarr = []
for item in mylist:
  holder = item.split(',')
  holderLeft = holder[0].split('-')
  holderRight = holder[1].split('-')
  myarr.append([[int(holderLeft[0]), int(holderLeft[1])],[int(holderRight[0]), int (holderRight[1])] ])

print(myarr[2])
print(myarr[2][0][0], myarr[2][1][0], myarr[2][0][1], myarr[2][1][1])


# use that list to figure out if pairs contain one another

count = 0
# part 1 solution: 536

for item in myarr:
  # 4-6 6-6
  # 6-6 4-6
  # print(item[0][0], item[0][1], item[1][0], item[1][1])
  if ((item[0][0] <= item[1][0]) and (item[0][1] >= item[1][1])) or ((item[0][0] >= item[1][0]) and (item[0][1] <= item[1][1]) ):
      count += 1

print("Part #1 count:", count)

count = 0
# 2-5 # 1-3   

# part 2 solution: 
for item in myarr:
  # print(item[0][0], item[0][1], item[1][0], item[1][1])
  if (((item[0][0] <= item[1][0]) and (item[0][1] >= item[1][1])) or ((item[0][0] >= item[1][0]) and (item[0][1] <= item[1][1])) or (((item[0][0] <= item[1][0]) and (item[0][1] >= item[1][0])) or ((item[0][0] <= item[1][1]) and (item[0][1] >= item[1][1])))or (((item[1][0] <= item[0][0]) and (item[1][1] >= item [0][0])) or ((item[1][0] <= item[0][1]) and (item[1][1] >= item[0][1])))):
      count += 1

print("Part #2 count:", count)

