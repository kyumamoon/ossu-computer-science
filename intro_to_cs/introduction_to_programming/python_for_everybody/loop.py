
# Looping through 0 to 10
for i in range (10):
    print(i)
    # prints 0 to 9

print("####")

# Looping through an array
a = ["a","b","c","d","e"]

for i in a:
    print(i)

print("####")

# Looping in a while loop with a break statement.
x = 5

while x < 10:
    if x == 8:
        break
    print(x)
    x+=1

print("####")

# Looping in a while loop with a continue statement
y = 6

while y < 10:
    if y == 8:
        continue # stops interation but loops still runs because its always 8 and never processed the code below to go to 9
    print(y)
    y+=1
