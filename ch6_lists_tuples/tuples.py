mytuple = ('rahul', 34, 6, 65, 67, 'pass')

#unpack
(name, *marks, verdict) = (mytuple)

print(name)
print(verdict)
print(marks)

# can be created with a list
mylist = [5, 3, 4]
# accepting it as argument
tuple_from_list = tuple(mylist)
print(tuple_from_list)