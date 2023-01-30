def printName(name,age):
    print(name)
    return "ABC",age # returns array

test = input("ENTER YO NAME: ")
x = printName(test,32)
print(x[0],x[1])

# Functions within functions

def funcA(x):
    def funcB():
        x = "abc"
        print(x)
    funcB()
funcA()