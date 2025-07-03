c_nums = [2, 23, 4, 5, 67, 4]

s_nums = map(lambda n : n * n, c_nums)
print(list(s_nums))

e_nums = filter(lambda n : n%2 == 0, c_nums)
print(list(e_nums))


from functools import reduce
f_mems = ("sravya", "rahul", "mores")
count_chars = reduce(lambda cnt, s : cnt + len(s), f_mems, 0)
print(count_chars)