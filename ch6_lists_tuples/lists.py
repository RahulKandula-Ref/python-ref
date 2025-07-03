family = ['Rahul', 'Sravya', 'LA']

# access
print(family[0])
print(family[1:])
print(family[0:2])

# search
print('Somechild' in family)
print(family.index('Sravya'))

# exapand lists
manjeera = []

manjeera.append('security')

manjeera += ['sameeksha', 'office staff']

manjeera.extend(family)


# replace / insert
manjeera.insert(1, 'second shift security')

manjeera[3:3] = ['sam mom', 'sam bro']

manjeera[0:2] = ['assam sec', 'owl security', 'head chief']



# delete

not_present = manjeera.pop()

manjeera.remove('owl security')

del manjeera[0:2]

family.clear()

print(len(manjeera))
print(manjeera)

print(len(family))



# sort and reverse
manjeera.append('ZeeKeeper')
manjeera.sort(key=str.lower)
print(manjeera)

nums = [4, 43, 1, 2, 60]
nums.reverse()
print(nums)

nums.sort(reverse=True)
print(nums)
print(sorted(nums, reverse=False))
print(nums)


# making a copy of the list
numscopy = nums.copy()
mynums = list(nums)
justnums = nums[:]