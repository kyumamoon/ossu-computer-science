xx = open('test.txt','r') # read mode to read data
# x = open('test.txt','w') // writes mode to write data

lines = 0

# Iterating through each line of text file
for i in xx:
    lines+=1
    print(i)
print(lines)

wholeRead = xx.read()
print(len(wholeRead))
print(wholeRead,"WHOLEREAD")


# Quitting with try and except.
try:
    reads = open('test.txt')
except:
    print("ERROR")
    quit()

print(reads.read())