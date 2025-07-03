# create
nums = {1, True, 2, False, 3, 4, 0}

print(nums)

# there is no index or key value pairs 
# we can check for this though
print(3 in nums)


# add
# single
nums.add(8)
# more than one
nums.update({10,11,12})
print(nums)


# interesting set methods
one = {1, 2, 3, 4, 5, 6, 7,7,8,8,8,99,10,11,12}
bigger_set = one.union({11, 12, 13, 14})
print(bigger_set)


bigger_set.intersection_update(one)
print(bigger_set)
bigger_set.symmetric_difference_update({10, 11, 12, 99})
print(bigger_set)