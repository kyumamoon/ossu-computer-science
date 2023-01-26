# Declaring dict
bag = dict()

bag2 = {'key':"value"}

# Adding key and value in dict
bag['key'] = "value"

print(bag)
print(bag['key'])

# Checking if key exists
print('key' in bag)

# Checking key and adding it with default value if it doesnt exist
# get() method
# First parameter of get method is the key to search, second is the default value to add to key if key not found
bag['banana'] = bag.get('banana',0)
print(bag)

# Adding and checking with an addition expression to right of get
bag['banana'] = bag.get('banana',0)+1
print(bag)

# Looping through dictionary
for key in bag:
    print("KEY:",key)
    print("VALUE:",bag[key])

# Getting all values or keys
print(bag.keys())
print(bag.values())

# Tuples
print(bag.items())

# i,e in golang looping like an index and element
for i,e in bag.items():
    print("KEY:",i," ","VALUE:",e)