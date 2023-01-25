x = [1,2,3]
y = ["a","b","c"]
print(x[0])
print(x)
x[0] = 5
print(x)

# Ranging Over
for i in range(len(y)):
    print(i)
# 0,1,2

for i in x:
    print(i)

# Concatenate
z = x + y
print(z)

# Slicing
print(x[0:1])

# Creating a list
a = []
# or 
b = list()

# Appending
a.append(5)

# Logics
print(5 in a)
print(5 not in a)

# Sort
test = [3,5,1]
test.sort()
print(test)

# methods
print(len(test))
print(max(test))
print(min(test))
print(sum(test))

# Splitting string into list using whitespace as delimiter
text = "TE TE TE"
textSplit = text.split()
print(textSplit)

text2 = "TELTELTE"
textSplit2 = text2.split()
print(textSplit2)
textSplit2 = text2.split('L')
print(textSplit2)
