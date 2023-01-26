# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

dict = {}

for line in handle:
    if 'From ' in line:
        split = line.split()
        time = split[5]
        timeSplit = time.split(':')
        hour = timeSplit[0]
        dict[hour] = dict.get(hour,0)+1

dictTuple = dict.items()
dictSort = sorted(dictTuple)
for i,e in dictSort:
    print(i,e)
#print(sorted([i,e] for i,e in dictTuple))
#for i,e in dictTuple:
#    print(i,e)