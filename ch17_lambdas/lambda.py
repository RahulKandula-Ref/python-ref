squared = lambda num : num * num

print(squared(5))

lambda a, b : a + b


#########################

def funcBuilder(x):
    return lambda num : num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(2))
print(addTwenty(2))