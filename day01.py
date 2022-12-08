
i = 0
counter = 0
mystr = ''
myarr = []
totarr = []

with open('my_data.txt') as file:
     for line in file:
        #if line == '\n': 
        #   i += 1
         #print(line)
        mystr += line

myarr = mystr.splitlines()

# print(myarr)

for item in myarr:
    if item == '':
        totarr.append(counter)
        counter = 0
    else:
        counter += int(item)

print(max(totarr))

totarr.sort(reverse=True)

print(totarr[0] + totarr[1] + totarr[2])