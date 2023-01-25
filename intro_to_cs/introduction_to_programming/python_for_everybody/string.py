x = "string"
y = 'string'
z = "abc"+"def" # = abcdef
w = "123" # a string not an int
v = int(w) # conversion of string to int

# Slicing a string
print(x[0])
print(y[3:])
print(z[2:4])

# Catching length
print(len(z))

# Looping through string
for i in x:
    print(i)

# in operator strings to see whether character is in string
print("s" in x)

# comparing strings alphabetically
print("abc" > "banana") # is abc after banana
print("abc" < "banana") # is abc before banana

# methods
# lowercase

name = "BOB"
name2 = name.lower()
print(name2)

# type checking
print(type(name))

# checking available methods for the variable
print(dir(name))

name.upper() # capitalize
name.lower() # lowercase
name.capitalize() # capitalize
name.find('OB') # finds the index where this substring exists. returns -1 if false
name.replace('OB','AB') # finds all substring and replaces it
name.lstrip() # removes whitespace left of string
name.rstrip() # removes whitespace right of string
name.strip() # removes whitespace left and right of string
name.startswith('B') # returns bool whether string starts with given string/character 