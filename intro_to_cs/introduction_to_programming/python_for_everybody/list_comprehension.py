# Create List Comprehension using square brackets.
# []

# Initiate list order/variables in parenthesis, basically what format for the lists that the list comprehension should produce each iteration of a tuple.
# [(e,i)]

# Loop through the tuple to get i(key) and e(value).
# [(e,i) for i,e in tupleVariable]
# this prints out a reversed version of the tuple elements

t = (("A",3),("B",2),("C",1))
print(t)

print([(e,i) for i,e in t])
