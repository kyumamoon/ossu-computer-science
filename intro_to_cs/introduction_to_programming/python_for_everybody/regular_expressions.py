# Regex/Regular Expression is a smart Find/Search
# import using "import re"
# Regular expressions is a string method to do stuff with strings
# So it can use escape characters or formatting symbols to do various functions.

# Methods
# search() returns true or false whether found
# findall() returns values extracted when found

# ^     Matches beginning of line
# $     Matches end of line
# .     Matches any character
# \s    Matches whitespace
# \S    Matches non-whitespace characters
# *     Repeats character zero or more times
# *?    Repeats character zero or more times (not greedy)
# +     Repeats character one or more times
# +?    Repeats character one or more times (not greedy)
# [aeiou]   Matches a single character in the listed set
# [^XYZ]    Matches a single character NOT in listed set
# [a-z0-9]  The set of characters can include a range
# (         Indicates where to start the extraction
# )         Indicates where to end the extraction
# [^ ]      Match non-blank character
# \         Escape character to escape any of symbols above

# Searching a subString to see if it starts with it. Using ^ before the string.
import re

stringTest = "i am a string"
print(re.search('^i',stringTest))

# Searching a subString to see if it contains the subString
stringTest2 = "i am a string"
print(re.search('am',stringTest))

# Special functiosn to match a subString with changing lengths.
# Using ^, start of string
# Using ., match any character after the symbol
# Using *, any number of times.
# GREEDY MATCHING, Using ^.+ will find the largest subString that meets criteria.
# Adding ? will make less greedy. ^.+?
stringTest3 = "X-Sieve: CMU Sieve 2.3"
print(re.search('^X.*:',stringTest3))
# Basically, search line if it starts with "X" and get any character after it a number of times and stop at the string ":"

# Extracting stuff from string
stringTest4 = "I AM 50 and 20 and 1 plus 6216"
print(re.findall('[0-9]+',stringTest4))
# [0-9]+ extracts any number that has one or more digits in it.
# [0-9] extracts any digit found, individually

# Non-Whitespace symbol
# \S
# Matches any non-whitespace characters
stringTest5 = "steitjqiti ajdiawjdwa@1312312 test"
print(re.findall('\S+@\S+',stringTest5))

# Specific returning using parenthesis
# Checks whether stringTest5 starts with that string, and find/extract the thing inside parenthesis
print(re.findall('^steitjqiti (\S+@\S+)',stringTest5))

stringTest6 = "From stephen.marquard@uct.ac.za Sat Jun 5 09:14:16 2008"
print(re.findall('@(\S+)',stringTest6))
print(re.findall('@(\S*)',stringTest6))
print(re.findall('@([^ ]*)',stringTest6))

stringTest7 = "From stephen.marquard@uct.ac.za Sat Jun 5 09:14:16 2008 0.4211 test"
print(re.findall('[0-9:]+',stringTest7))