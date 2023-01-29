import re

handle = open("regex_actual_data.txt")

arrays = list()
sum = 0

for line in handle:
    numList = re.findall('[0-9]+',line)
    for num in numList:
        arrays.append(num)


for i in arrays:
    sum+=int(i)

print(sum)