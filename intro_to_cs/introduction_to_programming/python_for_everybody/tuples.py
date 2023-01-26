# Tuples are immutable, cannot change its content, cant use any altering methods on a tuple as would on a list.
# Tuples are like lists.
# Tuples more efficient than lists when making temp variables
# Can use operators on tuples. ><== etc

print((1,2,3) > (0,2,3))
# true because only compares first index of tuple


# Assigning variables and creating tuples.
x,y = (1,5)
print(x) # 1
print(y) # 5

# Transforming dict to a tuple
bag = {"money":10,"coins":50,"mask":1}
tuples = bag.items()
print(tuples)

for i,e in tuples:
    print("KEY:",i)
    print("VALUES:",e)

# Sorting Tuples by keys using sorted() method
print(sorted(tuples))
# Sorting by ascending/descending
print(sorted(tuples,reverse = True))